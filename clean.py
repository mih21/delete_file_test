import os
import glob

directory='test'
os.chdir(directory)
files=glob.glob('*')
for filename in files:
    os.unlink(filename)