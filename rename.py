import os
import shutil

srcdirpath = "C:\\Users\\ezhex\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\"

for root, dirnames, filenames in os.walk(srcdirpath):
    for filename in filenames:
        name, ext = os.path.splitext(filename)
        if ext == ".png":
            shutil.move(root + filename, root + name)
