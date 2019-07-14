EventLibrary
============

Event Library for Robot Framework.
This allows one to say that when A happens then do X and when B happens then do Y.

One could argue that there are 3 levels of waiting:

1) Sleeper: Sleep
2) Poller: Wait Until
3) Observer: Invoke When

This library aims to allow you to act with the 3 option.

<code>
*** Settings ***
Library  EventLibrary

*** Variables ***
${SKY}   dark

*** Test Cases ***
Invoke Later Test
  ${hello}=  Invoke Later  Log  Hello
  ${world}=  Invoke Later  Log  World
  Wait Until Events Happened  ${hello}  ${world}

Invoke After Test
  ${event}=  Invoke After  0.5  Log  Printed after 0.5 seconds
  Wait Until Events Happened  ${event}

Invoke When Test
  Set sky color to blue
  ${orange}=  Invoke When  Sky is orange  Log  Impossible!!!
  Invoke After  0.1  Set sky color to orange
  Wait Until Events Happened  ${orange}

Invoking in the event loop Test
  Invoke Later  Set sky color to blue
  ${ora}=  Invoke When   Sky is orange   Log end
  Invoke When   Sky is blue     Set sky color to orange
  Wait Until Events Happened  ${ora}

*** Keywords ***
Log end
  ${ends}=  Invoke Later  Log  the end
  Wait Until Events Happened  ${ends}

Set sky color to blue
  Set test variable  ${SKY}  blue

Set sky color to orange
  Set test variable  ${SKY}  orange

Sky is orange
  Should Be Equal    ${SKY}  orange

Sky is blue
  Should Be Equal    ${SKY}  blue

</code>

