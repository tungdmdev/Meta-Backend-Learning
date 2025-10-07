list1 = [1,2,3,4,5,6,7,8,9]
list2 = [1,2,3,4,5,6,7,8,9]

count = 0
#outer loop
for x in list1:
    count += 1
    #inner loop
    for y in list2:
        count += 1

print(count)


import time
start_time = time.time()

for i in range(1):
    for j in range(100):
        print(0, end = " ")
    print()

print(round((time.time() - start_time), 2))


num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

count = 0

for x,num in enumerate(num_list):
    count += 1
    if num == 36:
        print('Number found at ', x)
        break

print(count)