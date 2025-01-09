def keep_evens(nums):
    evens=filter(lambda num:num%2==0, nums)
    return list(evens)
print(keep_evens([1,2,3,4,5,6,7]))



lst=['witch','halloween','pumpkin','cat','candy','wagon','moon','soon']

def oo(words):
    lst2=filter(lambda words: 'o'in words, lst)
    return list(lst2)
print(oo(lst))

lst=['witch','halloween','pumpkin','cat','candy','wagon','moon','soon']

lst2=filter(lambda word: 'o' in word, lst)
print(list(lst2))