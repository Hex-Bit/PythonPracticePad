my_list=[1,2,3,4,5,6,7,8,9]
for item in my_list:
    print(item)

for item in range(0,10):
    print(item)


evens=[x for x in range(0,21,2)]
print(evens)

s='Something'
for letter in list(enumerate(s)):
    print(list(letter))


# For loops in tuples
tuples=[(1,2),(2,3),(3,4)]
for (item1,item2) in tuples:
    print(item1,item2)

# List zipping 


my_list=[1,2,3,4,5,6,7,8,9]
my_list2=[1,2,3,4,5,6,7,8,9]
for item in zip(my_list,my_list2):
    print(item)
