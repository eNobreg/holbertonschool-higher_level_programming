#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
hidden = dir(hidden_4)
for names in hidden:
    if names[0] != "_":
        print("{}".format(names))
