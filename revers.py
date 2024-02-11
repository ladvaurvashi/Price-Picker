s = input("Enter the string: ")
word=""
s2= ""
for i in range(len(s)):
    if (s[i]==" "):
        s2 = s2+word[::-1]+" "
        word=""
    elif (i == len(s)-1):
        word = word+s[i]
        s2 = s2+word[::-1]
    else:
        word = word+s[i]

print(s2)