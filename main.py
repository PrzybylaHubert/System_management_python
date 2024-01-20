from src import monitor_processes
from src import memory_analysis
from src import file_explorer
from src import io_monitor
from src import network_analysis
from src import user_accounts
from src import service_monitor

def main_menu():
    print("")
    print("Główne Menu")
    print("1. Monitor Procesów")
    print("2. Analiza Pamięci")
    print("3. Eksplorator Systemu Plików")
    print("4. Monitor Wejścia-Wyjścia")
    print("5. Analiza Aktywności Sieciowej")
    print("6. Konta Użytkowników")
    print("7. Monitor Usług Systemowych")
    print("8. Wyjdź")

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
            user_accounts.display_user_accounts()
        elif user_choice == '7':
            service_monitor.display_service_status()
        elif user_choice == '8':
            print("Wyjście z programu.")
            break
        else:
            print("Niepoprawny wybór. Wybierz ponownie.")
