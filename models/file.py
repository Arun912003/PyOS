class File:

    def __init__(self, name, owner):
        self.name = name
        self.content = ""
        self.owner = owner
        self.permission = "write"

    def to_dict(self):

        return {
            "name": self.name,
            "content": self.content,
            "owner": self.owner,
            "permission": self.permission
        }
    @classmethod
    def from_dict(cls, data):

        file = cls(
            data["name"],
            data.get("owner")
            
        )
        file.permission = data.get(
            "permission",
            "write"
        )

        file.content = data["content"]

        return file