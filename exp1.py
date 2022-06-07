def encryptText(plain_text,key):
  cipher = ""
  for i in range(len(plain_text)):
    if plain_text[i].islower():
      cipher += chr((ord( plain_text[i] ) + key - 97) % 26 + 97)
    elif plain_text[i].isupper():
      cipher += chr((ord( plain_text[i] ) + key - 65 ) % 26 + 65)
    elif plain_text[i].isnumeric(): 
      cipher += str(int(plain_text[i]) + key)
    else:
      cipher += "#"
  return cipher

def decryptText(cipher,key):
  plain = ""
  for i in range(len(cipher)):
    if cipher[i].islower():
      plain +=  chr((ord(cipher[i]) - key - 97 ) % 26 + 97 )  
    elif cipher[i].isupper():
      plain += chr((ord( cipher[i] ) - key - 65 ) % 26 + 65)
    elif cipher[i].isnumeric(): 
      plain += str(int(cipher[i]) - key)
    else:
      plain += " "
  
  return plain

def main():
  while True:
    option = int(input("Enter an option:"))
    if option == 1:
      plain_text = input("Enter a plain_text")
      key = int(input("Enter a key"))
      encrypted_text = encryptText(plain_text,key)
      print("The encrypted text is {}".format(encrypted_text))
      break
    elif option == 2:
      encrypt_text = input("Enter a plain_text")
      key = int(input("Enter a key"))
      decrypted_text = decryptText(encrypt_text,key)
      print("The encrypted text is {}".format(decrypted_text))
      break
    else:
      print("Thank you")
      break

main()
