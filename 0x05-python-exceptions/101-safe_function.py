#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        r = fct(*args)
        return r
    except Exception as err:
        print("Exception: {}".format(err), file=stderr)
        return None
