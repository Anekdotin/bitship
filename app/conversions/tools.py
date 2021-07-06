import string
import random


def randomstring(length):
    letters = string.ascii_lowercase
    x = (''.join(random.choice(letters) for i in range(length)))
    return x

