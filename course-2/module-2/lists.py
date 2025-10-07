list1 = [1,2,3,4,5]
list2 = ['a','b','c']
list3 = ['Hello', 1, True, 40.22]
list4 = [1, [2,3,4],5,6]

print(list1[2])
print(*list1)
print(list1, sep = " ")

list1.insert(len(list1), 6)
print(list1, sep = " ")

list1.append(6)

list1.extent([6,7,8,9])

list1.pop(4)

del list1[2]

for x in list1:
    print('Value: ', x)