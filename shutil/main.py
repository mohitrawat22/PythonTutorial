import shutil
import os

# copy main.py to main2.py (if already exist then it overwrites)
shutil.copy('shutil/main.py', 'shutil/main2.py')

# copy main.py to main3.py (if already exist then it overwrites) with metadata
shutil.copy2('shutil/main.py', 'shutil/main3.py')

# copy contents of mainfolder1 to mainfolder2 (if already exist then merge)
shutil.copytree('shutil/mainfolder1', 'shutil/mainfolder2')

# move file from one location to another
shutil.move('shutil/mainfolder2/mainfolder_file1.py', 'shutil/mainfolder_file1.py')

# deletes folder and its contents
shutil.rmtree("shutil/mainfolder1")

# deletes a file
os.remove('shutil/mainfolder_file1.py')