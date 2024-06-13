#Write a program that takes a string input from the user and writes it to a text file.
f=open("string.txt","w")
s=input("enter a string ")
f.write(s)
f.close()
