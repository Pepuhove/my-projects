# Which number do you want to check?
n= int(input('enter a number: '))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
def num_check(number):
 
  if number%2==0:
    print('This is an even number.')
  else:
    print('This is an odd number.')
num_check(number=n)