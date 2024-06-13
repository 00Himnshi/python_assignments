#Write a python program that checks if a substring is present in a given string.
S=input("enter the string")
sub=input("enter substring to look for")
ans=S.find(sub)
if ans!=-1:
    print("Yes it is the substring")
else:
    print("No")