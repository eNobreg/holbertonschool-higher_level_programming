#!/usr/bin/python3
for i in range(0, 101):
    if i / 10 < i % 10:
        if i < 89:
            print("{:d}".format(i), end=", ")
        else:
            print("{:d}".format(i))
