<!--
# README.md
# EugeneKay/vlege
-->

Vlege
=====


Table of Contents
-----------------

  1. [About](#about)
  2. [Usage](#usage)
  3. [Copyright](#copyright)
  4. [Changelog](#changelog)
  5. [Authors](#authors)
  6. [License](#license)


About
-----

Vlege is a **Very Low-Effort Gallery Engine**, powering HTML image galleries based upon a native filesystem structure. Complicated server-side scripting languages and databases are eschewed in favor of basic HTML and JavaScript generated using a simple Python script and some helpful libraries.


Usage
-----

First make sure you have Python3 and the necessary libraries installed, using your system's package system or via `pip`. You will need *Pillow* and *Jinja2*. Then Install Vlege by downloading the script and placing it in your `$PATH` somewhere.

```
$ mkdir ~/bin
$ PATH=$PATH:~/bin
$ [curl https://raw.githubusercontent.com/EugeneKay/vlege/dev/vlege/vlege.py](https://raw.githubusercontent.com/EugeneKay/vlege/dev/vlege/vlege.py) > ~/bin/vlege
$ chmod +x ~/bin/vlege
$
```

Now run Vlege by pointing it at your album.

```
$ vlege /path/to/your/album/
$
```

If everything went well, you should get a pile of -thumb and -medium images, along with an index.html listing.


Copyright
---------

Vlege is Copyright&copy; 2014 by Vlege Authors, enumerated in the [Authors](#authors) section of this README document. Detailed authorship can be found by examining the source code repository via the `git blame` command.

The **Vlege** name is Copright&copy; 2014 Eugene E. Kashpureff Jr, and is pending trademark registration in the United States of America. Usage of the name is permitted when referring to the Vlege software or its usage. See the [License](#license) section of this document for the grants associated with this mark.

Any included libraries are copyright by their respective authors, as noted in their source files.


Changelog
---------

Changelog for this release(**v0.1**):

  * Initial stable-ish release
  * Basic image-creation functionality
  * Ostensibly an import-able module
  * Includes a README!

See the [CHANGELOG](CHANGELOG.md) for historical entries, or the git source repository for per-commit change information.


Authors
-------

Primary Author & Maintainer:
  * [Eugene E. Kashpureff Jr](mailto:eugene@kashpureff.org)


License
-------

Vlege is offered as free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. If you wish to obtain Vlege under another license(including a proprietary commercial license) for inclusion into other software or use in a situation where the GNU GPL is not acceptable, you may contact the Maintainer for further information.

When obtained under the GNU General Public License, Vlege is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with Vlege. If not, you may obtain it from the [GNU Project](http://www.gnu.org/licenses/).

Usage of the **Vlege** mark is restricted to the primary Vlege [software](https://github.com/EugeneKay/vlege) distributed by Eugene E. Kashpureff Jr, and references to and usage of the same. Further permission is given to use this mark in a manner consistent with the purpose and image of the brand, eg, "Powered by Vlege".

Any public distribution, fork, or usage of Vlege which differs substantially from the original must be rebranded to prevent confusion with the canonical distribution. Reference to Vlege is permitted(eg, "Based upon Vlege"), within the same *reasonable* conditions associated with the mark. Operation of a mirrored software repository, containing only a faithful redistribution of the original, is permitted, with the provision that it is to be marked as such.

Software or services which include Vlege code must maintain the Authors listing and License information contained in this document within their source code and any further redistributions. You may change the License to any license which is forward-compatible with the License under which you obtained Vlege, including any versions of the GNU General Public License higher than 3, or the GNU Affero General Public License version 3 or higher.

Software or services which utilize Vlege in an unchanged or minimally altered format(eg, dynamic or static linking of the code) may do so without further attribution, but any such attribution is appreciated by the authors, if present. The suggested format is: "Powered by [Vlege](http://github.com/EugeneKay/vlege)", with the 'Vlege' mark being a hyperlink to the named website, if the medium supports it.

The full source code for Vlege is available [on Github](https://github.com/eugenekay/vlege).
