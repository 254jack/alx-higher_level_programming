#!/usr/bin/python3.8
if __name__ == '__main__':
    import hidden_4

    names = dir(hidden_4)
    sorted = sorted(name for name in names if not name.startswith("__"))
    for name in sorted:
        print(name)
