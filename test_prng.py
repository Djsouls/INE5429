from time import process_time

from random_ import genSeed, xorshift, bbs

b = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

print('Xorshift:')
for nBits in b:
    s = genSeed(nBits)
   
    t = process_time()
    xorshift(nBits, s)
    print(f'time for {nBits}: {process_time() - t}')

print('Blum-Blum-Shub:')
for nBits in b:
    s = genSeed(nBits)
   
    t = process_time()
    bbs(nBits, s)
    print(f'time for {nBits}: {process_time() - t}')
