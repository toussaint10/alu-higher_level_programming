#!/usr/bin/python3
import sys

if _name_ == "_main_":
    total = 0
    for i in range(len(sys.argv)):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
