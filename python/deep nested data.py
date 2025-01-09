'''import copy
info=[['Yvonne','Sande',5],['Pepu','Hove',4],['wiz','Wisdom',6]]
last_names=[]
for i in info:
   last_names.append(i[1])
   print(last_names)
a=info[:]
#print(a)
deep_copied_version=copy.deepcopy(info)
print(deep_copied_version)'''

a=[[[1,2],[2,3],[3,4],[1,9]]]
dict1={}
for i in a:
    for x in i:
        for y in x:
            if y in dict1:
                dict1[y]+=1
            else:
                dict1[y]=1
print(dict1)


l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]
third=[]

for sublist in l_of_l:
    if len(sublist) >= 3:  # Make sure the sublist has at least three elements
        third.append(sublist[2])

print(third)
