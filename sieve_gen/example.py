import sieve

for n, i in zip(range(6), sieve.sieve()):
    print i
