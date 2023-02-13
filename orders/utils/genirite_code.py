import random


def genirite_code(lenght=12):
    numbers='12345678ABCDEFGabcd'
    return ''.join(random.choice(numbers) for _ in range (lenght))