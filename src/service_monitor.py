import psutil
import platform

def display_service_status():
    print()
    print("Monitor Usług Systemowych")
    try:
        while True:
            print("Dostępne opcje:")
            print("1. Wyświetl listę działających usług")
            print("2. Wyjdź")

            user_choice = input("Wybierz opcję: ")

            if user_choice == '1':
                display_running_services()
            elif user_choice == '2':
                break
            else:
                print("Niepoprawny wybór. Wybierz ponownie.")

    except KeyboardInterrupt:
        print("Monitor Usług Systemowych zakończony.")
    finally:
        print("Powrót do Menu Głównego.")

def display_running_services():
    services = get_running_services()
    print("\nLista działających usług:")
    for service_info in services:
        print(f"Usługa: {service_info['name']}")
        print(f"Status: {service_info['status']}")
        print(f"Uruchamiana przez: {service_info['username']}")
        print(f"Ścieżka do pliku wykonywalnego: {service_info['path']}")
        print("-" * 30)
    print("\n")

def get_running_services():
    services = []
    if platform.system().lower() == "windows":
        for service in psutil.win_service_iter():
            service_info = {
                'name': service.display_name(),
                'status': service.status(),
                'username': service.username(),
                'path': service.binpath(),
            }
            services.append(service_info)
    elif platform.system().lower() == "linux":
        # Dodaj odpowiednią obsługę usług dla systemów Linux
        pass
    return services

if __name__ == "__main__":
    display_service_status()
