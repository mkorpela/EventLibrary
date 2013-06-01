*** Settings ***
Library  EventLibrary

*** Variables ***
${SKY}   dark

*** Test Cases ***
Invoke Later Test
  Invoke Later  Log  Hello
  Invoke Later  Log  World
  Execute Event Loop

Invoke After Test
  Invoke After  0.5  Log  Printed after 0.5 seconds
  Execute Event Loop

Invoke When Test
  Set sky color to blue
  Invoke When  Sky is orange  Log  Impossible!!!
  Invoke After  0.1  Set sky color to orange
  Execute Event Loop

Invoking in the event loop Test
  Invoke Later  Set sky color to blue
  Invoke When   Sky is orange   Invoke Later   Log  the end
  Invoke When   Sky is blue     Set sky color to orange
  Execute Event Loop

*** Keywords ***
Set sky color to blue
  Set test variable  ${SKY}  blue

Set sky color to orange
  Set test variable  ${SKY}  orange

Sky is orange
  Should Be Equal    ${SKY}  orange

Sky is blue
  Should Be Equal    ${SKY}  blue
