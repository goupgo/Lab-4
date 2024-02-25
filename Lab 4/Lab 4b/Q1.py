def Q1():
    handle = open('poem.txt',"r")
    print(handle.read())

def Q2():
    fhandle = open('story.txt',"r")
    read2 = f.read()
    count = 0
    lines = read2.split('\n')
    for line in lines:
        if line[0] != 'T':
            count+=1
    print('No of lines which not start with "T":',count)