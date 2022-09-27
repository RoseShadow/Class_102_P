from distutils import extension
import os
import shutil

from_dir= "C:/Users/pc/Downloads"
to_dir= "C:/Users/pc/Desktop/Whitehat junior/class/After Class100/python/Class 102 P"

dir_list=os.listdir(from_dir)

for file_name in  dir_list:
    name,ext=os.path.splitext(file_name)

    if ext =="":
        continue
    if ext in ['.ppt', '.xls', '.csv', '.pdf', '.txt']:
        path1 = from_dir + '/' + file_name                       # Example path1 : Downloads/ImageName1.jpg        
        path2 = to_dir + '/' + "Pdf_Files"                     # Example path2 : D:/My Files/Image_Files      
        path3 = to_dir + '/' + "Pdf_Files" + '/' + file_name

        if os.path.exists(path2) :
            print("moving")
            shutil.copy(path1,path3)

        else :
            os.makedirs(path2)
            print("moving")
            shutil.copy(path1,path3)
