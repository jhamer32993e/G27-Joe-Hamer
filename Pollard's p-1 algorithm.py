import random


def euclid(a1, b):
    r = a1 % b
    mya = b
    myb = r
    while myb > 0:
        r = mya % myb
        mya = myb
        myb = r
    return mya
# Euclid's algorithm to avoid importing math for gcd function

n = open('PrimeList.csv', 'r')
# File of primes up to 10^7
Lines = n.readlines()
# Choose 2 random primes for factorisation
p1 = int(Lines[random.randint(1, len(Lines))])
p2 = int(Lines[random.randint(1, len(Lines))])
print("Chosen primes:", p1, p2)
# Find product of the primes
n = p1 * p2
# Set initial values of a, i, d
a = 2
i = 2
d = 1
while d == 1:
    a = (a**i) % n
    d = euclid(a-1, n)
    # My implementation of Euclid's Algorithm as defined above, instead of math.gcd()
    i += 1
    print("Iteration:", i-2)
    print("d =", d)
print("First factor is", d)
print("Second factor is", int(n/d))
# Chose to output for each iteration as initially I had primes up to 10^8, which ended up being too big to upload
# and outputting each step made sure i knew the code was indeed running as it sometimes took upwards of 5 minutes.
