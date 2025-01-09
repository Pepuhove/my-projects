"""names= ("joe","pepu","wiz")
for name in ["joe","pepu","wiz"]:
    print(f"Hi {name} please come to my party!")
print("See you there guys!")

for achar in "Go spot go":
    print(achar)
    
s=("python rocks")
count=0
for ch in s:
    print("HELLO")
    count+=1
print("There are" ,count,"letters.")

import turtle
wn= turtle.Screen()
pepu=turtle.Turtle()

for i in range(6):
    pepu.forward(50)
    pepu.left(90)
    pepu.left(45)
wn.exitonclick()

names = ("pepu","ave","gerie")
count = 0
for name in ["pepu","ave","gerie"]:
    print(name.count("e"))
    count+=1
    """
"""
accum=0
for i in range(11):
    accum+=i
print(accum)
print(max(range(11)))

nums=[0,1,2,3,4,5,6,7,8,9,10]
count=0
for i in nums:
    count+=1
print(count)


str=(" i like to work.")
count=0
for numbs in str:
    count+=1
print(count)

nums=list(range(41))
print(nums)
sum=0
for i in nums:
    sum+=i
print(sum)
 
fruits=["apple","banana","orange","lemon","orange"] 
for i in range (5):
    print(i,fruits[i]) 

nums=[1,2,3,"hi","hey"]
for i in nums:
    print(i)
    
for i in nums:
    print(type(i))
 
 
word=["hey","hello","words"]
for i in word:
    print(i,len(i))
    
    
nums = "3.0,4.0,2.0,1.0,5.0"
above = 0
num_list = nums.split(',')  # Split the string into a list of numbers

for num in num_list:
    if float(num) > 3.0:  # Convert the string to a float and compare
        above += 1

print(above)



#finding the average of nummbers in a list==sum(nums)//len(nums)
nums= [2,4,1,5,6,8]
count=0
avg=sum(nums)
for i in nums:
    count+=1
    avg=sum(nums)//count
print(avg)


a=["a","b","c"]
z=a
a[1]="i"
z.remove("i")
print(z)

#ACCUMMMULATOR Pattern with lists
nums = [3,5,8]
accum = []
for i in nums:
    b = i**2
    accum.append(b)
print(accum)


a=("")
for i in range(36):
    print("b")
    """
a="hie how are you"
b=a.split()
c=[]
for i in b:
    c=i[0].upper
    
print(c)
    
    
