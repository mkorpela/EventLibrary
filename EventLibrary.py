import time
from collections import deque
from robot.libraries.BuiltIn import BuiltIn

class EventLibrary(object):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self
        self._events = deque()
        self._no_condition = lambda: True

    def _end_keyword(self, name, attributes):
        BuiltIn().run_keyword("go_through_events")

    def invoke_later(self, keyword, *arguments):
        """
        The keyword will be executed when it is its turn in the event queue.
        """
        event = (self._no_condition, keyword, arguments)
        self._events.appendleft(event)
        return event

    def invoke_after(self, delay, keyword, *arguments):
        """
        The keyword will be executed when it is its turn in the event queue and the given delay has gone.
        """
        event = (self._time_condition(delay), keyword, arguments)
        self._events.appendleft(event)
        return event

    def _time_condition(self, delay):
        condition_time = float(delay)+time.time()
        return lambda: time.time() >= condition_time

    def invoke_when(self, condition, keyword, *arguments):
        """
        The keyword will be executed when it is its turn in the event queue and the given keyword condition doesn't fail
        """
        event = (self._keyword_condition(condition), keyword, arguments)
        self._events.appendleft(event)
        return event

    def _keyword_condition(self, keyword):
        return lambda: BuiltIn().run_keyword_and_return_status(keyword)

    def go_through_events(self):
        if not self._events:
            return
        condition, keyword, arguments = event = self._events.pop()
        if condition():
            BuiltIn().run_keyword(keyword, *arguments)
        else:
            self._events.appendleft(event)

    def wait_until_events_happened(self, *events):
        waited = list(events)
        while set(self._events).intersection(set(waited)):
            self.go_through_events()
            time.sleep(0) #GIL prevents other threads if this is busy .. so must yeild
            
