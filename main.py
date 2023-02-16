import os
import shutil
import glob
from tkinter import Tk 
from tkinter.filedialog import askdirectory
from folderSelector import *
 
run_program()
selected_path = run_program() 
            
#get a list of all the files, sorted by modified time, descending
files = list(filter(os.path.isfile, glob.glob(selected_path+'/'+'*'))) #filter just files, not dir, and glob.glob is to get all files in the path
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
        if os.path.exists(selected_path+'/'+'Images'):
            shutil.move(name+'.'+ext,selected_path+'/'+'Images')
        else:
            os.makedirs(selected_path+'/'+'Images')
            shutil.move(name+'.'+ext,selected_path+'/'+'Images')
    else:
        #with non-image file, go with this flow
        if os.path.exists(selected_path+'/'+ext):
            shutil.move(name+'.'+ext,selected_path+'/'+ext)
        else:
            os.makedirs(selected_path+'/'+ext)
            shutil.move(name+'.'+ext,selected_path+'/'+ext)

