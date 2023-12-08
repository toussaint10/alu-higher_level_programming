#!/usr/bin/python3

if _name_ == "__main__":
    import sys
    
    total = 0
    for i in range(len(sys.argv)):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
