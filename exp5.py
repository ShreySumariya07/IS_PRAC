import random,math
def primitiveRoot(p):
  alpha = 0
  li = []
  for i in range(2,p):
    for j in range(1,p):
      if (i**j)%p in li:
        pass
      else:
        alpha = j
      li.append((i**j)%p)
  return alpha

p = int(input("Enter a prime number:\n"))
alpha = primitiveRoot(p)

xa = random.randint(2,p)
xb = random.randint(2,p)

ka = (alpha**xa)%p
kb = (alpha**xb)%p

k1 = (kb**xa)%p
k2 = (ka**xb)%p

print("Alice private key:{}".format(xa))
print("Bob private key:{}".format(xb))
print("Alice public key:{}".format(ka))
print("Bob private key:{}".format(kb))
print("Alice secret key:{}".format(k1))
print("Bob secret key:{}".format(k2))