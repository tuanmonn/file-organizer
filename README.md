# file-organizer

## Problem
On macOS, everything I download from the Internet will land on the Downloads folder. 

After a while, this folder becomes a mess of all file types that I may or may not need. Although I am using Raycast (Apple Spotlight on steroid), scraping through such a mess for files, especially new ones is hugely time-consuming. 

## Solution requirements
With the above pain point, I need a solution to:
1. Cleanup my Downloads folder periodically (ideally every day) so whenever there is a newly downloaded file, I can spot them right away.
2. Keep an archive of all the old files, well, just in case.

## Introducing: File Organizer (FO) (excuse my poor naming attempt, this app is not for commercial distribution yet!)

### What does it do?
- (With minimal setup) FO will run periodically (set by you) to bring all the files of the same type into the same folder.
- If your files are images, with extension of {png, jpeg, jpg,...} it will be grouped under the folder "Images" (cuz I have images of many filetypes and I don't want to sort through 'png', 'jpeg',
'jpg' folders just to find one single image, okay?)

### How to use FO?
1. See that lil green button with '<> Code' word up there? Yes, on the upper right. Click on it. Download the ZIP.
2. If you're pro and want to prove your un-laziness to no one, go ahead and run the main.py in the ZIP. Otherwise, skip this step.
3. Go to dist/main, and click on the file 'main'. Yes that lil black one that looks like the terminal window. 
4. The program will run, opening a window for you to select the folder you want to clean up. 
5. Choose the folder and let the magic works. Check your folder and gasps in disbelief. 

**Eh wait, what if you want to automate this?**
On macOS, there's a program called **Crontab** that can let you schedule a task to run periodically. Follow these steps to set up Crontab to work with FO:

1. Open your terminal, type `crontab -e` to open the editor of crontab
2. Press `i` to enter "insert" mode (equivalent: edit mode, stupid name)
3. Use the special command of crontab to schedule. 

After rigorous search attempt, I figured out the **correct** command to use for my computer (why doesn't the Internet have it before?). It's in this format:

`[special_command_for_the_schedule] [space] [path_to_the_executable_file_dont_input_the_extension]`

Example:

`* * * * * /Users/{your_username}/Downloads/python-file-organizer/file-organizer/dist/main/main`

_Notes: For the special commands of crontab, visit: https://crontab.guru/_

4. After you write the command, press `Esc` to exit the "insert" mode. Then type `:wq` (`w` - write, `q` - quit), press `Enter` to run the command. 
5. If the command is run successfully, you'll see a system popup of crontab asking for permission to administer our computer. Allow it. 
6. To double check that the crontab is created, you can write `crontab -l`.
7. If you want to delete the job you just created, write `crontab -r`. 
8. That's it! Now our program will run on the period that we've just specified. 


