import os
import shutil

#executable file is located in /dist/main 
#path to directory - need to change for every new computer - after change need to make into an executable file again
path = '/Users/hungtuan.nguyen/Downloads'

#create a list of all the files 
list_file = []

#create a list of all the filename
list_full = os.listdir(path)

#find all the files in the Downloads dir and add to the list_file
for a in list_full:
    #only work with file that start without '.' to ignore hidden sys files
    if not a.startswith('.'):
        isFile = os.path.isfile(path+'/'+a)
        if isFile:
            list_file.append(a)

#create a list of all image ext
list_img_ext_lower = ['png','jpg','jpeg','webp', 'gif', 'avif']
list_img_ext_full = []

#add to the full list all the lower and upper case
for i in range(len(list_img_ext_lower)):
    list_img_ext_full.append(list_img_ext_lower[i])
    list_img_ext_lower[i] = list_img_ext_lower[i].upper()
    list_img_ext_full.append(list_img_ext_lower[i])

#check the extension of all the file in list_file
for file in list_file:
    name, ext = os.path.splitext(file)
    ext=ext[1:]
    #with images file, go with this flow
    if ext in list_img_ext_full:
        #check if the "Image" folder exists:
        if os.path.exists(path+'/'+'Images'):
            shutil.move(path+'/'+file,path+'/'+'Images')
        else:
            os.makedirs(path+'/'+'Images')
            shutil.move(path+'/'+file,path+'/'+'Images')
    else:
        #with non-image file, go with this flow
        if os.path.exists(path+'/'+ext):
            shutil.move(path+'/'+file,path+'/'+ext)
        else:
            os.makedirs(path+'/'+ext)
            shutil.move(path+'/'+file,path+'/'+ext)

