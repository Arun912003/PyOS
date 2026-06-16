from models.directory import Directory
from models.file import File
import json

class FileSystem:

    def __init__(self):

        self.root = Directory("root")

        self.current_directory = self.root
        self.load()

# Basics Navigation Commands 

    def mkdir(self, dirname):

        if dirname in self.current_directory.subdirectories:
            print("Directory already exists")
            return
    
        new_directory = Directory(dirname)

        new_directory.parent = self.current_directory

        self.current_directory.subdirectories[dirname] = new_directory
        self.save()

        print(f"{dirname} created successfully")

    def ls(self):
        print("Directories:")

        for directory in self.current_directory.subdirectories:
            print(f"[DIR] {directory}")

        print("\nFiles:")

        for file in self.current_directory.files:
            print(f"[FILE] {file}")

    def cd(self, dirname):

        if dirname == "..":

            if self.current_directory.parent:
                self.current_directory = self.current_directory.parent

            return

        if dirname in self.current_directory.subdirectories:

            self.current_directory = self.current_directory.subdirectories[dirname]

        else:

            print("Directory not found")

    def pwd(self):

        path = []

        current = self.current_directory

        while current:

            path.append(current.name)

            current = current.parent

        print("/".join(reversed(path)))

#2. File Managements systems

#so here we are basically checking and creating the files
 
    def create_file(self, filename, owner):

        if filename in self.current_directory.files:
            print("File already exists")
            return
        
        new_file = File(
            filename,
            owner
            
        )
        self.current_directory.files[filename] = new_file
        self.save()
        print(f"{filename} created successfully")

# after that we need to like read the file so firstly we are checking file present or then we reading the content of the file

    def read_file(self,filename):
        if filename not in self.current_directory.files:
            print("file not found")
            return
        file=self.current_directory.files[filename]
        print(file.content)

# here we are simply writing the content after checking the filename present or not and then taking user input of the content

    def write_file(
            self,
            filename,
            current_user,
            is_admin = False
    ):

        file = self.current_directory.files[filename]

        if(
            file.owner != current_user
            and 
            not is_admin
        ):

            print("Permission denied")

            return

        if file.permission != "write":

            print("File is read-only")

            return
        
        if filename not in self.current_directory.files:
            print("file not found")
            return
        content = input("Enter content:")
        self.current_directory.files[filename].content=content
        self.save()
        print("Content saved")

# here we are checking the file by its name and then if want to delete then simply deleting the file

    def delete_file(
            self,
            filename,
            current_user,
            is_admin =False
            
    ):
        if filename not in self.current_directory.files:
            print("File not found")
            return
        
        file = self.current_directory.files[filename]
        
        if(
            file.owner != current_user
            and
            not is_admin
        ):

            print("Permission denied")
            return
        
        # Confirmation before deletion
        confirm = input(
            f"Delete file {filename}? (yes/no): "
        )

        if confirm.lower() != "yes":

            print("Operation cancelled")
            return
        
        del self.current_directory.files[filename]
        self.save()
        print("File deleted")

# for removing directories

    def rmdir(self, dirname):

        if dirname not in self.current_directory.subdirectories:

            print("Directory not found")
            return

        directory = self.current_directory.subdirectories[dirname]

        if directory.subdirectories or directory.files:

            print("Directory is not empty")
            return

        del self.current_directory.subdirectories[dirname]

        self.save()

        print(f"{dirname} deleted successfully")

#  to save the data in form JSON

    def save(self):

        data = self.root.to_dict()

        with open("data/filesystem.json", "w") as file:
            json.dump(data, file, indent=4)

