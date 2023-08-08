#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dt = abs(number) % 10
if dt > 5:
    print(f"Last digit of {number:d} is {dt:d} and is greater than 5")
if dt == 0:
    print(f"Last digit of {number:d} is {dt:d} and is 0")
if dt < 6 and dt != 0:
    print(f"Last digit of {number:d} is {dt:d} and is less than 6 and not 0")
