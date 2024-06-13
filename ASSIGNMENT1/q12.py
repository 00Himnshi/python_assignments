# Write a python program that calculates the sum of the digits of a given number.
def sum_of_digits(num):

    if num//10==0:
        return num
    return num%10+sum_of_digits(num//10)

num=int(input("enter a number"))
print(sum_of_digits(num))