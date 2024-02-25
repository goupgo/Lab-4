def Q1():
    fhandle1 = open('abc.txt',"r")
    read1 = f.read()
    uppercount = 0
    lines = read1.split('\n')
    for line in lines:
        for char in line:
            if char.isupper():
                uppercount += 1
    print('Total words:', uppercount)   

def Q2():
    fhandle2 = open('article.txt',"r")
    read2 = fhandle2.read()
    count_this = 0
    count_these = 0
    lines = read2.split(' ')
    for line in lines:
        if line == 'this':
            count_this += 1
        if line == 'these':
            count_these += 1
    print(count_this)
    print(count_these)