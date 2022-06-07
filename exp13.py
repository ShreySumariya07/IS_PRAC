import math


def changeCharPositionToRight(inter_text, digit):
    some_text = []
    i = digit - 1
    while i < len(inter_text):
        some_text.append(inter_text[i])
        i = i + digit
    last = some_text[len(some_text)-1]
    i = len(some_text)-1
    while len(some_text) > 1 and i > 0:
        some_text[i] = some_text[i-1]
        i = i - 1
    some_text[i] = last
    i = digit - 1
    k = 0
    while i < len(inter_text):
        inter_text[i] = some_text[k]
        i = i + digit
        k = k + 1
    return inter_text


def changeCharPositionToLeft(inter_text, digit):
    some_text = []
    i = digit - 1
    while i < len(inter_text):
        some_text.append(inter_text[i])
        i = i + digit
    first = some_text[0]
    i = 1
    while len(some_text) > 1 and i < len(some_text):
        some_text[i-1] = some_text[i]
        i = i+1
    some_text[len(some_text)-1] = first
    i = digit - 1
    k = 0
    while i < len(inter_text):
        inter_text[i] = some_text[k]
        i = i + digit
        k = k + 1
    return inter_text


def encryptText(plain_text, key):
    inter_text = [x for x in plain_text]
    ceaser_text = ""
    for i in range(0, len(inter_text)):
        if inter_text[i] == " ":
            inter_text[i] = "#"
    value = 0
    key_length = 0
    while key > 0:
        digit = int(key % 10)
        if digit == 0:
            break
        value += digit
        key_length += 1
        inter_text = changeCharPositionToRight(inter_text, digit)
        key = key / 10
    for x in inter_text:
        ceaser_text += x
    encrypt_text = ""
    matrix = []
    col = int(value / key_length)
    i = 0
    while i < len(ceaser_text):
        fragment = list(ceaser_text[i:i+col])
        while len(fragment) < col:
            fragment.append("#")
        matrix.append(fragment)
        i = i + col
    a = 0
    b = 0
    c = len(matrix) - 1
    d = col - 1
    while a <= c and b <= d:
        for i in range(a, c+1):
            encrypt_text += matrix[i][b]
        b = b + 1
        for i in range(b, d+1):
            encrypt_text += matrix[c][i]
        c = c - 1
        if a != c:
            for i in range(c, a-1, -1):
                encrypt_text += matrix[i][d]
        d = d - 1
        for i in range(d, b-1, -1):
            encrypt_text += matrix[a][i]
        a = a + 1
    return encrypt_text


def decryptText(ceaser_text, key):

    plain_text = ""
    newKey = int(0)
    value = 0
    key_length = 0
    while key > 0:
        digit = int(key % 10)
        if digit == 0:
            break
        value += digit
        key_length += 1
        newKey = (newKey * 10)+digit
        key = key / 10
    col = int(value / key_length)
    rows = int(len(ceaser_text) / col)

    matrix = []
    i = 0
    while i < len(ceaser_text):
        fragment = []
        while len(fragment) < col:
            fragment.append("#")
        matrix.append(fragment)
        i = i + col
    j = 0
    a, b, c, d = 0, 0, rows-1, col-1
    while a <= c and b <= d:
        for i in range(a, c+1):
            matrix[i][b] = ceaser_text[j]
            j += 1
        b = b + 1
        for i in range(b, d+1):
            matrix[c][i] = ceaser_text[j]
            j += 1
        c = c - 1
        if a != c:
            for i in range(c, a-1, -1):
                matrix[i][d] = ceaser_text[j]
                j = j + 1
        d = d - 1
        for i in range(d, b-1, -1):
            matrix[a][i] = ceaser_text[j]
            j = j + 1
        a = a + 1
    new_text = ""
    for i in range(rows):
        for j in range(col):
            new_text += matrix[i][j]
    if new_text[len(new_text)-1] == "#":
        new_text = new_text[:len(new_text)-1]
    inter_text = [x for x in new_text]
    while newKey > 0:
        digit = int(newKey % 10)
        if digit == 0:
            break
        inter_text = changeCharPositionToLeft(inter_text, digit)
        newKey = newKey / 10
    for x in inter_text:
        if x == "#":
            plain_text += " "
        else:
            plain_text += x
    return plain_text


def main():
    while True:
        option = int(
            input("Enter the option number \n1.Encryption\n2.Decryption\n3.Exit\n"))
        if option == 1:
            plain_text = input("Enter the plain text:\n")
            key = int(input("Enter a valid key\n"))
            ceaser_text = encryptText(plain_text, key)
            print("The encrypted text is"+ceaser_text)
        elif option == 2:
            ceaser_text = input("Enter the encrypted text:\n")
            key = int(input("Enter a valid key\n"))
            plain_text = decryptText(ceaser_text, key)
            print("The decrypted text is\n"+plain_text)
        elif option == 3:
            break


main()
