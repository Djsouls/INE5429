from enum import Enum, auto
from random import getrandbits

from fixedint import FixedInt

class PRNGAlgorithm(Enum):
    XORSHIFT = auto()
    ANOTHER = auto()

# Sometimes the number returned by getrandbits()
# doesn't have exactly the number of bits requested,
# this function exits to assure that it will.
def genSeed(nBits: int) -> int:
    s = getrandbits(nBits)

    while s.bit_length() != nBits:
        s = getrandbits(nBits)

    return FixedInt(nBits, signed=False, mutable=True)(s)

def xorshift(nBits: int, s: FixedInt) -> int:
    while int(s).bit_length() != nBits:
        s ^= (s << 13)
        s ^= (s >> 7)
        s ^= (s << 17)

    return int(s)

def another():
    ...

def randomNBits(nBits: int, alg=PRNGAlgorithm.XORSHIFT):
    if alg == PRNGAlgorithm.XORSHIFT:
        seed = genSeed(nBits)

        return xorshift(nBits, seed)
    elif alg == Algorithm.ANOTHER:
        another()
