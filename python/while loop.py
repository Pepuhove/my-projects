"""def sumTo(aBound):
    theSum=0
    aNumber=1
    while aNumber <= aBound:
        theSum+=aNumber
        aNumber+=1
    return theSum
print(sumTo(4))
print(sumTo(1000))

def even_num(num):
    even_nums=[]
    for n in range(num):
        if n%2==0:
            even_nums.append(n)
    return even_nums
a=list(even_num(15))
print(a)


count=0
even_nums=[]
while count <= 15:
    if count % 2 ==0:
        even_nums.append(count)
        count+=1"""
trial = 0
name = input('Enter your name: ')

while name.strip() == "" or name.isdigit():
    print('You did not put your name!')
    name = input('Enter your name: ')
    trial += 1
    if trial == 3:
        import time
        for seconds in range(10, 0, -1):
            print(f'You have {seconds} seconds left.')
            time.sleep(1)
        trial = 0

if trial < 3:
    trial += 1
    print(f'Hello {name}, you made it in {trial} trial(s).')
    print('That\'s awesome!')
