from enum import Enum, auto

from random import randint, getrandbits

from random_ import randomNBits, genSeed

class Algorithm:
    MILLER_RABIN = auto()
    ANOTHER = auto()

# Checks if a given number is prime
def millerRabin(p: int, rounds: int = 8) -> bool:
    """Checks if a given number is prime using the Miller-Rabin algorithm.

    Args:
        p: The number to check
        rounds: The number of rounds wanted in the check
    """

    def isComposite(p: int, d: int):
        """Verify if a given number is composite

        Args:
            p: The number to be verified
            d: The number of times p can be dived by 2
        """

        a = randint(2, p - 1)

        x = pow(a, d, p)

        if x == 1 or x == p - 1:
            return False

        while d != p - 1:
            x = x * x % p

            d *= 2

            if x == 1:
                return True
            if x == p - 1:
                return False

        return True 
 
    if p == 2:
        return True

    if p % 2 == 0 or p % 3 == 0 or p % 5 == 0 or p % 7 == 0 or p % 11 == 0:
        return False

    if (p ** 2 - 1) % 24 != 0:
        return False

    d = p - 1

    # Checking how many times d can be divided by 2
    while d % 2 == 0:
        d >>= 1

    for _ in range(rounds):
        if isComposite(p, d):
            return False

    return True

def getPrimeNBits(nBits: int, algorithm=Algorithm.MILLER_RABIN):
    """Gets a prime with nBits bits of length

    Args:
        nBits: The number of bits desired
        algorthm: The algorithm to check primality
    """

    seed = genSeed(nBits)
    p = randomNBits(nBits, seed)
    i = 0

    if algorithm == Algorithm.MILLER_RABIN:
        while not millerRabin(int(p)):
            p = randomNBits(nBits, p)
            i += 1
        print(f'Numbers tested: {i}')

        return p
    elif algorithm == Algorithm.ANOTHER:
        ...

    #return p
