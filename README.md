EventLibrary
============

Event dispatcher Library for Robot Framework

<code>
    *** Test Cases ***

    Odottele valoja

      Laukase juttu mikä pistää punasen valon joskus palaa

      Venaa et punanen valo palaa
      
      Laukase juttu mikä pistää sinisen valon joskus palaan
      
      Laukase juttu mikä pistää vihreen valon joskus palaan
      
      Venaa et sininen valo palaa
      
      Laukase juttu mikä pistää keltasen valon joskus palaan
      
      Venaa et vihree valo palaa
      
      Venaa et keltanen valo palaa


    Eventtijuttui
      
      Laukase juttu mikä pistää punasen valon joskus palaan
      
      Lisää eventti  sit ku se punanen valo palaa niin   Laukase juttu mikä pistää vihreen valon joskus palaan    timeout 5s
      
      Lisää eventti  sit ku se vihree valo palaa niin    Hyvä hyvä
      
      Laukase juttu mikä pistää sinisen valon joskus palaan
      
      Lisää eventti  sit ku se sininen valo palaa niin   Laukase juttu mikä pistää keltasen valon joskus palaan
      
      Lisää eventti  sit ku se keltanen valo palaa niin   Hyvä hyvä
      
      Käynnistä eventtiluuppi ja odota et kaikki on käsitelty     event timeout 30s
</code>

http://en.wikipedia.org/wiki/Event_dispatching_thread
