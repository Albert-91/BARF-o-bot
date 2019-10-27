## intent: affirm
<!-- user wants to affirm /confirm -->
<!-- 
# basic cases -->
- ok
- tak
- mhm
- aha
- git
- gites
- spoko
- dobrze
- pewnie
- dokładnie
- oczywiście
- akceptuję
- potwierdzam
- zdecydowanie
- doskonale
- świetnie
- fantastycznie
<!-- 
# advanced cases -->
- tak proszę
- zdecydowanie tak
- bez wątpienia
- bardzo git
- bardzo dobrze
- bardzo ok
- bardzo fajnie
- bardzo w porządku
- absolutnie tak


## intent: deny
<!-- user wants to deny / regret -->
<!-- 
# basic cases -->
- nie
- nic
- nope
- nigdy
- odmawiam
- odmówię
- zaprzeczam
- zaprzeczę
<!--
# advanced cases -->
- absolutnie nie
- nie sądzę
- nie ma mowy
- nie bardzo
- nie, dziękuję
- nie, dzięki
- nie chcę
- nie chcę tego
- nie akceptuję
- nie mogę
- nie ma mowy 
- nie całkiem
- nieważne
- muszę zaprzeczyć
- muszę odmówić
- tym razem nie
- tym razem zaprzeczę
- tym razem odmówię
- już w niczym
- nie chcę nic
- nie chcę niczego
- nie ma opcji
- nie ma takiej mowy

## intent: stop
<!-- user wants to stop / cancel / break -->
- stop
- wyjdź
- wróć
- anuluj
- przerwa
- przerwij
- zatrzymaj

## intent: explain
- po co
- czemu
- dlaczego
- w jakim celu
- do czego
- wytłumacz
- wyjaśnij
- czy muszę
- dlaczego muszę
- co mogę
- ile mogę
 
## intent: entered_vehicle_type
<!-- user says a vehicle type -->
- [samochód](vehicle_type)
- [auto](vehicle_type:samochód)

## intent: menu
- menu
- start

## intent: entered_data
<!-- intent that catch user entered some data to prevent other intent be recognised in this case -->
- [1](int_number)
- [12](int_number)
- [123](int_number)

## intent: out_of_scope
- dupa
- qwerty
