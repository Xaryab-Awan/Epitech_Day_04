print("Enter a number then a string:")
num:int=input()
str=input()
if num ==0:
    exit()
elif 'a' in str or 'e' in str or 'i' in str or 'o' in str or 'u' in str:
    print(num)
elif num>=42:
    print(num)
else:
    print(str)