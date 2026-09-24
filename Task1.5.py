num=input("Enter an Integer: ")
num=int(num)
found=False
if num==42:
    print("a",end="")
    found=True
if num<=21:
    print("b",end="")
    found=True
if num%2==0:
    print("c",end="")
    found=True
if num/2<21:
    print("d",end="")
    found=True
if num%2!=0 and num>=45:
    print("e",end="")
    found=True
if found==False:
    print("f")

