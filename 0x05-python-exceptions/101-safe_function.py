#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as exp:
        print("Exception: {}".format(exp.args[0]), file=sys.stderr)
        return None
