#
# description:
#

import os
import shutil

from PIL import Image


class Win10AssetSaver:
    srcdirpath = ("C:\\Users\\ezhex\\AppData\\Local\\Packages"
                  "\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\")

    def saveBackground(dstdirpath, sizefilter):
        print(dstdirpath)
        fileset = set()
        if os.path.exists(dstdirpath):
            for root, dirnames, filenames in os.walk(dstdirpath):
                for filename in filenames:
                    fileset.add(os.path.splitext(filename)[0])
        else:
            os.mkdir(dstdirpath)
        for root, dirnames, filenames in os.walk(Win10AssetSaver.srcdirpath):
            for filename in filenames:
                src = root + filename
                dst = dstdirpath + filename

                # already exist
                if filename in fileset:
                    continue
                # image size filter
                try:
                    img = Image.open(src)
                    if not img.size == sizefilter:
                        continue
                except Exception:
                    continue

                print("copy %s" % filename)
                shutil.copy2(src, dst + ".jpg")
        print("complete.")


Win10AssetSaver.saveBackground("D:\\Image\\Win10Assets\\", (1920, 1080))
