from datetime import datetime
from QueueClass import Queue


class User: ## Setup User class
    def __init__(self, username):
        self.username = username
        self.role = "User"


class Admin(User): ## Setup admin calling from User Class
    def __init__(self, username):
        super().__init__(username)
        self.role = "Admin"


class Analyst(User): ## Setup Analyst calling from User Class
    def __init__(self, username):
        super().__init__(username)
        self.role = "Analyst"


class Incident: ## Setup Incident class to contain all info about an incident
    def __init__(self, incident_id, incident_type, severity, description):
        self.incident_id = incident_id
        self.incident_type = incident_type
        self.severity = severity
        self.description = description
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.status = "Open"

    def __str__(self):
        return (f"[{self.incident_id}] {self.incident_type} | "
                f"Severity: {self.severity} | Status: {self.status} | "
                f"Time: {self.timestamp}")


class IncidentManager: ## Setup IncidentManager Class that deals with managing incidents and Queue
    def __init__(self):
        self.queue = Queue()

    def add_incident(self, incident):
        self.queue.enqueue(incident) ## Add incident into the Queue
        print(f"---------------\nAdded incident {incident.incident_id}\n---------------")

    def resolve_incident(self):
        if self.queue.is_empty(): ## Checks if queue is empty
            print("---------------\nNo Incidents found\n---------------")
        else:
            incident = self.queue.dequeue() ## Resolve incident from top of the Queue
            incident.status = "Resolved"
            print(
                f"Incident Resolved\nID: {incident.incident_id} | Type: {incident.incident_type} | Severity: {incident.severity} | Description: {incident.description} | Status: {incident.status} | Time: {incident.timestamp}")

    def list_incidents(self):
        if self.queue.is_empty():
            print("No Incidents found")
        for incident in list(self.queue.items): ## Loops through to find all incidents and prints them out
            print(f"ID: {incident.incident_id} | Type: {incident.incident_type} | Severity: {incident.severity} | Description: {incident.description} | Status: {incident.status} | Time: {incident.timestamp}")

    def search_incidents(self, search_id):
        if self.queue.is_empty():
            print("---------------\nNo incidents found\n---------------")
            return

        found = False  # track if we found it or not

        for incident in list(self.queue.items): ## Loops through the incidents and if search ID matches one of them then print that one out
            if incident.incident_id == search_id:
                print(f" ID: {incident.incident_id} | Type: {incident.incident_type} | Severity: {incident.severity} |  | Description {incident.description} |  Status: {incident.status} | Time: {incident.timestamp}")
                found = True
                break  # stop once found
        if not found:
            print(f"---------------\nNo ID with {search_id} was found\n---------------")


def load_incidents(filename, manager): ## Function to load incident from a file
    try:
        with open(filename, "r") as file: ## Open readonly
            lines = file.readlines()
            if not lines:
                print("---------------\nNo Incidents found in the file\n---------------")
            for line in lines: ## Loops each line in the file
                each_line = line.strip().split(",") ## Splits up each line by every comma
                if len(each_line) != 4: ## Makes sure theirs exactly 4 parts if not skip that line
                    print(f"Skipping invalid line: {line.strip()}")
                    continue
                load_id = each_line[0] ## Grabbing each part of the line and assinging to a variable
                load_type = each_line[1]
                load_severity = each_line[2]
                load_description = each_line[3]

                new_incident = Incident(load_id, load_type, load_severity, load_description) ## Puts everything togeather into a new incident var
                manager.add_incident(new_incident) ## Loads in a new incident
                print(f"Successfully Loaded New incident {new_incident.incident_id}")
    except FileNotFoundError: ## if file is not found print out
        print(f"{filename} not found")


def main():
    try:
        manager = IncidentManager() ## Grabs incident manager class
        print("Welcome to Incident Management System")
        username = input("Enter your username: ")
        while not username.strip(): ## Ensures username is not empty and loops till its not
            print("Username cannot be empty")
            username = input("Enter your username: ")

        role = input("Please enter your role ( Admin | Analyst | ): ")

        if role == "admin":
            user = Admin(username)
        elif role == "analyst":
            user = Analyst(username)
        else:
            user = User(username)

        print(f"Login Successful: Welcome {user.role} {user.username}!")

        load_incidents("incidents.txt", manager) ## Load incidents from the txt file

        while role.lower() == "admin": ## If the role is admin run this loop
                try:
                    choice = int(input("Incident Management Menu\n 1. View Incidents\n 2. Add Incidents\n 3. Resolve Incidents\n 4. Exit\n Enter your choice: ")) ## Choice system by number

                    if choice == 1:
                        print("----------------")
                        manager.list_incidents()
                        print("----------------")

                    elif choice == 2:
                        add_id = input("Enter new Incident ID: ")
                        add_type = input("Enter new Incident Type: ")
                        add_severity = input("Enter new Incident Severity: ")
                        add_description = input("Enter new Incident Description: ")
                        manager.add_incident(Incident(add_id, add_type, add_severity, add_description)) ## Adds a new incident based on the info
                        print(f"---------------\nSuccessfully Added Incident {add_id}\n---------------")

                    elif choice == 3:
                        manager.resolve_incident()

                    elif choice == 4:
                        print(f"---------------\nGoodbye {user.username}\n Exiting....\n---------------")
                        break

                    else:
                        print("---------------\nPlease enter a valid choice.\n---------------")

                except ValueError:
                    print("---------------\nInvalid choice. Please enter a number.\n---------------")


        while role.lower() == "analyst":
                try:
                    choice = int(input(
                        "Incident Management Menu\n 1. View Incidents\n 2. Search Incidents by ID \n 3. Exit\n Enter your choice: "))

                    if choice == 1:
                        print("----------------")
                        manager.list_incidents()
                        print("----------------")

                    elif choice == 2:
                        search = input("Enter Incident ID: ")
                        manager.search_incidents(search)

                    elif choice == 3:
                        print(f"---------------\nGoodbye {user.username}\n Exiting....\n---------------")
                        break

                    else:
                        print("---------------\nPlease enter a valid choice.\n---------------")

                except ValueError:
                    print("---------------\nInvalid choice. Please enter a number.\n---------------")

        while role.lower() == "user" or not role.lower() == "admin" and not role.lower() == "analyst": ## Run this role
                try:
                    choice = int(input(
                        "Incident Management Menu\n 1. View Incidents\n 2. Exit\n Enter your choice: "))

                    if choice == 1:
                        print("----------------")
                        manager.list_incidents()
                        print("----------------")

                    elif choice == 2:
                        print(f"---------------\nGoodbye {user.username}\n Exiting....\n---------------")
                        break

                    else:
                        print("---------------\nPlease enter a valid choice.\n---------------")

                except ValueError:
                    print("---------------\nInvalid choice. Please enter a number.\n---------------")
    except KeyboardInterrupt: ## If program is forcefully stopped run this print instead of erroring
        print(f"\n---------------\nKeyboard Interruption Detected | Exiting....\n---------------")

main()