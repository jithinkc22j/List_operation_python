# Creating an empty list
L=[]
print(L)
# find index value of characters in a list.
l = ["a", "b", "c", 10, 20, 30]
print(l[1])
print(l[0])
print(l[3])

#Replication of list
list1 = ['a', 'b', 'c', 10, 20, 30]
print (4*list1)

#Concatenation of list

list1 = ['a', 'b', 'c', 10, 20, 30]
list2 = ['d', 'e', 'f', 40, 50, 60]

print(list1 + list2)

#List slicing

list1 = ['a', 'b', 'c', 10, 20, 30]

print(list1[0:3])
print(list1[:3])
print(list1[0:])
print(list1[2:5:2])
print(list1[:-3])
print(list1[-1:])
