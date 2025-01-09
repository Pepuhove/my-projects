
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
a=sent.split(' ')
acro=[]

for i in a:
    if i not in  stopwords:
        acro.append(i[:2].upper())
acro='. '.join(acro)

print(acro)


p_phrase = "was it a car or a cat I saw"
r_phrase=p_phrase[::-1]
print(r_phrase)

#frist forty chararcters in file emotion_words
"""f=open('emotion_words2.txt','r')
file=f.read()
first_forty=file[:40]
print(first_forty)"""


stri = "what can I do"

char_d={}
for i in stri:
    if i not in char_d:
        char_d[i]=1
    else:
        char_d[i]+=1
print(char_d)

product = "iphone and android phones"
lett_d = {}

# Count the occurrences of each character
for i in product:
    if i not in lett_d:
        lett_d[i] = 1
    else:
        lett_d[i] += 1

# Find the key with the highest value
max_value = max(lett_d, key=lett_d.get)

print(max_value)


def total(lst):
    sum=0
    for i in lst:
        sum+=i
    return sum
sum=total([1,2,3,4,5])
print(sum)


def addit(number):
    return number + 5

def mult(number):
    return number * addit(number)
result_addit = addit(10)  # This will return 15 (10 + 5)
result_mult = mult(10)   # This will return 150 (10 * (10 + 5))


def info(name, age, birth_year,year_in_college,hometown):
    return name, age, birth_year,year_in_college,hometown
result=info('Pepu',29,1994,2014,'Harare')
print(result)


def sublist(input_list):
    result = []
    i = 0
    while i < len(input_list) and input_list[i] != "STOP":
        result.append(input_list[i])
        i += 1
    return result



winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']

#winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']

# Define a function to extract the first name for sorting
def sort_by_first_name(full_name):
    return full_name.split()[0]

# Sort the list by first name
winners = sorted(winners, key=sort_by_first_name)

# Print the sorted list
print(winners)


lst = [3, 5, 1, 6, 7, 2, 9, -2, 5]
lst_sorted=sorted(lst,reverse=True)
print(lst_sorted)


medals = {'Japan': 41, 'Russia': 56, 'South Korea': 21, 'United States': 121, 'Germany': 42, 'China': 70}
top_three = sorted(medals, key=lambda x: medals[x], reverse=True)[:3]
print(top_three)
