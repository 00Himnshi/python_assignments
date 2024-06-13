# Write a python program that generates the first n numbers in the Fibonacci sequence. 
def Fibonacci(n):
    if n==1:
        print("0")
        return 
    print("0,1",end=",")
    n1=0
    n2=1
    c=3
    while(c<=n):
        n3=n2+n1
        print(n3,end=",")
        n1=n2
        n2=n3
        c+=1
    
    

n=int(input("enter the value of n: "))
Fibonacci(n)
