
## **Mastermind(z możliwością łamania kodu przez komputer)**

**Opis zadania**

- Możliwość samodzielnego odgadnięcia kodu lub zadanie kodu 'komputerowi'
 - Okno z polem tekstowym na 4 cyfry, listą odpowiedzi, przyciskiem “Sprawdź”,  oraz przyciskiem “Reset”
- Po rozpoczęciu gry generowana jest losowa liczba (kod) złożona z czterech cyfrod 1 do 6 włącznie (1111, 1112, 1113, ..., 3455, 3456, 3461, 3462, ..., 6665, 6666). W wypadku gry z 'komputerem' możliwość wyboru kodu samodzielnie
- Gracz wpisuje cztery cyfry od 1 do 6 do pola tekstowego i naciska przycisk “Sprawdź”. W wypadku gry z 'komputerem' przycisk sprawdź służy do przejścia do następnego strzału komputera
- Do pola odpowiedzi dopisywana jest odpowiedź zawierająca: liczbę wpisaną przez gracza, liczbę cyfr na poprawnych pozycjach oraz liczbę cyfr występujących w kodzie, ale na złych pozycjach.
- Jeśli gracz lub komputer wpisał liczbę będącą kodem, wyświetlane jest okno z napisem “Wygrana”.
- Jeśli gracz lub komputer po 12 próbach nie odgadł kodu, wyświetlane jest okno z napisem “Przegrana”.
- Reguły gry (m.in. sprawdzanie strzału) realizowana jest przez osobną klasę, dziedziczą po niej klasy HumanPlayer i ComputerPlayer.

**Testy**

- Wyświetlenie (wypisanie w konsoli) wylosowanego kodu, wpisanie odpowiedzi z błędnymi cyframi -oczekiwana informacja o braku poprawnych trafień
- Wyświetlenie wylosowanego kodu, wpisanie odpowiedzi z poprawnymi cyframi w złych miejscach -oczekiwana informacja o niepoprawnym położeniu.
- Wyświetlenie wylosowanego kodu, wpisanie odpowiedzi z dwoma poprawnymi cyframi w dobrych miejscach i dwoma poprawnymi w złych miejscach -oczekiwana informacja o dwóch trafieniach i dwóch złych pozycjach.
- Wyświetlenie wylosowanego kodu, wpisanie poprawnej odpowiedzi -oczekiwana informacja o wygranej.
- Wpisanie 12 razy niepoprawnego kodu -oczekiwana informacja o przegranej.
- Próba wpisania niepoprawnego kodu do pola odpowiedzi (mniej lub więcej niż 4 znaki, znaki nie będące cyframi od 1 do 6) -oczekiwane nieuznanie kodu (gracz nie traci tury).
- Wpisanie 10 kodów, resetowanie gry, wpisanie 5 kodów -oczekiwane normalne działanie gry (czy licznik tur resetuje się po wciśnięciu “Reset”).
- Sprawdzenie sprawności algorytmu łamiącego kod
