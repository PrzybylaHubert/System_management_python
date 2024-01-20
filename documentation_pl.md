# Dokumentacja Narzędzi Monitorujących System

## Monitor Procesów

### Funkcjonalność
Narzędzie do wyświetlania listy bieżących procesów z informacjami takimi jak ID procesu, zużycie CPU, pamięci itp.

### Opcje
1. Wyświetl listę bieżących procesów.
2. Posortuj listę procesów według zużycia CPU, pamięci lub nazwy.
3. Filtruj procesy według nazwy.

### Dodatkowe Informacje
Użytkownicy nie otrzymują pełnej listy od razu; zamiast tego otrzymują po jednym procesie na kliknięcie. <br>
Plik: `monitor_processes.py`

### Oczekiwany Wynik
- Lista bieżących procesów z informacjami takimi jak ID procesu, zużycie CPU, pamięci itp.
- Posortowana lista procesów w zależności od wybranej opcji (CPU, pamięć lub nazwa).
- Wyniki procesów po filtrowaniu według nazwy.

## Analiza Pamięci

### Funkcjonalność
Narzędzie do monitorowania zużycia RAM i pamięci wirtualnej.

### Opcje
1. Wyświetl informacje o zużyciu RAM.
2. Wyświetl informacje o zużyciu pamięci wirtualnej.

### Dodatkowe Informacje
Plik: `memory_analysis.py`

### Oczekiwany Wynik
- Informacje o zużyciu RAM lub pamięci wirtualnej.

## Eksplorator Systemu Plików

### Funkcjonalność
Proste narzędzie do przeglądania struktury systemu plików, wyświetlania właściwości plików i folderów.

### Opcje
1. Wyświetl strukturę systemu plików.
2. Wyświetl właściwości wybranego pliku/folderu.
3. Przejdź do innych folderów.

### Dodatkowe Informacje
Wpisanie `..` cofa użytkownika o jeden katalog, a `.` nie wykonuje żadnych działań. <br>
Plik: `file_explorer.py`

### Oczekiwany Wynik
- Struktura systemu plików.
- Informacje o wybranym pliku/folderze.
- Zmieniona bieżąca lokalizacja po nawigacji przez foldery.

## Monitor Wejścia-Wyjścia

### Funkcjonalność
Narzędzie do śledzenia operacji wejścia-wyjścia, takich jak odczyt/zapis na dysku.

### Opcje
1. Wyświetl informacje o operacjach wejścia-wyjścia.

### Dodatkowe Informacje
Plik: `io_monitor.py`

### Oczekiwany Wynik
- Informacje o operacjach wejścia-wyjścia, takie jak liczba odczytów, liczba zapisów, bajty odczytane i bajty zapisane.

## Monitor Aktywności Sieciowej

### Funkcjonalność
Narzędzie do monitorowania aktywności sieciowej, wyświetlanie otwartych portów, aktywnych połączeń itp.

### Opcje
1. Wyświetl aktualną konfigurację sieciową.
2. Wyświetl informacje o otwartych portach.
3. Wyświetl informacje o aktywnych połączeniach.

### Dodatkowe Informacje
Plik: `network_activity.py`

### Oczekiwany Wynik
- Informacje o aktywności sieciowej, takie jak otwarte porty, aktywne połączenia i aktualna konfiguracja sieci.

## Konta Użytkowników

### Funkcjonalność
Narzędzie do wyświetlania listy zalogowanych użytkowników i ich aktywności.

### Opcje
1. Wyświetl listę zalogowanych użytkowników.
2. Wyświetl aktywność wybranego użytkownika (wymagana pełna nazwa użytkownika).

### Dodatkowe Informacje
Plik: `user_accounts.py