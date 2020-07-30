import unittest


class Greeter:
    """Class to handle greeting of entrants at hotel
    """

    def __init__(self, boss):
        """init function

        Args:
        boss -- (string) the name of the hotel boss

        Returns:
        None

        """
        self.boss = boss
        self.last_entered = None

    def enters(self, visitor):
        """tracking for who has last entered

        Args:
        visitor -- (string) the name of the entrant

        Returns:
        None

        """
        self.last_entered = visitor

    def greet(self):
        """geets the last entrant

        Args:
        None

        Returns:
        (string) A greeting based on the last entrant

        """
        if (self.last_entered == self.boss):
            greeting = f"Hello, {self.boss}"
        elif (self.last_entered != None):
            greeting = f"Welcome, {self.last_entered}"
        else:
            greeting = None
        self.last_entered = None
        return greeting


class TestGreeter(unittest.TestCase):

    def test_boss(self):
        g = Greeter('Chuck')
        g.enters('Chuck')
        self.assertEqual(g.greet(), "Hello, Chuck")

    def test_not_boss(self):
        g = Greeter('Chuck')
        g.enters('John')
        self.assertEqual(g.greet(), "Welcome, John")

    def test_no_new_entries(self):
        g = Greeter('Chuck')
        g.enters('John')
        g.greet()
        self.assertEqual(g.greet(), None)


if __name__ == '__main__':
    unittest.main()
