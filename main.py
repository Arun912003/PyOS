from services.filesystem import FileSystem
from services.history import History
from services.logger import Logger
from services.auth import Auth
from services.help import Help
import subprocess

fs = FileSystem()
history=History()
logger = Logger()
auth = Auth()

while True:
    try:
        username = (
            auth.current_user.username
            if auth.current_user
            else "guest"
        )

        command = input(
            f"{username}@{fs.get_current_path()}> "
        ).strip()

        if not command:
            continue
        history.add_command(command)

        parts = command.split()

        cmd = parts[0]
    except Exception as e:
        print(f"Error: {e}")

    if cmd == "mkdir":

        if len(parts) < 2:
            print("Usage: mkdir foldername")
            continue

        fs.mkdir(parts[1])
        logger.add_log(f"Directory '{parts[1]}' created")

    elif cmd == "ls":

        fs.ls()
    
    elif cmd == "history":

        history.show_history()

    elif cmd == "logs":

        logger.show_logs()

    elif cmd == "cd":

        if len(parts) < 2:
            print("Usage: cd foldername")
            continue

        fs.cd(parts[1])

    elif cmd == "pwd":

        fs.pwd()

    elif cmd == "register":

        if len(parts) != 3:
            print("Usage: register username password")
            continue

        auth.register(parts[1], parts[2])

    elif cmd == "login":

        if len(parts) != 3:
            print("Usage: login username password")
            continue

        auth.login(parts[1], parts[2])

    elif cmd == "logout":

        auth.logout()

    elif cmd == "whoami":

        auth.whoami()
    
    elif cmd == "create":

        if len(parts) < 2:
            print("Usage: create filename")
            continue

        if auth.current_user is None:
            print("Please Login first")
            continue

        fs.create_file(
            parts[1],
            auth.current_user.username
            
        )
        logger.add_log(f"File '{parts[1]}' created")

    elif cmd == "write":

        if len(parts) < 2:
            print("Usage: write filename")
            continue

        fs.write_file(parts[1], auth.current_user.username)
        logger.add_log(f"File '{parts[1]}' updated")

    elif cmd == "read":

        if len(parts) < 2:
            print("Usage: read filename")
            continue

        fs.read_file(parts[1])

    elif cmd == "delete":

        if len(parts) < 2:
            print("Usage: delete filename")
            continue
        if auth.current_user is None:
            print("Please Login First")
            continue

        fs.delete_file(
            parts[1],
            auth.current_user.username,
            auth.is_admin()
        
        )
        logger.add_log(f"File '{parts[1]}' deleted")

    elif cmd == "deleteuser":

        if not auth.is_admin():

            print("Admin access required")

            continue

        if len(parts) != 2:

            print("Usage: deleteuser username")

            continue

        auth.delete_user(parts[1])

    elif cmd == "deleteaccount":

        auth.delete_current_user()

    elif cmd == "rmdir":

        if len(parts) < 2:

            print("Usage: rmdir dirname")

            continue

        fs.rmdir(parts[1])

    elif cmd == "chmod":

        if len(parts) != 3:

            print(
                "Usage: chmod filename permission"
            )

            continue

        if auth.current_user is None:

            print("Please login first")

            continue

        fs.chmod(
            parts[1],
            parts[2],
            auth.current_user.username
        )

#shows the tree like hierarchy structure of the folders and files inside the root

    elif cmd == "tree":

        fs.tree()

# used to find the path of the file

    elif cmd == "find":

        if len(parts) < 2:

            print("Usage: find filename")

            continue

        fs.find(parts[1])

# move one file to directory 

    elif cmd == "move":

        if len(parts) != 3:

            print(
                "Usage: move filename directory"
            )

            continue

        fs.move_file(
            parts[1],
            parts[2]
        )

#copy source file to new file
    elif cmd == "copy":

        if len(parts) != 3:

            print(
                "Usage: copy source_file new_file"
            )

            continue

        fs.copy_file(
            parts[1],
            parts[2]
        )

#this shows like overall disk usage like total directories , total file , storage used

    elif cmd == "diskinfo":

        fs.diskinfo()

# this will delete all the directory data include files and all remove -recursive

    elif cmd == "rmr":

        if len(parts) != 2:

            print(
            "Usage: rmr dirname"
            )

            continue

        fs.rmr(parts[1])

#this will simply show all the commands and you can take help if needed
    elif cmd == "help":

        Help.show()

    elif cmd == "rename":

        if len(parts) != 3:

            print(
                "Usage: rename oldname newname"
            )   

            continue

        if auth.current_user is None:

            print("Please login first")

            continue

        fs.rename_file(
            parts[1],
            parts[2],
            auth.current_user.username
        )

    elif cmd == "fileinfo":

        if len(parts) != 2:

            print(
                "Usage: fileinfo filename"
            )

            continue

        fs.fileinfo(parts[1])

    elif cmd == "clear":

        subprocess.run(["clear"])

    elif cmd == "version":

        print("PyOS v1.0")

    elif cmd == "about":

        print("\nPyOS")
        print("Terminal-Based Operating System Simulator")
        print("Built using Python, OOP and JSON Persistence\n")

    elif cmd == "listusers":

        if not auth.is_admin():

            print("Admin access required")

            continue

        auth.list_users()

    elif cmd == "exit":

        print("Exiting PyOS...")
        break


    else:

        print("Invalid Command")

    