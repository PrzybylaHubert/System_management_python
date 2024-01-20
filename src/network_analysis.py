import psutil

def analyze_network_activity():
    print("")
    print("Analiza Aktywności Sieciowej")
    try:
        while True:
            print("Dostępne opcje:")
            print("1. Wyświetl aktualną konfigurację sieciową")
            print("2. Wyświetl otwarte porty")
            print("3. Wyświetl aktywne połączenia")
            print("4. Wyjdź")

            user_choice = input("Wybierz opcję: ")

            if user_choice == '1':
                display_network_configuration()
            elif user_choice == '2':
                display_open_ports()
            elif user_choice == '3':
                display_active_connections()
            elif user_choice == '4':
                break
            else:
                print("Niepoprawny wybór. Wybierz ponownie.")

    except KeyboardInterrupt:
        print("Analiza Aktywności Sieciowej zakończona.")
    finally:
        print("Powrót do Menu Głównego.")

def display_network_configuration():
    network_info = psutil.net_if_addrs()
    print("\nAktualna konfiguracja sieciowa:")
    for interface, addresses in network_info.items():
        print(f"\nInterfejs: {interface}")
        for address in addresses:
            print(f"  {address.family.name} address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast address: {address.broadcast}")

def display_open_ports():
    open_ports = get_open_ports()
    print("\nOtwarte porty:")
    for port_info in open_ports:
        print(f"Port: {port_info['port']}")
        print(f"  Adres IP: {port_info['ip']}")
        print(f"  Stan: {port_info['status']}")
        print("-" * 30)
    print("\n")

def display_active_connections():
    active_connections = get_active_connections()
    print("\nAktywne połączenia:")
    for connection in active_connections:
        print(connection)
    print("\n")

def get_open_ports():
    open_ports = []
    for port in psutil.net_connections(kind='inet'):
        if port.status == psutil.CONN_LISTEN:
            port_info = {
                'port': port.laddr.port,
                'ip': port.laddr.ip,
                'status': port.status,
            }
            open_ports.append(port_info)
    return open_ports

def get_active_connections():
    active_connections = []
    for connection in psutil.net_connections(kind='inet'):
        if connection.status == psutil.CONN_ESTABLISHED:
            active_connections.append(connection)
    return active_connections

if __name__ == "__main__":
    analyze_network_activity()
