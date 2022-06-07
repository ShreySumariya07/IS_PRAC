import hashlib
def KeyGeneration():
  p = 5
  q = 11
  n = p*q
  z = (p-1)*(q-1)

  e = 2
  while e<=z and math.gcd(e,z) != 1:
    e+=1
  
  d=1
  while (e*d)%z != 1:
    d+=1
  
  return (n,e,d)

def primitiveRoot(p):
  q = 0
  li = []
  for i in range(2,p):
    for j in range(1,p):
      if (i**j)%p in li:
        pass
      else:
        q = i
      li.append((i**j)%p)
  return q

def encryption(plain):
  key = KeyGeneration()
  e = key[1]
  n = key[0]
  cipher = ""
  for i in range(len(plain)):
    if plain[i] == "":
      cipher += "#"
    else:
      cipher += chr((ord(plain[i])**e)%n)
  return cipher

def decryption(cipher):
  key = KeyGeneration()
  d = key[2]
  n = key[0]
  plain = ""
  for i in range(len(cipher)):
    if cipher[i] == "#":
      plain += " "
    else:
      plain += chr((ord(cipher[i])**d)%n)
  return plain

def sender(message):
  result = hashlib.md5(message.encode())
  digest1 = result.hexdigest()
  signature = encryption(digest1)
  return signature

def receiver(message,signature):
  result = hashlib.md5(message.encode())
  digest2 = result.hexdigest()
  digest1 = decryption(signature)
  return (digest2,digest1)

message = "Hello my name is Shrey"
signature = sender(message)
receiverData = receiver(message,signature)
md2 = receiverData[0]
md1 = receiverData[1]

if md2 == md1:
  print("Integrity check successfully")
else:
  print("Integrity check unsuccessful")