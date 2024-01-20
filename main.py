import monitor_processes
import memory_analysis
import file_explorer
import io_monitor
import network_analysis

def main_menu():
    print("")
    print("Główne Menu")
    print("1. Monitor Procesów")
    print("2. Analiza Pamięci")
    print("3. Eksplorator Systemu Plików")
    print("4. Monitor Wejścia-Wyjścia")
    print("5. Analiza Aktywności Sieciowej")
    print("6. Inna Funkcjonalność (do dodania)")
    print("7. Wyjdź")

if __name__ == "__main__":
    while True:
        main_menu()
        user_choice = input("Wybierz opcję: ")

        if user_choice == '1':
            monitor_processes.run_monitor()
        elif user_choice == '2':
            memory_analysis.analyze_memory()
        elif user_choice == '3':
            file_explorer.explore_file_system()
        elif user_choice == '4':
            io_monitor.monitor_io()
        elif user_choice == '5':
            network_analysis.analyze_network_activity()
        elif user_choice == '6':
            # Dodaj inną funkcjonalność tutaj
            print("Wybrano Inną Funkcjonalność (do dodania)")
        elif user_choice == '7':
            print("Wyjście z programu.")
            break
        else:
            print("Niepoprawny wybór. Wybierz ponownie.")
