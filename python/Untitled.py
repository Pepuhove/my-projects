"""sentence = ("I am busy studying coputer science hopefully soon I will be a developer")
count = 0
for _ in sentence:
    print(sentence[::-1])
    print(len(sentence))
    print(sentence.count("developer"))
    count+=1
    break
    
for name in ["pepu","sande","wiz"]:
    print(name.count("e"))
    
for idx in range (5):
    square = idx * idx
    print(square)
    
for name in ["Wiz","Yvo","Masi","Pepu","Thavo"]:
    print("Hi", name, "you are cordially invited to the party on Saturday!")
    
nums = [1,2,3,4,5,6,7,8,9]
sum = 0
for i in nums:
    sum = sum + i
print(sum)
#this is the same method of getting the sum
sum = 0
for i in range (10):
    sum+=i
print(sum)

#counting the number of items in a list
nums = [1,2,3,4,5,6,7,8,9,10]
count = 0
for i in nums:
    count+=1
print(count)

word = ("HAPPY")
for i in reversed(word):
    print(i)
    """
    

"""
cities = [
    {"city": "Paris", "country": "France"},

    {"city": "Berlin", "country": "Germany"},

    {"city": "Geneva", "country": "Switzerland"},

    {"city": "Nice", "country": "France"},

    {"city": "Rome", "country": "Italy"},

    {"city": "Dubai", "country": "UAE"},

    {"city": "Bangkok", "country": "Thailand"},

    {"city": "Phuket", "country": "Thailand"},

    {"city": "Tokyo", "country": "Japan"},
    ]
    
count=0
count2=0
for city,country in cities:
    count+=1
    count2+=1
    
print(f"I am going to visit {count} cities in {count2} countries.")
        
my_string = "this is a test string this is only a test"
word_counts = {}

for word in my_string.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

most_frequent_word = max(word_counts, key=word_counts.get)
print(most_frequent_word) """

#counting characters excluding a space " "
words = "why are you so slow when you are walking?"
total=0
for i in words:
    if i !=" ":
        total+=1
print(total)

#counting characters excluding "a"
story = "I came to SA some many years ago"
total=0
for i in story:
    if i !="a":
        total+=1
print(total)

#counting number of vowels
phrase = "what if we plan to go out next year"
count=0
for i in phrase:
    if i in ["a","e","i","o","u"]:
        count+=1
print(f"There are actually {count} vowels in the phrase")


# counting the number of "o":
s="zoology"
o_count=0
for i in s:
    if i=="o":
        o_count+=1
print(f"There are {o_count} 'o' in zoology")


#finding the maximum value
nums=[2,4,9,20,200,200,0,1]
max_num=nums[0]
count=0
for i in nums:
    if i > max_num:
        max_num=i 
        
print(count)    
print(f"The maximum number is {max_num}")


#finding the minimum or lowest number
nums=[2000,82,1990,78,2,5]
min_num=nums[0]
for i in nums:
    if i<min_num:
        min_num=i
print(f"The minimum number is {min_num}.")

