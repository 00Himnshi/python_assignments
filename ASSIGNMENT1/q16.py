#Write a program in python that counts the frequency of each character in a string.
def c(s):
    set_char=set()
    for char in s:
        set_char.add(char)
    for c in set_char:
        n=s.count(c)
        print(c,": ",n)
s=input("enter a string ")
c(s)