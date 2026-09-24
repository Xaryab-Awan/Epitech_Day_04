msg=input("Enter a message to Decrypt: ").lower()
key=int(input("Enter the size of the key: "))

frequency=[8.12, 1.49, 2.71, 4.32, 12.02, 2.30, 2.03,
        5.92, 7.31, 0.10, 0.69, 3.98, 2.61, 6.95, 7.68, 1.82,
        0.11, 6.02, 6.28, 9.10, 2.88, 1.11, 2.09, 0.17, 2.11, 0.07]
char=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z']
print("Encrypted Text: ",msg)
groups = [""] * key
index = 0
found_key=""
for c in msg:
    if c not in char:
        continue
    groups[index % key] += c
    index += 1
for i in range(len(groups)):
     best_score=-1
     best_shift=0
     for j in range(26):
        decrypted=""
        for k in range(len(groups[i])):
            index=char.index(groups[i][k])
            decrypted+=char[(index-j)%26]
        counts=[0]*26
        for l in range(len(decrypted)):
            index=char.index(decrypted[l])
            counts[index]+=1
        score=0
        for m in range(26):
            actual_pct=(counts[m] / len(groups[i])) * 10
            expected_pct = frequency[m]
            score+= abs(actual_pct - expected_pct)
        if(score<best_score or best_score==-1):
            best_score=score
            best_shift=j

     found_key += char[best_shift]
print("Recovered key:", found_key)
orignal_text=""
shift_index=0
for i in range(len(msg)):
    if msg[i] in char:
        index=char.index(msg[i])
        key_shift=char.index(found_key[shift_index%len(found_key)])
        orignal_text+=char[index-key_shift%26]
        shift_index+=1
    else:
        orignal_text+=msg[i] 
        continue
print("Orignal Text: ",orignal_text)
    
    


