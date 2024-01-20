import psutil

def analyze_memory():
    print("")
    print("Analiza Pamięci")
    try:
        while True:
            print("Dostępne opcje:")
            print("1. Zużycie pamięci operacyjnej")
            print("2. Zużycie pamięci wirtualnej")
            print("3. Wyjdź")

            user_choice = input("Wybierz opcję: ")

            if user_choice == '1':
                print(f"Zużycie pamięci operacyjnej: {psutil.virtual_memory().percent}%")
            elif user_choice == '2':
                print(f"Zużycie pamięci wirtualnej: {psutil.swap_memory().percent}%")
            elif user_choice == '3':
                break
            else:
                print("Niepoprawny wybór. Wybierz ponownie.")

    except KeyboardInterrupt:
        print("Analiza Pamięci zakończona.")
    finally:
        print("Powrót do Menu Głównego.")
