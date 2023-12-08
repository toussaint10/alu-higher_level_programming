#!/usr/bin/python3
import hidden_4

if _name_ == "_main_":
    """Print all names defined by hidden_4 module"""
    names = dir(hidden_4)
   for name in names:
       if name[:2] != "__":
            print(name)
