a = input()
b = ord(a)
if b == 122:
    b = 97
else:
    b += 1
a = chr(b)
print(a)
