from datetime import datetime   # for timestamps

class QueueClass:
    def __init__(self):
        self.items = []         # queue storage

    def enqueue(self, item):
        self.items.append(item) # add to queue

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # remove first
        return None

    def is_empty(self):
        return len(self.items) == 0   # check empty

    def get_all(self):
        return self.items             # return list

class User:
    def __init__(self, username):
        self.username = username      # store name
        self.role = "User"            # default role


class Admin(User):
    def __init__(self, username):
        super().__init__(username)    # inherit User
        self.role = "Admin"           # set role


class Analyst(User):
    def __init__(self, username):
        super().__init__(username)
        self.role = "Analyst"         # set role

class Incident:
    def __init__(self, incident_id, incident_type, severity, description):
        self.incident_id = incident_id        # ID
        self.incident_type = incident_type    # type
        self.severity = severity              # severity
        self.description = description        # description
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # time created
        self.status = "Open"                  # default status

    def __str__(self):
        return (f"[{self.incident_id}] {self.incident_type} | "
                f"Severity: {self.severity} | Status: {self.status} | "
                f"Time: {self.timestamp}")    # readable output

class IncidentManager:
    def __init__(self):
        self.queue = QueueClass()     # incident queue