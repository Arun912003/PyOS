import json
import os

class History:

    def __init__(self):

        self.history_file = "data/history.json"

        self.commands = []

        self.load()

    def load(self):

        if os.path.exists(self.history_file):

            with open(self.history_file, "r") as file:

                try:
                    self.commands = json.load(file)

                except:
                    self.commands = []

    def save(self):

        with open(self.history_file, "w") as file:

            json.dump(self.commands, file, indent=4)

    def add_command(self, command):

        self.commands.append(command)

        self.save()

    def show_history(self):

        if not self.commands:

            print("No command history found")
            return

        for index, command in enumerate(self.commands, start=1):

            print(f"{index}. {command}")