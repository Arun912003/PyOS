# PyOS - Terminal Based Operating System Simulator

## Overview

PyOS is a terminal-based Operating System Simulator built entirely using Core Python and Object-Oriented Programming principles.

The project simulates a hierarchical file system and provides common operating system functionalities such as file management, directory navigation, user authentication, permissions, command history, logging, and persistent storage.

The primary objective of this project is to strengthen problem-solving skills, OOP concepts, data structures, recursion, file handling, and backend engineering fundamentals.

---

## Features

### File System Operations

* Create directories (`mkdir`)
* Remove empty directories (`rmdir`)
* Remove directories recursively (`rmr`)
* Navigate directories (`cd`)
* Display current directory (`pwd`)
* List files and folders (`ls`)
* Tree view of the complete file system (`tree`)

### File Operations

* Create files (`create`)
* Read file contents (`read`)
* Write file contents (`write`)
* Delete files (`delete`)
* Copy files (`copy`)
* Move files (`move`)
* Rename files (`rename`)
* Search files and directories (`find`)
* View file metadata (`fileinfo`)

### User Management

* User registration
* User login/logout
* Current user tracking (`whoami`)
* Delete account
* Admin role support
* List all users (Admin only)

### Security & Permissions

* File ownership
* Permission control using `chmod`
* Role-based access control
* Admin privilege management

### System Utilities

* Command history
* Activity logs
* Disk usage statistics (`diskinfo`)
* Help command
* About command
* Version information
* Terminal clear functionality

### Data Persistence

All data is persisted using JSON files:

* users.json
* filesystem.json
* history.json
* logs.json

Data remains available even after restarting the application.

---

## Project Structure

```text
PyOS
│
├── main.py
│
├── models
│   ├── user.py
│   ├── file.py
│   └── directory.py
│
├── services
│   ├── auth.py
│   ├── filesystem.py
│   ├── history.py
│   ├── logger.py
│   └── help.py
│
├── data
│   ├── users.json
│   ├── filesystem.json
│   ├── history.json
│   └── logs.json
│
└── README.md
```

---

## Concepts Used

### Object-Oriented Programming

* Classes
* Objects
* Encapsulation
* Modular Design

### Data Structures

* Tree Data Structure
* Dictionaries
* Lists

### Algorithms

* Recursive Tree Traversal
* Depth First Search (DFS)

### Backend Concepts

* Authentication
* Authorization
* Role-Based Access Control (RBAC)
* Serialization & Deserialization
* Exception Handling

---

## Available Commands

### Directory Commands

```bash
mkdir <dirname>
rmdir <dirname>
rmr <dirname>
cd <dirname>
pwd
ls
tree
```

### File Commands

```bash
create <filename>
write <filename>
read <filename>
delete <filename>
copy <source> <destination>
move <file> <directory>
rename <oldname> <newname>
find <name>
fileinfo <filename>
chmod <filename> <permission>
```

### User Commands

```bash
register <username> <password>
login <username> <password>
logout
whoami
deleteaccount
```

### Admin Commands

```bash
listusers
deleteuser <username>
```

### System Commands

```bash
history
logs
diskinfo
help
clear
version
about
exit
```

---

## How To Run

Clone the repository:

```bash
git clone <repository-url>
```

Navigate into the project:

```bash
cd PyOS
```

Run the application:

```bash
python3 main.py
```

---

## Sample Usage

```bash
register arun 1234
login arun 1234

mkdir Documents
cd Documents

create notes.txt
write notes.txt

tree
find notes.txt

diskinfo
history
logs
```

---

## Future Enhancements

* Password hashing
* Multi-level permissions
* User groups
* File compression
* Backup and restore
* Export logs
* Network simulation
* Process management

---

## Author

Arun Gupta

Built as a backend engineering and operating system simulation project using Python.
