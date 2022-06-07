import math
def KeyGeneration(p,q,r):
  n = p*q*r
  z = (p-1)*(q-1)*(r-1)
  e = 2
  while e<=z and math.gcd(e,z)!= 1:
    e += 1
  d = 2
  while (d*e)%z != 1:
    d += 1
  return (e,d,n)
def EncryptText(plain,p,q,r):
  key = KeyGeneration(p,q,r)
  e = key[0]
  n = key[2]
  cipher = (plain**e)%n
  return cipher

def DecryptText(cipher,p,q,r):
  key = KeyGeneration(p,q,r)
  d = key[1]
  n = key[2]
  plain = (cipher**d)%n
  return plain

plain = 23
p = 5
q = 7
r = 11
enc = EncryptText(plain,p,q,r)
dec = DecryptText(enc,p,q,r)
print(enc)
print(dec)