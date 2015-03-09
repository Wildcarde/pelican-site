Title: Framing the Problem: Building a Dicom Storage Server with Open Source / Free Software
Slug: Problem-Building-Dicom-Storage-ossFOSS
Date: 2010-10-14
Category: Sysadmin
Tags: Sysadmin, Dicom


I should state at the outset that our needs for a Dicom Server are a different than most use cases for the system.  In a standard system you configure a Central Test Node / PAC server to store all of your images.  These systems can typically store images by study ID, patient ID, test administer ID or several other permutations of this information.  Then any device that implements the network standard can directly connect to the server and request based on this meta data and it pops up on their screen.  This is a fantastic approach if your in a hospital or doctors office / medical center as it allows you to retrieve data in remote locations and poke at it pretty easily.

However this very convenient system is not at all convenient if you want to be able to extract the Dicom files out onto a NAS for processing on a cluster.  Specifically we need to be able to farm images out into their respective labs storage area (at the labs will, not ours).  Presently this is done via manual intervention on the parts of the labs by running a command we've labeled 'dicom rename' which accepts a subject ID and a few other flags, then dumps the related files into a specified destination folder with 'pretty' names.  From here they can run conversion scripts on these renamed files to make them friendlier to the myriad analysis programs our labs use in their individual tool-chains.

Up until now we've been running a program simply called CTN (Central Test Node) which has served us OK.  This package was originally written to demonstrate the ideas presented in the Dicom spec so that there was a test to run against for what appears to have amounted to a vendor fair.  It's fairly thin and doesn't implement much, other than a Dicom Storage interface keeping the files in huge mangled directory names with a lookup in a MySQL database.  This system has worked fine as noted with a few fixes here and there to make it work with newer versions of MySQL.

Be that as it may, this system is a dead end with no development being done on it.  On the heels of this fact we are also bringing a new system online that probably will not work with our old server system or if we can even configure the old system to accept simultaneous transfers from two sources.  In lieu of finding out the hard way we are moving on to a new system.  However what form that system will take has yet to be determined and we are currently attempting to evaluate our options (attempting because finding this information is proving less trivial than expected).  The challenge being:  Find a new software package that is flexible enough to allow us to slot it into our current work flow but stable enough to handle large data transfers from multiple hosts simultaneously.  It would be nice to be able to add extensions and automation features to it as well (like say.. auto rename scripts, cutting out the need for a database entirely).

If anyone knows anything that fits the bill feel free to post it in the comments.  For my part I'll be writing at least one more post on this discussing the packages we've looked at and evaluated as well as a post about how we finally got it setup.

TLDR:  
Finding Dicom Servers is less easy than expected, but I'm going to do the legwork for you.  Any helper functions we write will eventually make it into the pni-toolbox repository (free code!).

Brass Tacks:  
I will probably get sick of doing this at some point and simply pick the best option of what's currently been tested instead of evaluating every possible option / permutation.
