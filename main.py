from time import process_time

from primes import getPrimeNBits

nBits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

total = 0

for n in nBits:
    t = process_time()

    p = getPrimeNBits(n)

    elapsed = process_time() - t
    total += elapsed
    print(f'time for {n}: {elapsed}')
    print(p)
    print()

print(f'Total time: {total:.4}s')
