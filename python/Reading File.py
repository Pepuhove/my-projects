"""File1=["This is first file \n","This is second file \n"] 
with open("Example1.txt","r")as File1:
    file_stuff=File1.readline()
    print(file_stuff)
    file_stuff=File1.readline() 
    print(file_stuff)   

File1=["This is first file \n","This is second file \n"] 
with open("Example1.txt","w")as File1:
    for line in File1:
"""
exmpl2= "Example2.txt"
with open ("exmpl2.txt","w")as writefile:
    writefile.write("Pepu urisei")