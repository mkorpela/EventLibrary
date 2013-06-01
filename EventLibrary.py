import time
from collections import deque
from robot.libraries.BuiltIn import BuiltIn

class EventLibrary(object):

      def __init__(self):
          self._events = deque()
          self._no_condition = lambda: True

      def invoke_later(self, keyword, *arguments):
          self._events.appendleft((self._no_condition, keyword, arguments))

      def invoke_after(self, delay, keyword, *arguments):
          self._events.appendleft((self._time_condition(delay), keyword, arguments))

      def _time_condition(self, delay):
          condition_time = float(delay)+time.time()
          return lambda: time.time() >= condition_time

      def execute_event_loop(self):
          while self._events:
            condition, keyword, arguments = self._events.pop()
            if condition():
              BuiltIn().run_keyword(keyword, *arguments)
            else:
              self._events.appendleft((condition, keyword, arguments))
            time.sleep(0) #GIL prevents other threads if this is busy .. so must yeild
                
