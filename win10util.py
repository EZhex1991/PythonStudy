#
# description:
#

import os
import shutil

from PIL import Image


class Win10AssetSaver:
    srcdirpath = os.path.join(
        os.environ["UserProfile"], "AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets")

    def saveBackgrounds(dstdirpath, sizefilter):
        print("source: ", Win10AssetSaver.srcdirpath)
        print("destination:", dstdirpath)
        fileset = set()
        if os.path.exists(dstdirpath):
            for root, dirnames, filenames in os.walk(dstdirpath):
                for filename in filenames:
                    fileset.add(os.path.splitext(filename)[0])
        else:
            os.mkdir(dstdirpath)
        for root, dirnames, filenames in os.walk(Win10AssetSaver.srcdirpath):
            for filename in filenames:
                src = os.path.join(root, filename)
                dst = os.path.join(dstdirpath, filename)

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
        print("complete.", end="\n\n")


Win10AssetSaver.saveBackgrounds(os.path.join(
    os.environ["OneDrive"], "Pictures/Win10_1920x1080"), (1920, 1080))
Win10AssetSaver.saveBackgrounds(os.path.join(
    os.environ["OneDrive"], "Pictures/Win10_1080x1920"), (1080, 1920))
