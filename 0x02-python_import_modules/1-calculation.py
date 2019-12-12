#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

a = 5
b = 10
print("{} + {} = {}".format(b, a, add(b, a)))
print("{} - {} = {}".format(b, a, sub(b, a)))
print("{} * {} = {}".format(b, a, mul(b, a)))
print("{} / {} = {}".format(b, a, div(b, a)))
