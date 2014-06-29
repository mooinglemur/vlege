#!/usr/bin/env python3

import os
from PIL import Image

size={}
size["thumb"]=(200,200)
size["medium"]=(1000,1000)


for root, dirs, files in os.walk("."):
    print("Directory: ", root)
    for filename in files:
        try:
            filepath=root+"/"
            filesplit=os.path.splitext(filename)
            if filesplit[1].lower() != ".jpg":
                continue
            filebase=filepath+filesplit[0]
            print("File: "+filepath+filename)
            img = Image.open(filepath+filename)
            thumb = img.copy()
            thumb.thumbnail(size["thumb"])
            thumb.save(filebase+"-thumb.jpg")
            if img.size > size["medium"]:
                medium = img.copy()
                medium.thumbnail(size["medium"])
                medium.save(filebase+"-medium.jpg")
        except IOError:
            print("Could not make thumbnail")

