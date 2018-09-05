x=int(input('Enter Your mark : '))
if x<=100:
    if x > 79:
        print('You got A+ that is Outstanding !!')
    elif x > 74:
        print('You got A that is Excellent !!')
    elif x > 69:
        print('You got A- that is Very Good !!')
    elif x > 64:
        print('You got B+ that is Good !!')
    elif x > 59:
        print('You got B that is Satisfactory !!')
    elif x > 54:
        print('You got B- that is Above Average !!')
    elif x > 49:
        print('You got C+ that is Average !!')
    elif x > 44:
        print('You got C that is Bellow Average !!')
    elif x >= 40:
        print('You got D that is Pass !!')
    else:
        print('You are fucking Failure Person')
else:
    print('Highest Marks Is 100')
