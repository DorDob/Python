import random


def add(a, b):
    return a + b


sum_two = add(11, 21)

def multiply(a, b):
    return a * b

ml = multiply(3, 5)

# vc = volume_cuboid(3, 5, 12)
# vb = volume_ball(10)
# wgc =

def volume_cuboid(a, b, c):
    return a * b * c


vc = volume_cuboid(3, 5, 12)


def volume_ball(r):
    return 4 / 3 * 3.14 * r ** 3


vb = volume_ball(10)
wgc = vb > vc
print(wgc)

n = vc / vb
print(f' cuboid volume is {n}' 'ball volume is')


#
def square(a):
    return a ** 2


n21 = square(21)
n67 = square(67)
print(n21)
print(n67)

# wylosuj dwa elementy z listy

l = [1, 3, 5, 11, 13, 21, 43, 56, 9]


def number():
    n1 = random.choice(l)
    n2 = random.choice(l)
    return n1, n2


wylosowano = number()
print(wylosowano)


# albo
def two_elements(input_list):
    a = random.choice(input_list)
    b = random.choice(input_list)
    return a, b


# ablo

l1, l2 = number(l)
print(l1, l2)

# KALASY
