#!/usr/bin/python3
# Author: JDRZ


if __name__ == "__main__":
    import sys
    sum = 0
    if len(sys.argv) is 1:
        print("{}".format(sum))
    elif len(sys.argv) > 1:
        for x in range(1, len(sys.argv)):
            sum = sum + int(sys.argv[x])
        print("{}".format(sum))
