import psutil

def display_user_accounts():
    print()
    print("Konta Użytkowników")
    try:
        while True:
            print("Dostępne opcje:")
            print("1. Wyświetl listę zalogowanych użytkowników")
            print("2. Wyświetl aktywność użytkownika")
            print("3. Wyjdź")

            user_choice = input("Wybierz opcję: ")

            if user_choice == '1':
                display_logged_users()
            elif user_choice == '2':
                display_all_users_and_choose()
            elif user_choice == '3':
                break
            else:
                print("Niepoprawny wybór. Wybierz ponownie.")

    except KeyboardInterrupt:
        print("Konta Użytkowników zakończone.")
    finally:
        print("Powrót do Menu Głównego.")

def display_logged_users():
    logged_users = get_logged_users()
    print("\nZalogowani użytkownicy:")
    for user_info in logged_users:
        print(f"Użytkownik: {user_info['user']} ({user_info['full_name']})")
        print(f"Terminal: {user_info['terminal']}")
        print(f"Czas logowania: {user_info['login_time']}")
        print("-" * 30)
    print("\n")

def display_all_users_and_choose():
    logged_users = get_logged_users()
    print("\nWszyscy zalogowani użytkownicy:")
    for user_info in logged_users:
        print(f"Użytkownik: {user_info['user']} ({user_info['full_name']})")
    selected_username = input("\nPodaj pełną nazwę użytkownika, którego aktywność chcesz wyświetlić: ")
    display_user_activity(selected_username)

def display_user_activity(username):
    user_activity = get_user_activity(username)
    if user_activity:
        print(f"\nAktywność użytkownika {username}:")
        for activity_info in user_activity:
            print(f"Proces: {activity_info['name']}")
            print(f"ID Procesu: {activity_info['pid']}")
            print(f"Rozpoczęto: {activity_info['start_time']}")
            print("-" * 30)
        print("\n")
    else:
        print(f"\nBrak aktywności dla użytkownika {username}.\n")

def get_logged_users():
    logged_users = []
    for user in psutil.users():
        user_info = {
            'user': user.name,
            'full_name': "",  # Poprawka
            'terminal': user.terminal,
            'login_time': user.started,
        }
        try:
            user_info['full_name'] = get_full_username(user_info['user'])
        except KeyError:
            pass
        logged_users.append(user_info)
    return logged_users

def get_user_activity(username):
    user_activity = []
    for process in psutil.process_iter(['username', 'pid', 'create_time', 'name']):
        try:
            if process.info['username'] == username:
                activity_info = {
                    'name': process.info['name'],
                    'pid': process.info['pid'],
                    'start_time': process.info['create_time'],
                }
                user_activity.append(activity_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return user_activity

def get_full_username(username):
    try:
        return psutil.Process().username()
    except psutil.NoSuchProcess:
        return ""

if __name__ == "__main__":
    display_user_accounts()
