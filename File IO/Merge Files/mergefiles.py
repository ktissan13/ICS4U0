# Merge Files
# Tissan Kugathas
# ICS4U0
# November 14 2019

with open('File IO/Merge Files/temp.tmp','w') as final:
    with open('File IO/Merge Files/file1.txt','r') as file1:
        list1 = list(file1)
        with open('File IO/Merge Files/file2.txt','r') as file2:
            list2 = list(file2)
            index1 = 0
            index2 = 0
            while index1 != len(list1) or index2 != len(list2):
                if index1 < len(list1) and index2 < len(list2):
                    if int(list1[index1]) < int(list2[index2]):
                        final.write(list1[index1])
                        index1 += 1
                    elif int(list1[index1]) > int(list2[index2]):
                        final.write(list2[index2])
                        index2 += 1
                else:
                    if index1 < len(list1):
                        final.write(list1[index1])
                        index1 += 1
                    if index2 < len(list2):
                        final.write(list2[index2])
                        index2 += 1
