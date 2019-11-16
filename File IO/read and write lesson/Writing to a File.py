#Lesson on Writing to a file
#ICS4U0
#Mr Veera
#16 MAY 2018

fp = open("File IO/read and write lesson/pc_writetest.tmp", "w")              # The first argument in the open() function
                                                # is the physical file name/path.
                                                # The second argument can be one of the following:
                                                #
                                                # 1. 'w' - write mode. If file already exists, then
                                                # it is over written. Incase file does not exist,
                                                # a new file is created and then written into.
                                                #
                                                # 2. 'a' - append mode. Whatever is being written is
                                                # appended at the end of what already exists in the file.
                                                #
                                                # 3. 'r+' - read/write mode.
                                                # The file is opened for read or write operations.
                                                #
                                                # 4. 'r' - read mode. The file is opened in read mode.
                                                #
                                                # The second argument is optional, in case omitted,
                                                # the default mode is 'r'.

while True:
    text = input("Please enter a line of text( double 'Enter' keystroke to end): ")
    if text=='':
        break
    else:
        text=text+'\n'
        fp.write(text)
##        print(fp.write(text))                 # prints the number of characters written
                                                # returned by the write function.
fp.close()

fp = open("pc_writetest.tmp")
buffer = fp.read()
fp.close()
print(buffer)
