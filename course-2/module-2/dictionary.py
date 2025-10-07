my_d = {1: 'Test', 'Name': 'Jimmy'}

my_d[2] = 'Test 2'

my_d[1] = 'Not a test!'
print(my_d)

for key, value in my_d.items():
    print(str(key) + " : " + value)