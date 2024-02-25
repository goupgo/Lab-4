import os
import datetime

def q1():
    fhandle1 = open("sales.txt", "a")

def q2():
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    now = str(now) + '.txt'
    fhandle2 = open(now)

def q3():
    file_path = r'' 
    os.unmask(0)
    with open(os.open(file_path, os.O_CREAT | os.O_WRONLY, 0o777), 'w') as fh:
        fh.write('content')