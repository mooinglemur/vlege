#!/usr/bin/env python3

## Dependencies
# File-handling
import os
# Image-handling
from PIL import Image

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
        # Prepare for failure
        try:
            # Full path to file
            filepath=root+"/"
            # Pull apart filename
            filesplit=os.path.splitext(filename)
            # Skip non-images
            if filesplit[1].lower() != ".jpg":
                continue
            # Basic name of file
            filebase=filepath+filesplit[0]
            # Echo
            print("File: "+filepath+filename)
            # Load file
            img = Image.open(filepath+filename)
            # Create+save a Thumbnail
            thumb = img.copy()
            thumb.thumbnail(size["thumb"])
            thumb.save(filebase+"-thumb.jpg")
            # Do we need a Medium?
            if img.size > size["medium"]:
                # Create+savea Medium
                medium = img.copy()
                medium.thumbnail(size["medium"])
                medium.save(filebase+"-medium.jpg")
        # Failure found!
        except IOError:
            print("Could not make thumbnail")

