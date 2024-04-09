import random
import math

n = open('PrimeList.csv', 'r')
# File of primes up to 10^7
Lines = n.readlines()
# Choose 2 random primes for factorisation
p1 = int(Lines[random.randint(1, len(Lines))])
p2 = int(Lines[random.randint(1, len(Lines))])
print("Chosen primes:", p1, p2)
# Find product of the primes
n = p1 * p2
# Choose initial value of a, want to find a, b s.t. n=a^2-b^2=(a+b)(a-b)=pq
a = math.ceil(n**0.5)
# Find b
b = (a**2 - n)**0.5
steps = 1
print("Current a=", a)
print("Current b=", b)
# Is b an integer? If no, increase a by 1 and repeat
while b % 1 != 0:
    a += 1
    b = (a**2 - n)**0.5
    steps += 1
    print("Current a=", a)
    print("Current b=", b)
# Calculate p, q from a and b
p = a + b
q = a - b
print("Found primes:", int(p), int(q))
print("Initial primes:", p1, p2)
# printing initial primes again as if the chosen primes are large enough there is too
# much output to see the first print
print(steps, "iterations")
# Chose to output for each iteration as initially I had primes up to 10^8, which ended up being too big to upload
# and outputting each step made sure i knew the code was indeed running as it sometimes took upwards of 5 minutes.
