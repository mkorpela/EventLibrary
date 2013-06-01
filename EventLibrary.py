from collections import deque
from robot.libraries.BuiltIn import BuiltIn

class EventLibrary(object):

      def __init__(self):
          self._events = deque()

      def invoke_later(self, keyword, *arguments):
          self._events.appendleft((keyword, arguments))

      def execute_event_loop(self):
          while self._events:
            keyword, arguments = self._events.pop()
            BuiltIn().run_keyword(keyword, *arguments)
            
                
