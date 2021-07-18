from time import process_time

from primes import getPrimeNBits

nBits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

for n in nBits:
    t = process_time()
    p = getPrimeNBits(n)
    print(f'time for {n}: {process_time() - t}')
    print(p)
