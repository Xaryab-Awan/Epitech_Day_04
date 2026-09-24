msg=input("Enter a message: ").lower()
key=input("Enter the key: ").lower()
char=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z']
print("Orignal Text: ",msg)
cipher:str=""
index:int=-1
shift=-1
key_index:int=0
for i in range(len(msg)):
    if msg[i] not in char:
        cipher += msg[i]
        continue
    index = char.index(msg[i])
    shift = char.index(key[key_index % len(key)])
    cipher += char[(index + shift) % 26]
    key_index += 1

print("Ciphered Text: ",cipher)
        