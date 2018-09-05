
# File Opening, The First Process


errorfile = open('/media/sh1mu7/1CD23A07D239E5A4/Work/Python/PythonPracticepad/hex_note')
errorfile.seek(0)

print(errorfile.readlines())
errorfile.close()


# second Option TO open is more secure


with open('/media/sh1mu7/1CD23A07D239E5A4/Work/Python/PythonPracticepad/hex_note') as myFile:
    lines=myFile.read()

print(lines)


# this is how create a new file and read from this file and
# remind that write method is always override the other text file and
#  it also create the file if the file does not exist in directory


with open('/media/sh1mu7/1CD23A07D239E5A4/Work/Python/PythonPracticepad/hex_note2','w') as my_new_File:
    my_new_File.write('Hey Mahmudul')
with open('/media/sh1mu7/1CD23A07D239E5A4/Work/Python/PythonPracticepad/hex_note2','r') as my_new_File:
    print(my_new_File.read())


# Appending is the way to add another lines without overriding the previous lines
# (a) is for only for append (a+) is for append read and write mode


with open('/media/sh1mu7/1CD23A07D239E5A4/Work/Python/PythonPracticepad/hex_note2','a') as my_new_File:
    my_new_File.write('Hey Mahmudul')
with open('/media/sh1mu7/1CD23A07D239E5A4/Work/Python/PythonPracticepad/hex_note2','r') as my_new_File:
    print(my_new_File.read())


    