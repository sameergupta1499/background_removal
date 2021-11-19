from zipfile import ZipFile
import os
from os.path import basename
cwd = os.getcwd()
image_dir = cwd + "/images/"
file1 = open('url.txt', 'r')
file_name = file1.readline()
total_lines = [i for i in file_name.split() if i.isdigit()][0]
file_name=file_name.replace(total_lines,'')
file_name=file_name.replace(' ','_')
file_name=file_name.replace('\n','')
file_name = file_name+'.zip'
if file_name=='.zip':
    file_name='images.zip'
# print(file_name)
# print(image_dir)
with ZipFile('zip/'+file_name, 'w') as zipObj:
   # Iterate over all the files in directory
   for folderName, subfolders, filenames in os.walk(image_dir):
       for filename in filenames:
           #create complete filepath of file in directory
           filePath = os.path.join(folderName, filename)
           # Add file to zip
           zipObj.write(filePath, basename(filePath))

print('images zip successfully!')