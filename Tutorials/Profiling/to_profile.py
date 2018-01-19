import random

def get_number():
    return random.randint(0, 100)

def add2():
    return get_number() + 2

values = []
for x in range(100000):
    values.append(add2())

print(sum(values))


