

abbrevs = ['usa', 'chn', 'zim']

def f(st):
    return st.upper()

#names_upper = list(map(f, abbrevs))
names_upper=list(map(lambda st: st.upper(), abbrevs))
print(names_upper)


