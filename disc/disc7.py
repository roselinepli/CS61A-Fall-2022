class Student:
    extension_days = 3

    def __init__(self, name, staff):
        self.name = name
        self.understanding = 0
        staff.add_student(self)
        print("Added", self.name)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class Professor:

    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1

    def grant_more_extension_days(self, student, days):
        student.extension_days = days


class Email:
    """Every email object has 3 instance attributes: the message, the name, and the
    recipient name.
    >>> email = Email('hello', 'Alice', 'Bob')
    >>> email.msg
    'hello'
    >>> email.sender_name
    'Alice'
    >>> email.recipient_name
    'Bob'
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name


class Server:
    """Each Server has an instance attribute clients, which is a dictionary
    that associates client names with client objects."""
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the client it is addressed to."""
        client_name = email.recipient_name
        client = self.clients[client_name]
        client.receive(email)

    def register_client(self, client: 'Client', client_name: str):
        """Takes a client object and client_name and adds them to the
        clients instance attribute."""
        self.clients[client_name] = client


class Client:
    """Every Client has instance attributes name(which is used for addressing emails to
    the client), server(which is used to send emails out to other clients), and inbox(a
    list of all emails the client has received).

    >>> s = Server()
    >>> a = Client(s, 'Alice')
    >>> b = Client(s, 'Bob')
    >>> a.compose('Hello, World!', 'Bob')
    >>> b.inbox[0].msg
    'Hello, World!'
    >>> a.compose('CS 61A Rocks!', 'Bob')
    >>> len(b.inbox)
    2
    >>> b.inbox[1].msg
    'CS 61A Rocks!'
    """
    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.name = name

        server.register_client(self, name)

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the given recipient client."""
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)

    def receive(self, email):
        """Take an email and add it to the inbox of this client."""
        self.inbox.append(email)


def client_tests():
    s = Server()
    a = Client(s, 'Alice')
    b = Client(s, 'Bob')
    msg = "Hello, world!"
    a.compose(msg, 'Bob')
    actual = b.inbox[0].msg
    assert actual == msg, f"expected '{msg}', got '{actual}'"


if __name__ == '__main__':
    client_tests()


