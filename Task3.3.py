msg=input("Enter a message: ")
key=input("Enter the key: ")
char=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z']
print("Orignal Text: ",msg)
cipher:str=""
index:int=-1
shift=-1
key_index:int=0
for i in range(len(msg)):
    for j in range(len(char)):
        if msg[i]==char[j]:
            index=j
    for k in range(len(char)):
        if key[key_index%len(key)]==char[k]:
            shift=k+1
    if msg[i]==" " or msg[i]==".":
        cipher+=msg[i]
        continue
    else:
        cipher+=char[(index+shift)%26]
        key_index+=1

print("Ciphered Text: ",cipher)
        