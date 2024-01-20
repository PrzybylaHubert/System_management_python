import psutil

def monitor_io():
    print("")
    print("Monitor Wejścia-Wyjścia")
    try:
        while True:
            print("Dostępne opcje:")
            print("1. Wyświetl informacje o operacjach wejścia-wyjścia")
            print("2. Wyjdź")

            user_choice = input("Wybierz opcję: ")

            if user_choice == '1':
                io_counters = psutil.disk_io_counters(perdisk=True)

                print("\nInformacje o operacjach wejścia-wyjścia:")
                for disk, io_info in io_counters.items():
                    print(f"Dysk {disk}:")
                    print(f"  Odczyty: {io_info.read_count}")
                    print(f"  Zapisy: {io_info.write_count}")
                    print(f"  Bajty odczytane: {io_info.read_bytes}")
                    print(f"  Bajty zapisane: {io_info.write_bytes}")
                    print("-" * 30)
                print("\n")
            elif user_choice == '2':
                break
            else:
                print("Niepoprawny wybór. Wybierz ponownie.")

    except KeyboardInterrupt:
        print("Monitor Wejścia-Wyjścia zakończony.")
    finally:
        print("Powrót do Menu Głównego.")
