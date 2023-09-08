3-infinite_add.py

#!/usr/bin/python3

if __name__ == "__main__":
    """Prints addition of all given arguments."""
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
