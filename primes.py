from enum import Enum, auto

from random import randint, getrandbits

from random_ import randomNBits

class Algorithm:
    MILLER_RABIN = auto()
    ANOTHER = auto()


# Checks if a given number is prime
def millerRabin(p: int, rounds=8):
    def isComposite(p: int, d: int):
        a = randint(2, p - 1)

        x = pow(a, d, p)

        if x == 1 or x == p - 1:
            return False

        while d != p - 1:
            x = pow(x, 2, p)

            d *= 2

            if x == 1:
                return True
            if x == p - 1:
                return False

        return True
        '''
        for _ in range(1, s):
            x = pow(x, 2, p)

            if x == 1:
                return True

            elif x == p - 1:
                return False
        '''
        #return True
 
    if p == 2:
        return True

    if p % 2 == 0 or p % 3 == 0 or p % 5 == 0 or p % 7 == 0 or p % 11 == 0:
        return False

    d = p - 1

    while d % 2 == 0:
        d >>= 1

    for _ in range(rounds):
        if isComposite(p, d):
            return False

    return True

def getPrimeNBits(nBits: int, algorithm=Algorithm.MILLER_RABIN):
    p = randomNBits(nBits)
    i = 0
    
    if algorithm == Algorithm.MILLER_RABIN:
        while not millerRabin(p):
            p = randomNBits(nBits)

            i += 1
        print(f'Numbers tested: {i}')

        return p
    elif algorithm == Algorithm.ANOTHER:
        ...

    #return p
