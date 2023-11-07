#!/usr/bin/python3
if __name__ == "__name__":
    """Print All Hidden Directories"""
    import hidden_4

    for i i dir(hidden_4):
        if i[:2] != "__":
            print(i)
