def encryptText(plain_text,column):
  inter_text = []
  cipher = ""
  i = 0
  while i < len(plain_text):
    fragment = list(plain_text[i:column+i])
    while len(fragment) < column:
      fragment.append(" ")

    inter_text.append(fragment)
    i = i + column
  for i in range(0,column):
    for j in range(0,len(inter_text)):
      if inter_text[j][i] == " ":
        cipher += "#"
      else:
        cipher += inter_text[j][i]
      
  return cipher

def decryptText(encrypt_text,column):
  inter_text = []
  plain = ""
  i = 0
  rows = int(len(encrypt_text)/column)
  while i < len(encrypt_text):
    fragment = list(encrypt_text[i:i+rows])
    i = i + rows
    inter_text.append(fragment)
  for i in range(0,rows):
    for j in range(0,column):
        if inter_text[j][i] == "#":
          plain += " "
        else:
          plain += inter_text[j][i]
  return plain

def main():
  while True:
    option = int(input("Enter an option:"))
    if option == 1:
      plain_text = input("Enter a plain_text")
      column = int(input("Enter a key"))
      encrypted_text = encryptText(plain_text,column)
      print("The encrypted text is {}".format(encrypted_text))
    elif option == 2:
      encrypt_text = input("Enter a encrypted")
      column = int(input("Enter a key"))
      decrypted_text = decryptText(encrypt_text,column)
      print("The encrypted text is {}".format(decrypted_text))
    else:
      print("Thank you")
      break

main()