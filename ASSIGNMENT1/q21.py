#Write a python program that counts the occurrences of a specific element in a list. 
n=int(input("enter element to search for: "))
ans=0
l=[1,2,3,3,6,7,8,3,9,9,0,1,2,8,5,3,4]
for i in l:
    if i==n:
        ans+=1
print("ans: ",ans)