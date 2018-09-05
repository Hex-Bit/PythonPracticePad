my_string = 'Secret agents are super good at staying hidden.'

for item in my_string.split():
    if len(item)%2==0:
        print(item)

mylist=[firstletter[0] for firstletter in my_string.split() ]
print(mylist)


evens=[num for num in range(0,11) if num%2==0]
print(evens)


evens=[num for num in range(0,11,2)]
print(evens)


import random
result=[]
for num in range(0,11):
    result.append(random.randint(0,100))
print(result)