total = [num**2 for num in range(10)]
print(total)

names = ["pepu","masi","lily"]
grades = [80, 90, 100]

for name, grade in zip(names, grades):
    print("{name} : {grade}".format)