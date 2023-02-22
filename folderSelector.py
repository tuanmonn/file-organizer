import os
import tkinter as tk
from tkinter.filedialog import askdirectory

#get the root dir of every laptop
root_dir = os.path.expanduser('~')

#get the path of the file we use to store user input
input_file_dir = root_dir + '/' + 'user_input.txt'


def run_program(): 
    path = 0 
    #open a window to confirm success
    def success_conf():
        window_success = tk.Toplevel(window)
        window_success.title("Confirmation")
        window_success_label = tk.Label(window_success,text="You're all set!\n Check your folder, everything is cleaned up now ✅")
        window_success_label.pack()
        window_success_button = tk.Button(window_success,text="Close", command=window_success.quit)
        window_success_button.pack()
        
    #define a function to open folder selector
    def folder_selector():
        folder = askdirectory(title='Select Folder')
        path = os.path.realpath(folder)
        with open(input_file_dir,'w') as f:
            f.write(path)
            f.close()
        success_conf()
        return path
    
    #main program logic
    if not os.path.exists(input_file_dir):
        #start the window
        window = tk.Tk()
        window.title("File Organizer by Tuanmonn")
        window.geometry("300x200")
        
        #create label
        label_welcome = tk.Label(text="Welcome to File Organizer!")
        label_ins = tk.Label(text="Please choose the folder you want to clean up")
        label_welcome.pack()
        label_ins.pack()
        
        #create a button to let user select folder
        button = tk.Button(text="Select Folder",command=folder_selector)
        button.pack()
        
        #keep the window open
        window.mainloop()
        return path
        
    else:
        with open(input_file_dir,'r') as f:
            path = f.read()
            f.close()
        return path
                
