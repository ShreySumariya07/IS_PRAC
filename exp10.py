
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
    
p = int(input("Enter any number"))
print(primitiveRoot(p))