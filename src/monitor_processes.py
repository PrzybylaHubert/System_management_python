import psutil

def display_process_info(process):
    print(f"ID procesu: {process.pid}")
    print(f"Zużycie CPU: {process.cpu_percent()}%")
    print(f"Zużycie pamięci: {process.memory_info().rss / (1024 * 1024):.2f} MB")
    print(f"Nazwa procesu: {process.name()}")
    print("-" * 30)

def run_monitor():
    print("")
    print("Monitor Procesów")
    try:
        while True:
            filter_by = input("Podaj fragment nazwy procesu do filtrowania (wpisz 'q' aby wrócić do menu głównego): ")
            if filter_by.lower() == 'q':
                break

            sort_options = {'cpu': 'cpu_percent', 'memory': 'memory_info'}
            print("Dostępne opcje sortowania:")
            for option in sort_options:
                print(f"- {option}")

            sort_by = input("Wybierz opcję sortowania (cpu/memory): ").lower()
            if sort_by not in sort_options:
                print("Niepoprawny wybór sortowania.")
                continue

            processes = list(psutil.process_iter(["pid", "name", "cpu_percent", "memory_info"]))
            processes = [process for process in processes if filter_by.lower() in process.name().lower()]

            # Poprawiona linia sortowania
            if sort_by == 'memory':
                processes.sort(key=lambda x: getattr(x.memory_info(), 'rss') / (1024 * 1024), reverse=True)
            else:
                processes.sort(key=lambda x: getattr(x, sort_options[sort_by])(), reverse=True)

            for process in processes:
                display_process_info(process)

                user_input = input("Naciśnij Enter, aby wyświetlić kolejny proces, lub 'q' aby zakończyć: ")
                if user_input.lower() == 'q':
                    break

    except KeyboardInterrupt:
        print("Monitor Procesów zakończony.")
    finally:
        print("Powrót do Menu Głównego.")