# System Monitoring Toolkit

This project is a System Monitoring Toolkit developed using Python. The entire project was prompted and generated using ChatGPT. Please note that it has been tested only on Windows 10.

## Features
1. **Process Monitor**: Displays information about current processes, including process ID, CPU usage, memory, etc.
2. **Memory Analysis**: Monitors and analyzes the usage of RAM and virtual memory.
3. **I/O Monitor**: Monitors input-output operations, such as disk reads/writes.
4. **Network Activity**: Monitors network activity, displaying open ports and active connections.
5. **User Accounts**: Displays a list of logged-in users, their full names, and activities.
6. **File Explorer**: Simple tool for navigating the file system, viewing properties of files and folders.
7. **Service Monitor**: Monitors and displays the status of running system services.

## Requirements

To run this project, you need to have the following dependencies installed:

- **psutil**: A cross-platform library for retrieving information on running processes and system utilization.

- **platform**: A built-in Python module providing an interface to access information about the underlying platform (operating system).

### Installing Dependencies

Before running the toolkit, make sure you have [pip](https://pip.pypa.io/en/stable/installation/) installed on your system.


To install the required dependencies, you can use the following commands:

```bash
pip install psutil
```

```bash
pip install platform
```
## Usage
1. Clone the repository.
2. Ensure you have Python installed.
3. Run `main.py` to access the main menu and choose from the available options.

## Documentation
For more details on each functionality, refer to the:
- [English Documentation](documentation/documentation.md)
- [Polska Dokumentacja](documentation/documentation_pl.md)

## Note
This project was generated using ChatGPT, and its primary testing environment is Windows 10. Use it in other environments at your own discretion.
