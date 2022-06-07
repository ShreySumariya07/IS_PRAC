import hashlib

def encryption(plain,key):
  cipher = ''

  for i in range(len(plain)):
    if plain[i].isupper():
      cipher += chr((ord(plain[i])+key -65) % 26 + 65)
    elif plain[i].islower():
      cipher += chr((ord(plain[i])+key -97) % 26 + 97)
    else:
      cipher += '#'

  return cipher

def sender(cipher):
  result = hashlib.md5(cipher.encode())
  digest = result.hexdigest()
  return digest

def receiver(cipher):
  result = hashlib.md5(cipher.encode())
  digest = result.hexdigest()
  return digest


plain = "Hello my name is Shrey"
key = 4
cipher = encryption(plain,key)
digest1 = sender(cipher)
digest2 = receiver(cipher)

print(digest1)
print(digest2)
print(digest1 == digest2)