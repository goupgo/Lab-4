import os
import shutil

def Q1():
    name = input()
    m ='./'+ name
    new = 'New_'+ name
    check_file = os.path.isfile(m)
    if check_file == True:
        os.rename(name, new)

def Q2():
    lst = ['sale_1.txt','sale_2.txt']
    lst_n = ['sales_1.txt','sales_2.txt']
    for i in range(len(lst)):
        os.rename(lst[i],lst_n[i])

def Q6(source_path, destination_path, new_filename):
    try:
        if os.path.exists(source_path):
            os.rename(source_path, os.path.join(destination_path, new_filename))
            print("File renamed successfully.")
        else:
            print("Source file does not exist.")
    except Exception as e:
        print("An error occurred:", e)


source_path = "source_folder/source_file.txt"  
destination_path = "destination_folder"       
new_filename = "new_file_name.txt"            

rename_and_move_file(source_path, destination_path, new_filename)