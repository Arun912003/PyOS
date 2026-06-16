import json
import os
from datetime import datetime

class Logger:

    def __init__(self):

        self.log_file = "data/logs.json"

        self.logs = []

        self.load()

    def load(self):

        if os.path.exists(self.log_file):

            with open(self.log_file, "r") as file:

                try:
                    self.logs = json.load(file)

                except:
                    self.logs = []

    def save(self):

        with open(self.log_file, "w") as file:

            json.dump(self.logs, file, indent=4)

    def add_log(self, message):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_entry = f"[{timestamp}] {message}"

        self.logs.append(log_entry)

        self.save()

    def show_logs(self):

        if not self.logs:
            print("No logs found")
            return

        for log in self.logs:
            print(log)