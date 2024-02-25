def q1():
    handle1 = open('q2.1.txt', 'w')
    content = input()
    handle1.write(content)
    handle1.close()

def q2():
    name = input('Enter an existing file: ')
    handle2 = open(name, 'w')
    content = input()
    handle2.write(content)
    handle2.close()

def q3():
    handle3 = open('q2.3.txt', 'w')
    lines = []
    while True:
        dong = input('Nhap line')
        cach_dong = dong + '\n'
        lines.append(cach_dong)
        if dong == 'End!':
            break
    for line in lines:
        handle3.write(line)
    handle3.close()
        
        