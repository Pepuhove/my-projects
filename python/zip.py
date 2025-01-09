L1=[1,2,3]
L2=[4,5,6]
L3=[]
for i in range(len(L1)):
    L3.append(L1[i]+L2[i])
print(L3)

L1=[1,2,3]
L2=[4,5,6]

L3=list(zip(L1,L2))
print(L3)

L1=[1,2,3]
L2=[4,5,6]

L3=[x1+x2 for (x1,x2) in list(zip(L1, L2))]
print(L3)

L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = map(lambda x: x[0] + x[1], zip(L1, L2))
print(list(L3))

L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3 = [x1 + x2 for x1, x2 in zip(L1, L2) if x1 > 10 and x2 < 5]
