#!/usr/bin/env python3
import sys

def isPrime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

if __name__ == "__main__":
    _nl = [] # initialize numberlist

    try:
        # Make an array from 1 - sys.argv[1]
        # Only put numbers that are prime in list
        for x in range(2,int(sys.argv[1])+1):
            if isPrime(x):_nl.append(x)

        # Print number list
        print(_nl)

    except OSError as e:
        # Other error
        sys.exit(e.message)

    except IndexError:
        # If user doesn't provide any argument
        sys.exit("Error:\n   IndexError!\nUsage:\n   " + sys.argv[0] + " <int>")

    except ValueError:
        # If user enters a non-number value as an argument
        sys.exit("Error:\n   '" + sys.argv[1] + "' is an invalid value\nUsage:\n   " + sys.argv[0] + " <int>")
