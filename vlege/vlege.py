#!/usr/bin/env python3

## Dependencies
# File-handling
import os
# Image-handling
from PIL import Image
# Argument-handling
import argparse
# Logging
import logging

## Define constants
# Initialize empty array
size={}
# Size of thumbnails
size["thumb"]=(200,200)
# Size of intermediates
size["medium"]=(1000,1000)

## Argument parsing
# Initialize
parser = argparse.ArgumentParser()
# Enumerate args
parser.add_argument("-v", "--verbose", help="Increase output verbosity",
                    action="store_true")
# Annnd... parse!
args = parser.parse_args()

## Output & Logging
if args.verbose:
    # Verbose logging
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)
    logging.info("Verbose output.")
else:
    # Standard logging
    logging.basicConfig(format="%(levelname)s: %(message)s")

## Main Loop
# Walk filesystem hierarchy
for root, dirs, files in os.walk("."):
    # Current directory
    logging.info("Directory: "+root)
    # Walk through files
    for filename in files:
        # Full path to file
        filepath=root+"/"
        # Pull apart filename
        filesplit=os.path.splitext(filename)
        # Basic name of file
        filebase=filepath+filesplit[0]
        # Echo
        logging.info("File: "+filepath+filename)
        # Skip non-images
        if filesplit[1].lower() != ".jpg":
            logging.info("Skipped, not a jpg")
            continue
        # Skip already-processed
        if os.path.isfile(filebase+"-thumb.jpg"):
            logging.info("Skipped, thumb found")
            continue
        # Only process originals
        if "-medium" in filesplit[0] or "-thumb" in filesplit[0]:
            logging.info("Skipped, is a thumb/med")
            continue
        # Load file
        try:
            img = Image.open(filepath+filename)
        except IOError:
            logging.error("Could not open file")
            continue
        # Create+save a Thumbnail
        thumb = img.copy()
        try:
            thumb.thumbnail(size["thumb"])
            thumb.save(filebase+"-thumb.jpg")
        except IOError:
            logging.error("Could not create thumb")
        # Do we need a Medium?
        if img.size > size["medium"]:
            # Create+savea Medium
            try:
                medium = img.copy()
                medium.thumbnail(size["medium"])
                medium.save(filebase+"-medium.jpg")
            except IOError:
                logging.error("Could not create medium")

