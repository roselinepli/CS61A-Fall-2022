import math
pi = math.pi

class Shape:
    """All geometric shapes will inherit from this Shape class."""
    def __init__(self, name):
        self.name = name

    def area(self):
        """Returns the area of a shape"""
        print("Override this method in ", type(self))

    def perimeter(self):
        """Returns the perimeter of a shape"""
        print("Override this function in ", type(self))


class Circle(Shape):
    """A circle is characterized by its radii"""
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2


class RegPolygon(Shape):
    """A regular polygon is defined as a shape whose angles and side lengths are all the same.
    This means the perimeter is easy to calculate. The area can also be done, but it's more
    inconvenient."""

    def __init__(self, name, num_sides, side_length):
        super().__init__(name)
        self.mum_sides = num_sides
        self.side_length = side_length

    def perimeter(self):
        return self.side_length * self.num_sides


class Square(RegPolygon):
    def __init__(self, name, side_length):
        super().__init__(name, 4, side_length)

    def area(self):
        return self.side_length ** 2


class Triangle(RegPolygon):
    def __init__(self, name, side_length):
        super().__init__(name, 3, side_length)

    def area(self):
        constant = math.sqrt(3)/4
        return constant * self.side_length ** 2


class Pet:

    def __init__(self, name, owner):
        self.is_alive = True
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Cat(Pet):

    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner)
        self.lives = lives

    def talk(self):
        print(self.name + " says meow!")

    def lose_life(self):
        if self.lives > 0:
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False
        else:
            print("This cat has no more lives to lose.")

    def revive(self):
        if not self.is_alive:
            self.__init__(self.name, self.owner)
        else:
            print("This cat still has lives to lose.")

class NoisyCat(Cat):
    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner, lives)

    def talk(self):
        for _ in range(2):
            super().talk()