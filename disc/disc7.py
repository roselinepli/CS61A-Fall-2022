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


    def register_client(self, client: 'Client', client_name: str):
        """Takes a client object and client_name and adds them to the
        clients instance attribute."""


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
        self.server = server
        self.name = name

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the given recipient client."""

    def receive(self, email):
        """Take an email and add it to the inbox of this client."""


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


class Button:

    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.times_pressed = 0

class Keyboard:
    """A Keyboard stores an arbitrary number of Buttons in a dictionary.
    Each dictionary key is a Button's position, and each dictionary vallue
    is the corresponding Button.
    >>> b1, b2 = Button(5, "H"), Button(7, "I)
    >>> k = Keyborad(b1, b2)
    >>> k.buttons[5].key
    'H'
    >>> k.press(7)
    'I'
    >>> k.press(0)
    ''
    >>> k.typing([5, 7])
    'HI'
    >>> k.typing([7, 5])
    'IH'
    >>> b1.times_pressed
    2
    >>> b2.times_pressed
    3
    """
    def __init__(self, *args):


    def press(self, pos):
        """Takes in a position of the buttton pressed, and
        returns that button's output."""


    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output."""


class TeamMember:
    def __init__(self, operation, prev_member=None):
        """
        A TeamMember object is instantiated by taking in an 'operation'
        and a TeamMember object 'prev_memver', which is the team member
        who "sits in front of" this current team member. A TeamMember also
        tracks a 'history' list, which contains the answers given by each
        individual team member.
        """

    def relay_calculate(self, x):
        """
        The relay_calculate method takes in a number 'x' and perfroms a replay
        by passing in 'x' to the first team member's 'operation'. Then, that
        answer is passed to the next member's operation, etc. until we get
        to the current TeamMember, in which case we return the final 'result'.
        """

    def relay_history(self):
        """
        Returns a list of the answers given by each team member in the most
        recent relay the current TeamMember has participated in.
        """

class Cat:
    def __init__(self, name, owner, lives=9):
        self.is_alive = True
        self.name = name
        self.owner = owner
        self.lives = lives

    def talk(self):
        return self.name + ' says meow!'

    @classmethod
    def cat_creator(cls, owner):
        """
        Returns a new instance of a Cat.
        This instance's name is "[owner]'s Cat", with [owner] being
        the name of its owner.
        >>> cat1 = Cat.cat_creator("Bryce")
        >>> isinstance(cat1, Cat)
        True
        >>> cat1.owner
        'Bryce'
        >>> cat1.name
        "Bryce's cat"
        >>> cat2 = Cat.cat_creator("Tyler")
        >>> cat2.owner
        'Tyler'
        >>> cat2.name
        "Tyler's Cat
        """
        name = owner + "'s cat"