#we want ki program start hone pe JSON load ho for that we written load function but the thing is ki abhi ye JSON sirf read
#karega, lakeen json ko wapas directory object me convert nahi kar rha for that directory.py file.py @classmethod
    def load(self):

        try:

            with open("data/filesystem.json", "r") as file:

                data = json.load(file)
                self.root= Directory.from_dict(data) #
                self.current_directory=self.root #

                print("Filesystem loaded")

        except:

            print("No saved filesystem found")


    def file_info(self, filename):

        if filename not in self.current_directory.files:
            print("File not found")
            return

        file = self.current_directory.files[filename]

        print(f"Name: {file.name}")
        print(f"Owner: {file.owner}")
        print(f"Content Length: {len(file.content)}")


    def chmod(self, filename, permission, current_user, is_admin =False):

        if filename not in self.current_directory.files:

            print("File not found")
            return

        file = self.current_directory.files[filename]

        if(
            file.owner != current_user
            and
            not is_admin
        ):

            print("Permission denied")
            return

        file.permission = permission

        self.save()

        print(
        f"Permission changed to {permission}"
        )

    def tree(self):

        self._print_tree(
            self.root,
            ""
    )
        
    def _print_tree(self, directory, prefix=""):

        print(prefix + directory.name)

    # Print subdirectories
        for subdir in directory.subdirectories.values():

            self._print_tree(
                subdir,
                prefix + "│   "
            )

    # Print files
        for file in directory.files.values():

            print(
                prefix + "│   "  + file.name
            )

    def find(self, target):

        results = []

        self._find_recursive(
            self.root,
            target,
            "root",
            results
        )

        if not results:

            print("No matching file or directory found")

            return

        for path in results:

            print(path)
    
    def _find_recursive(
        self,
        directory,
        target,
        current_path,
        results
    ):

    # Check current directory

        if directory.name == target:

            results.append(current_path)

    # Check files

        for file in directory.files.values():

            if file.name == target:

                results.append(
                    current_path + "/" + file.name
                )

    # Traverse subdirectories

        for subdir in directory.subdirectories.values():

            self._find_recursive(
                subdir,
                target,
                current_path + "/" + subdir.name,
                results
            )
    
    def get_directory(self, dirname):

        return self._get_directory_recursive(
            self.root,
            dirname
        )
    
    def _get_directory_recursive(
        self,
        directory,
        dirname
    ):

        if directory.name == dirname:

            return directory

        for subdir in directory.subdirectories.values():

            result = self._get_directory_recursive(
                subdir,
                dirname
            )

            if result:

                return result

        return None
    
    def move_file(
        self,
        filename,
        destination_dir
    ):

        if filename not in self.current_directory.files:

            print("File not found")

            return

        destination = self.get_directory(
            destination_dir
        )

        if destination is None:

            print("Destination directory not found")

            return

        file = self.current_directory.files[filename]

        destination.files[filename] = file

        del self.current_directory.files[filename]

        self.save()

        print(
            f"{filename} moved to {destination_dir}"
        )

    def copy_file(self, source_filename, new_filename):

        if source_filename not in self.current_directory.files:

            print("Source file not found")
            return

        if new_filename in self.current_directory.files:

            print("Destination file already exists")
            return

        source_file = self.current_directory.files[source_filename]

        new_file = File(
            new_filename,
            source_file.owner
        )

        new_file.content = source_file.content

        new_file.permission = source_file.permission

        self.current_directory.files[new_filename] = new_file

        self.save()

        print(
            f"{source_filename} copied to {new_filename}"
        )

    def diskinfo(self):

        directories, files, size = self._diskinfo_recursive(
            self.root
        )

        print(f"Total Directories: {directories}")
        print(f"Total Files: {files}")
        if size < 1024:

            print(f"Storage Used: {size} Bytes")

        elif size < 1024 * 1024:

            print(
                f"Storage Used: {size / 1024:.2f} KB"
            )

        else:

            print(
                f"Storage Used: {size / (1024 * 1024):.2f} MB"
            )

    def _diskinfo_recursive(self, directory):

        total_directories = 1
        total_files = 0
        total_size = 0

    # Files
        for file in directory.files.values():

            total_files += 1

            total_size += len(file.content)

    # Subdirectories
        for subdir in directory.subdirectories.values():

            d, f, s = self._diskinfo_recursive(
                subdir
            )

            total_directories += d
            total_files += f
            total_size += s

        return (
            total_directories,
            total_files,
            total_size
        )
    
    def rmr(self, dirname):

        if dirname not in self.current_directory.subdirectories:

            print("Directory not found")

            return
        
        confirm = input(
            f"Delete {dirname}? (yes/no): "
        )

        if confirm.lower() != "yes":

            print("Operation cancelled")

            return

        del self.current_directory.subdirectories[dirname]

        self.save()

        print(
            f"{dirname} and all contents deleted"
        )

    def rename_file(
        self,
        old_name,
        new_name,
        current_user
    ):

        if old_name not in self.current_directory.files:

            print("File not found")

            return

        if new_name in self.current_directory.files:

            print("File already exists")

            return

        file = self.current_directory.files[old_name]

        if file.owner != current_user:

            print("Permission denied")

            return

        file.name = new_name

        self.current_directory.files[new_name] = file

        del self.current_directory.files[old_name]

        self.save()

        print(
            f"{old_name} renamed to {new_name}"
        )

    def fileinfo(self, filename):

        if filename not in self.current_directory.files:

            print("File not found")

            return

        file = self.current_directory.files[filename]

        print(f"Name: {file.name}")

        print(f"Owner: {file.owner}")

        print(
            f"Permission: {file.permission}"
        )

        print(
            f"Size: {len(file.content)} Bytes"
        )

    def get_current_path(self):

        path = []

        current = self.current_directory

        while current is not None:

            path.append(current.name)

            current = current.parent
            
        path.reverse()

        return "PyOS/" + "/".join(path)