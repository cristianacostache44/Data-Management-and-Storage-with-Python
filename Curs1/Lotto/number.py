
import random

class Number:

    def __init__(self, a, b, c):
        self.nr = random.sample(range(a,b), c)

    def __str__(self):
        return str(self.nr)