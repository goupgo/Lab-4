def Q1():
    fopen = open('abc.txt',"r")
    sread = fopen.read()
    count = 0
    lines = sread.split('\n')
    for line in lines:
        for j in line:
            count+=1
    print('Total words:',count)
    
def display_words():
    fhandle = open('abc.txt',"r")
    read2 = fhandle.read()
    lines = read2.split(' ')
    for line in lines:
        if len(line) <= 4:
            print(line, end=' ')