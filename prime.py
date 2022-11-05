#!/usr/bin/env python3
import sys
import math

def isPrime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

if __name__ == "__main__":
    _nl = [] # initial numberlist
    nlp = [] # numberlist with exlusively primes

    try:
        # Make an array from 1 - sys.argv[1]
        for x in range(1,int(sys.argv[1])+1):_nl.append(x)

        # Append prime values from nl to nlp
        for n in range(0,len(_nl)+1):
            if n > 1:
                if isPrime(n)==True:nlp.append(n)
        print(nlp)

    except OSError as e:
        sys.exit(e.message)
