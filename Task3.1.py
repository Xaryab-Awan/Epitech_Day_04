msg=input("Enter a message: ")
key=int(input("Enter the key: "))
char=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z']
print("Orignal Text: ",msg)
cipher:str=""
index:int=-1
for i in range(len(msg)):
    index=-1
    for j in range(len(char)):
        if msg[i]==char[j]:
            index=j
    if msg[i]==" " or msg[i]==".":
        cipher+=msg[i]
        continue
    else:
        cipher+=char[(index+key)%26]

print("Ciphered Text: ",cipher)
        