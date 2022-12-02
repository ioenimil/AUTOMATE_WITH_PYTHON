# Import neccessary modules from Pillow Library and the os module
from PIL import Image, ImageTk
import os

# Creat a list of files and sub-directories in the SAMPLE directory
array = os.listdir('C:/Users/USER/Desktop/SAMPLE')

# Opening, converting and saving file in pngs director
for file in array:
    if file.endswith('.jpg'):
        os.chdir('C:/Users/USER/Desktop/SAMPLE')
        img = Image.open(file)
        ft, te = file.split(sep='.')
        if 'pngs' not in array:
            os.mkdir('pngs')         
    img.save(f'./pngs/{ft}.png')
    
    
