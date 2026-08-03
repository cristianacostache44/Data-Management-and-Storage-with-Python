
import random

class Number:

    def __init__(self, a, b):
        self.nr = random.randrange(a,b)

    def __str__(self):
        return str(self.nr)