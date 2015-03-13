#!/usr/bin/env python3
# vlege/vlege.py
# EugeneKay/vlege
#
# Vlege
#
# Vlege is a Very Low-Effort Gallery Engine, powering HTML image galleries
# based upon a native filesystem structure. Complicated server-side scripting
# languages and databases are eschewed in favor of basic HTML and JavaScript
# generated using a simple Python script and some helpful libraries.
#
# Copyright(c) 2014 Vlege Authors, including Eugene E. Kashpureff Jr.
# Licensed under GNU GPLv3+. See included README for more information
#


## Dependencies
# Basics
import os
import sys
# Logging
import logging
# CLI friendliness
import argparse
# Image-handling
from PIL import Image, ImageOps
# Output templating
import jinja2


## Function definitions
def vlege(path=None, thumb=200, dryrun=False):
    """Vlege-ize a path

    Keyword arguments:
    path -- path to be Vlege-ized
    thumb -- max pixel dimension of thumbnails
    """

    ## Sanitize variables
    # Existance of path
    if not os.path.isdir(path):
        raise MyError("Invalid album path specified. Must be a directory.")
    # Normalize path name
    path=os.path.normpath(path)

    # Size of thumb
    size={}
    size["thumb"]=(thumb, thumb)

    ## Initialize Jinja
    # Initialize Jinja
    JINJA=jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(
        os.path.realpath(__file__))))
    index_template=JINJA.get_template('index.html.jinja')

    ## Directory processing loop
    # Walk filesystem hierarchy
    for root, dirs, files in os.walk(path, topdown=False):
        # Currently-processing directory
        logging.info("Directory: %s" % root)
        dir_path=root+"/"
        dir_name=os.path.basename(root)

        # Reset for this directory
        folders=[]
        images=[]

        ## Subdirectory processing loop
        dirs.sort()
        for subdir in dirs:
            logging.info("Subdir: %s" % subdir)
            # Add to list
            folders.append({'name': subdir})

        ## Image processing loop
        files.sort()
        for filename in files:
            # Pull apart filename
            file_split=os.path.splitext(filename)
            # Basic name of file
            file_base=file_split[0]
            # Extension of file
            file_ext=file_split[1].lower()
            # Information
            logging.info("File: "+filename)
            # Skip non-images
            if file_ext !=".jpg":
                logging.info("Skipped, not a jpg")
                continue
            # Only process originals
            if "-thumb" in file_base:
                logging.info("Skipped, is a thumb")
                continue
            # Add to list
            images.append({'file': filename,
                          'thumb': file_base+'-thumb.jpg'})
            # Skip already-processed
            if os.path.isfile(dir_path+file_base+"-thumb.jpg"):
                logging.info("Skipped, thumb found")
                continue
            # Don't process on dry runs
            if dryrun is True:
                continue
            # Load file
            try:
                img=Image.open(dir_path+filename)
            except IOError:
                logging.error("Could not open file "+dir_path+filename)
                continue
            # Create+save a Thumbnail
            try:
                thumb=ImageOps.fit(img, size["thumb"],
                                   method=Image.ANTIALIAS)
                thumb.save(dir_path+file_base+"-thumb.jpg")
            except IOError:
                logging.error("Could not create thumb " + dir_path+file_base +
                              "-thumb.jpg")

        ## Index file building
        # Album information
        logging.info("Building index for " + root)
        index_value={'album': {'title': dir_name,
                               'separator': '-',
                               'path': root},
                     'folders': folders,
                     'images': images}
        # Generate index
        index_rendered=index_template.render(index_values)
        # Skip on dry runs
        if dryrun is True:
            continue
        # Open+truncate index file
        index_file=open(root+'/index.html', 'w')
        # Write out contents
        index_file.write(index_rendered)
        # Done with file
        index_file.close()


def main():
    ## Argument parsing
    # Initialize
    parser=argparse.ArgumentParser("vlege")

    # Enumerate args
    parser.add_argument("-d", "--dryrun", action="store_true",
                        help="Perform a dry run(do not modify files)")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Increase output verbosity")
    parser.add_argument("album", help="Path to an album to be processed")

    # Annnd... parse!
    args=parser.parse_args()

    # Set up logging
    if args.verbose:
        # Verbose logging
        logging.basicConfig(format="%(levelname)s: %(message)s",
                            level=logging.DEBUG)
        logging.info("Verbose output enabled")
    else:
        # Standard logging
        logging.basicConfig(format="%(levelname)s: %(message)s")

    logging.info("Executing main loop")
    vlege(path=args.album, dryrun=args.dryrun)

if __name__ == "__main__":
    sys.exit(main())
