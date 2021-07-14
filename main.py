from random_ import randomNBits
from primes import getPrimeNBits, millerRabin

nBits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

for n in nBits:
    print(f'{n}: {getPrimeNBits(n)}')
