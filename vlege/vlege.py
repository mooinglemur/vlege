#!/usr/bin/env python3

## Dependencies
# File-handling
import os
# Image-handling
from PIL import Image
# Argument-handling

## Variable setup
# Initialize empty array
size={}
# Size of thumbnails
size["thumb"]=(200,200)
# Size of intermediates
size["medium"]=(1000,1000)


# Walk filesystem hierarchy
for root, dirs, files in os.walk("."):
    # Current directory
    print("Directory: ", root)
    # Walk through files
    for filename in files:
        # Full path to file
        filepath=root+"/"
        # Pull apart filename
        filesplit=os.path.splitext(filename)
        # Basic name of file
        filebase=filepath+filesplit[0]
        # Echo
        print("File: "+filepath+filename)
        # Skip non-images
        if filesplit[1].lower() != ".jpg":
            print("Not a jpg!")
            continue
        # Skip already-processed
        if os.path.isfile(filebase+"-thumb.jpg"):
            print("Thumb found!")
            continue
        # Only process originals
        if "-medium" in filesplit[0] or "-thumb" in filesplit[0]:
            print("Not an original!")
            continue
        # Load file
        try:
            img = Image.open(filepath+filename)
        except IOError:
            print("Could not open file!")
            continue
        # Create+save a Thumbnail
        thumb = img.copy()
        try:
            thumb.thumbnail(size["thumb"])
            thumb.save(filebase+"-thumb.jpg")
        except IOError:
            print("Could not create thumb!")
        # Do we need a Medium?
        if img.size > size["medium"]:
            # Create+savea Medium
            try:
                medium = img.copy()
                medium.thumbnail(size["medium"])
                medium.save(filebase+"-medium.jpg")
            except IOError:
                print("Could not create medium!")

