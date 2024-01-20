# System Monitoring Toolkit Documentation

## 1. Process Monitor

### Functionality
Tool to display a list of current processes with information such as process ID, CPU usage, memory, etc.

### Options
1. Display a list of current processes.
2. Sort the process list by CPU usage, memory, or name.
3. Filter processes by name.

### Additional Information
Users do not receive the entire list at once; instead, they receive one process per click. <br>
File: `monitor_processes.py`

### Expected Output
- List of current processes with information such as process ID, CPU usage, memory, etc.
- Sorted list of processes based on the chosen option (CPU, memory, or name).
- Filtered results of processes based on name.

## 2. Memory Analysis

### Functionality
Tool to monitor the usage of RAM and virtual memory.

### Options
1. Display information about the usage of RAM.
2. Display information about the usage of virtual memory.

### Additional Information
File: `memory_analysis.py`

### Expected Output
- Information about the usage of RAM or virtual memory.

## 3. File Explorer

### Functionality
Simple tool for navigating the file system, viewing properties of files and folders.

### Options
1. Display the file system structure.
2. Display the properties of a selected file/folder.
3. Navigate through folders.

### Additional Information
Typing `..` moves the user back by one directory, and `.` does not perform any actions. <br>
File: `file_explorer.py`

### Expected Output
- File system structure.
- Information about a selected file/folder.
- Changed current location after navigating through folders.

## 4. I/O Monitor

### Functionality
Tool to track input-output operations, such as disk reads/writes.

### Options
1. Display information about input-output operations.

### Additional Information
File: `io_monitor.py`

### Expected Output
- Information about input-output operations, such as read count, write count, read bytes, and write bytes.

## 5. Network Activity

### Functionality
Tool to monitor network activity, displaying open ports, active connections, and current network configuration.

### Options
1. Display current network configuration.
2. Display information about open ports.
3. Display information about active connections.

### Additional Information
File: `network_activity.py`

### Expected Output
- Information about network activity, such as open ports, active connections, and current network configuration.

## 6. User Accounts

### Functionality
Tool to display a list of logged-in users and their activities.

### Options
1. Display a list of logged-in users.
2. Display the activity of a selected user (full username required).

### Additional Information
File: `user_accounts.py`

### Expected Output
- List of logged-in users, including their username and full name.
- Activity of the selected user, including processes currently running.

## 7. Service Monitor

### Functionality
Tool to display a list of running system services/daemons.

### Options
1. Display a list of running services.

### Additional Information
File: `service_monitor.py`

### Expected Output
- List of running services with their names, status, and path to the executable file.

---

This documentation covers the functionality, available options, any additional information, and the expected output for each tool in the System Monitoring Toolkit.
