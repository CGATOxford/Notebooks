import random


def build_numbers(nnumbers):
    return [random.randint(0, 1000000) for x in range(nnumbers)]


def find_number(number, numbers):
    return number in numbers


numbers = build_numbers(100000)

nfound = 0
for number in range(10000):
    if find_number(number, numbers):
        nfound += 1

print(nfound)
