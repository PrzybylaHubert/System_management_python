import monitor_processes

def main_menu():
    print("Główne Menu")
    print("1. Monitor Procesów")
    print("2. Inna Funkcjonalność (do dodania)")
    print("3. Wyjdź")

if __name__ == "__main__":
    while True:
        main_menu()
        user_choice = input("Wybierz opcję: ")

        if user_choice == '1':
            monitor_processes.run_monitor()
        elif user_choice == '2':
            # Dodaj inną funkcjonalność tutaj
            print("Wybrano Inną Funkcjonalność (do dodania)")
        elif user_choice == '3':
            print("Wyjście z programu.")
            break
        else:
            print("Niepoprawny wybór. Wybierz ponownie.")