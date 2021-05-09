def swapFile():
    fileInfo = input('Enter file path for file 1:')
    fileInfo2 = input('Enter file path for file 2:')

    file1 = open(fileInfo, 'r')
    read1 = file1.read()
    file2 = open(fileInfo2, 'r')
    read2 = file1.read()

    with open(fileInfo, 'w') as file1:
        file1.write(read2)

    with open(fileInfo2, 'w') as file2:
        file2.write(read1)

    print('Swap has been completed')
swapFile()