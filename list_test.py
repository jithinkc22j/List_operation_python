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
# Sort and reverse  functions
L1 = [1, 7, 2, 3]
L1.sort()
print(L1)
L1.reverse()
print(L1)

#Built in list functions
L1 = ["a", "b", "c", 1, 2, 3]
L2 = [4, 5, 6]
L1.append(7)
print(L1)
L1.remove(3)
print(L1)
L1.extend(L2)
print(L1)
L1.pop(0)
print(L1)
print(L1[1])
L1.insert(3, 8)
print(L1)

#Membership Operators in a List

L = ["a", "b", "c", 1, 2, 3]
print(2 in L)
print("a" not in L)
print(4 not in L)
print("d" in L)
