nested1=[['a','b','c'],['d','e'],['f','g']]
y=nested1
nested1[2].append('h')
print(y)
print(nested1)
print(len(y and nested1))
if len(y[0]) == len(y[2]):
    print(True)
else:
    print(False)

print([10,20,30][1])



info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }

# Access the color information
color = info['personal_data']['physical_features']['color']
social_media=info['other']['interested_in']
# Print the color information
print(color)
print(social_media)

info = [['Tina', 'Turner', 1939, 'singer'], 
        ['Matt', 'Damon', 1970, 'actor'], 
        ['Kristen', 'Wiig', 1973, 'comedian'], 
        ['Michael', 'Phelps', 1985, 'swimmer'], 
        ['Barack', 'Obama', 1961, 'president']]

last_names = []
for i in info:
    last_names.append(i[1])

print(last_names)


L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], 
     ['carrots', 'peas', 'cucumbers', 'green beans'], 
     ['root beer', 'smoothies', 'cranberry juice']]

b_strings = []

for sublist in L:
    for item in sublist:
        if 'b' in item:
            b_strings.append(item)

print(b_strings)

