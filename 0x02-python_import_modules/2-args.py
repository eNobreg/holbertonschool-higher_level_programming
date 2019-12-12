#!/usr/bin/python3
if __name__ == "__main__":
    import sys
argc = len(sys.argv)
print("{} arguments:".format(argc - 1))
for i in range(1, argc):
    print("{}: {}".format(i, sys.argv[i]))
