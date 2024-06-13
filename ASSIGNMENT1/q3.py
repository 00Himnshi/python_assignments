#Write a python program that calculates the factorial of a given number. 
def factorial(num):
    if num<0:
        print("ERROR NEGATIVE NUMBER ENTERED")
    if num==0:
        return 1
    return num*factorial(num-1)
n=int(input("enter the number"))
print(factorial(n))