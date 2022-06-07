import math
def KeyGeneration(p,q):
  n = p*q
  z = (p-1)*(q-1)
  e = 2
  while e<=z and math.gcd(e,z)!= 1:
    e += 1
  d = 2
  while (d*e)%z != 1:
    d += 1
  return (e,d,n)
def EncryptText(plain,p,q):
  key = KeyGeneration(p,q)
  e = key[0]
  n = key[2]
  cipher = (plain**e)%n
  return cipher

def DecryptText(cipher,p,q):
  key = KeyGeneration(p,q)
  d = key[1]
  n = key[2]
  plain = (cipher**d)%n
  return plain

plain = 23
p = 5
q = 11
enc = EncryptText(plain,p,q)
dec = DecryptText(enc,p,q)
print(enc)
print(dec)