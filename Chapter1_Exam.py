#Task 1

with open('/media/sh1mu7/1CD23A07D239E5A4/Work/Python/PythonPracticepad/hex_note3','w') as NewFile:
    NewFile.write('Hello How Are you ??\n If you dont mind i ask you some question ??\n WHa ts your name?')


with open('/media/sh1mu7/1CD23A07D239E5A4/Work/Python/PythonPracticepad/hex_note3','r') as ReadNewFile:
    lines=ReadNewFile.readlines()

#     #print all the lines the file does have

    print(lines)

    # #Print number of lines

    print(len(lines))

    # #print last line of your file
    last=lines[-1]
    print(last)

    # count 'O' from last line

    print(last[8])

    print(len(last.split()))
    # #print 2nd line of your file

    print(lines[1])

my_dict={'key1':[1,2,{'key2':[5,6,[1,['Get me out please']]]}]}

print(my_dict['key1'][2]['key2'][2][1])