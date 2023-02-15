import os
import shutil
import glob

#executable file is located in /dist/main 
#path to directory - need to change for every new computer - after change need to make into an executable file again
path = '/Users/hungtuan.nguyen/Downloads/'
            
#get a list of all the files, sorted by modified time, descending
files = list(filter(os.path.isfile, glob.glob(path+'*'))) #filter just files, not dir, and glob.glob is to get all files in the path
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
        if os.path.exists(path+'Images'):
            shutil.move(name+'.'+ext,path+'Images')
        else:
            os.makedirs(path+'Images')
            shutil.move(name+'.'+ext,path+'Images')
    else:
        #with non-image file, go with this flow
        if os.path.exists(path+ext):
            shutil.move(name+'.'+ext,path+ext)
        else:
            os.makedirs(path+ext)
            shutil.move(name+'.'+ext,path+ext)

