def double(lst):
    newlst=[]
    for i in lst:
        lst1=i*2
        newlst.append(lst1)
    return newlst

alst=double([1,2,3,4,5])
print(alst)


names=['usa','chn','zim']

def upper_name(st):
    return st.upper()

names_upper=map(upper_name,names)
