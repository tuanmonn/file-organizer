import os
import shutil
import glob
from tkinter import Tk 
from tkinter.filedialog import askdirectory

#get the root dir of every laptop
root_dir = os.path.expanduser('~')

#get the path of the file we use to store user input
input_file_dir = root_dir + '/' + 'user_input.txt'

#check if that path exists (this program has been run before)
#if not, prompt user to input the folder they want to do the cleanup
if not os.path.exists(input_file_dir):
    folder = askdirectory(title='Select Folder')
    path = os.path.realpath(folder)
    with open(input_file_dir,'w') as f:
        f.write(path)
        f.close()
#if yes, check the file for the path that user has input
else:
    with open(input_file_dir,'r') as f:
        path = f.read()
        f.close()
            
#get a list of all the files, sorted by modified time, descending
files = list(filter(os.path.isfile, glob.glob(path+'/'+'*'))) #filter just files, not dir, and glob.glob is to get all files in the path
files.sort(key=lambda x: -os.path.getmtime(x)) 

#now list_full contains all files only, sorted by mtime

#create a list of all image ext
list_img_ext = ['png','jpg','jpeg','webp', 'gif', 'avif']

#check the extension of all the file in list_file
for file in files:
    name, ext = os.path.splitext(file)
    ext=ext[1:]
    #with images file, go with this flow
    if ext.lower() in list_img_ext:
        #check if the "Image" folder exists:
        if os.path.exists(path+'/'+'Images'):
            shutil.move(name+'.'+ext,path+'/'+'Images')
        else:
            os.makedirs(path+'/'+'Images')
            shutil.move(name+'.'+ext,path+'/'+'Images')
    else:
        #with non-image file, go with this flow
        if os.path.exists(path+'/'+ext):
            shutil.move(name+'.'+ext,path+'/'+ext)
        else:
            os.makedirs(path+'/'+ext)
            shutil.move(name+'.'+ext,path+'/'+ext)

