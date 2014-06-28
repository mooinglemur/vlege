Vlege Design
============

This document is a Work-In-Progress, being used to design the basic layout of the Vlege system and expect gallery structure.

General Principles
------------------

 1. Be Pythonic.
 2. Rely upon the filesystem
 3. Avoid complex data structures. 

Gallery Structure
-----------------

 *  index.html
 *  (Gallery)/
     *  index.html
     *  index.json
     *  (Gallery)/ [Recursion supported]
         *  index.html
         *  index.json
         *  Image0001.jpg
         *  Image0001-thumb.jpg
         *  Image0001-medium.jpg
         *  Image0001.json
 *  resources/
     *  vlege.js
     *  vlege.css
