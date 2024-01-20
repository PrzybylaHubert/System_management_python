import os

def explore_file_system():
    current_directory = os.getcwd()

    print("")
    print("Eksplorator Systemu Plików")
    try:
        while True:
            print(f"Aktualny katalog: {current_directory}")
            print("Dostępne opcje:")
            print("1. Wyświetl zawartość bieżącego katalogu")
            print("2. Wyświetl właściwości pliku lub folderu")
            print("3. Przejdź do innego katalogu")
            print("4. Wyjdź")

            user_choice = input("Wybierz opcję: ")

            if user_choice == '1':
                print(f"\nZawartość katalogu {current_directory}:\n")
                for item in os.listdir(current_directory):
                    print(item)
                print("\n")
            elif user_choice == '2':
                file_or_folder = input("Podaj nazwę pliku lub folderu: ")
                file_path = os.path.join(current_directory, file_or_folder)

                if os.path.exists(file_path):
                    print("\nWłaściwości pliku lub folderu:")
                    print(f"Ścieżka: {file_path}")
                    print(f"Rozmiar: {os.path.getsize(file_path)} bajtów")
                    print(f"Uprawnienia: {oct(os.stat(file_path).st_mode)[-3:]}")
                    print("\n")
                else:
                    print("Podany plik lub folder nie istnieje.\n")
            elif user_choice == '3':
                new_folder = input("Podaj nazwę katalogu, do którego chcesz przejść (wpisz '..' aby cofnąć, '.' aby zostać): ")
                
                if new_folder == '..':
                    current_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
                elif new_folder == '.':
                    pass  # Zostawiamy bieżący katalog
                else:
                    new_path = os.path.join(current_directory, new_folder)

                    if os.path.exists(new_path) and os.path.isdir(new_path):
                        current_directory = new_path
                    else:
                        print("Podany katalog nie istnieje.\n")
            elif user_choice == '4':
                break
            else:
                print("Niepoprawny wybór. Wybierz ponownie.")

    except KeyboardInterrupt:
        print("Eksplorator Systemu Plików zakończony.")
    finally:
        print("Powrót do Menu Głównego.")
