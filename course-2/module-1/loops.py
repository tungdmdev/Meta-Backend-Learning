favorites = ['Creme Brulee', ' Apple Pie', 'Churros', 'Tiramisu', 'Chocolate Cake']

for idx, item in enumerate(favorites):
    print(idx, item)

count = 0

while  count < len(favorites ):
    print(' I like this desert', favorites[count])
    count += 1

# For loop
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    print('One of my favorite desserts is', dessert)

# While loop
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

count = 0

while count < len(favorites):
    print('One of my favorite desserts is', favorites[count]);
    count += 1

#If else
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        print('Yes, one of my favorite desserts is', dessert)
        break
else:  # This else belongs to the for loop, not the if statement
    print('No sorry, not a dessert on my list')

# Continue
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        continue
    print('Other desserts I like are', dessert) 

# Pass
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert)    