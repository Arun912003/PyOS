import json
import os

from models.user import User


class Auth:

    def __init__(self):

        self.users_file = "data/users.json"

        self.users = {}

        self.current_user = None

        self.load()

        # Create default admin if not exists
        if "admin" not in self.users:

            admin = User(
                "admin",
                "admin123",
                "admin"
            )

            self.users["admin"] = admin

            self.save()

    def load(self):

        if os.path.exists(self.users_file):

            with open(self.users_file, "r") as file:

                try:

                    data = json.load(file)

                    for user_data in data:

                        user = User.from_dict(user_data)

                        self.users[user.username] = user

                except:

                    self.users = {}

    def save(self):

        with open(self.users_file, "w") as file:

            json.dump(
                [user.to_dict() for user in self.users.values()],
                file,
                indent=4
            )

    def is_admin(self):

        return (
            self.current_user
            and
            self.current_user.role == "admin"
        )

    def register(self, username, password):

        if username in self.users:

            print("User already exists")
            return

        user = User(username, password)

        self.users[username] = user

        self.save()

        print("Registration successful")

    def login(self, username, password):

        if username not in self.users:

            print("User not found")
            return

        user = self.users[username]

        if user.password != password:

            print("Invalid password")
            return

        self.current_user = user

        print(f"Welcome {username}")

    def logout(self):

        if not self.current_user:

            print("No user logged in")
            return

        print(f"{self.current_user.username} logged out")

        self.current_user = None

    def whoami(self):

        if self.current_user:

            print(self.current_user.username)

        else:

            print("No user logged in")

    def list_users(self):

        for user in self.users.values():

            print(
                f"{user.username} ({user.role})"
            )

# can delete any user whether logined-in or not

    def delete_user(self, username):
        if username not in self.users:
            print("User not found")
            return
        del self.users[username]
        if (
            self.current_user
            and
            self.current_user.username == username
        ):

            self.current_user = None
        self.save()
        print(f"User '{username}' Deleted Successfully")

# this will only delete the current logged in user

    def delete_current_user(self):

        if self.current_user is None:

         print("Please login first")
         return

        username = self.current_user.username

        del self.users[username]

        self.current_user = None

        self.save()

        print(f"{username} deleted successfully")