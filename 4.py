import random
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gen_prime():
    while True:
        n = random.randrange(1, 100)
        if is_prime(n):
            return n

def gcd(phi):
    while True:
        e = gen_prime()
        gcd=math.gcd(e, phi)
        if gcd == 1:
            return e

def gcd_for_d(e, phi):
    while True:
        d = gen_prime()
        de=d*e
        gcd=math.gcd(de,phi)
        if gcd == 1:
            return d

p = gen_prime()
q = gen_prime()
print("Two prime numbers:", p, q)
n = p * q
print("Product of the above prime numbers is:", n)
phi = (p - 1) * (q - 1)
print("Phi Value:", phi)
e = gcd(phi)
print("Public Key:", e)
m = int(input("Enter the Message: "))
c = (m ** e) % n
print("Cipher Text is:", c)
d = gcd_for_d(e, phi)
print("Private Key:", d)


