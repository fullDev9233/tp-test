import numpy as np
import sympy as sp
import random

primes = []
def get_primes(count):
    i = 3
    len = 0
    primes.append(2)
    while len < count:
        if(sp.isprime(i)):
            primes.append(i)
            len += 1
        i += 2

def get_3d_prime():
    rand_idx = random.sample(range(0, 1000), 1000)
    rand_primes = []
    for i in range(len(rand_idx)):
        rand_primes.append(primes[rand_idx[i]])
    result = np.array(rand_primes)
    return result.reshape([10,10,10])

get_primes(1000)
print(get_3d_prime())






