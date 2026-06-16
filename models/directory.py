from models.file import File
class Directory:

    def __init__(self, name):
        self.name = name
        self.parent = None
        self.subdirectories = {}
        self.files = {}

    def to_dict(self):

        return {
            "name": self.name,
            "subdirectories": {
                name: directory.to_dict()
                for name, directory in self.subdirectories.items()
            },
            "files": {
                name: file.to_dict()
                for name, file in self.files.items()
            }
        }
    
    @classmethod
    def from_dict(cls, data):

        directory = cls(data["name"])

    # for Restoring subdirectories
        for dirname, dirdata in data["subdirectories"].items():

            child = cls.from_dict(dirdata)

            child.parent = directory

            directory.subdirectories[dirname] = child

    # for Restoring  files
        for filename, filedata in data["files"].items():

            restored_file = File.from_dict(filedata)

            directory.files[filename] = restored_file

        return directory