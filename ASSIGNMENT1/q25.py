#Write a program that copies the contents of one text file to another. 
f=open("content.txt","r")
newf=open("main.txt","w")
content=f.read()
newf.write(content)
newf.close()
f.close()