Title: Dicom Server Rundown
Slug: Dicom-Server-Rundown
Date: 2011-01-07
Category: Sysadmin
Tags: Sysadmin, Dicom, CTN, DCF, Offis, DCM4che, XNat, Conquest, PACSOne, ClearCanvas

A few weeks ago (ok.. weeks may no longer be accurate..) I noted that I was starting a new project to get a Dicom server up and running, here I present the results of all my reading and poking and prodding.  The first thing to know is there is no silver bullet, none of these represented the ideal solution in my eyes and they are all clearly driven by their individual groups needs.  That said some turned out to be more practical than others in the long run.


[CTN](ftp://ftp.erl.wustl.edu/pub/dicom/software/ctn/)

This is the package we've been running up till now.  It's biggest appeal is that exact legacy, we know it and it's idiosyncrasies.  Sorta kinda at least, we don't know it well enough to clean out the associated MySQL database for instance.  A bigger downside is that it hasn't been maintained since 2003, and this leads to some nuisances in getting it built on a Centos 5 install, but these problems are by no means deal breakers.  The bigger problem is the configuration which involves a combination of both compiler flags, MySQL tweaks and environmental variables that need to be configured just right for the house of cards to start up without throwing a fit.  It also requires our users to utilize some helper scripts that I'd like to excise if possible from our overall tool-chain.

[DCF - Dicom Connectivity Framework](http://www.laurelbridge.com/pdf/DCF-Product-Description.pdf)

A fairly powerful package if you have the time and inclination to do it yourself.  Manufacturing tools that deal with Dicom files and protocols in C#.NET, Java or C++.  However, this is an SDK.  There doesn't appear to be any official quick tools for setting up a default environment that you can just tweak.  It may be there but the advertisement page doesn't discuss it.  The 'Compass' package from the associated company seems more inline with what I was looking for but it's a pay for product and that breaks the goal of my project by being pay for.


[Dicom.offis](http://dicom.offis.de/index.php.en)

Sadly this software seems like it could fit the bill very well.  In their listing of 'Dicom Software' they even have a program called 'DCMSTCOM' which appears to be a storage application built off their free toolkit DCMTK.  It however is not free and as such is off the list of options for the purposes of this project.  That said, DCMTK could be used to build a new storage system for free (as it itself is free) but this isn't the pre built / tested land we are looking for here.  An extremely bare-bone server is included in DCMTK called '[storescp](http://support.dcmtk.org/docs/storescp.html)', however I'm not sure how one is supposed to know it exists since there's no way to get to the documentation without a google search (and prior knowledge).

[Dcm4che](http://www.dcm4che.org/confluence/display/ee2/Home)

All I can say is I found this package.  Beyond that.. I can't offer much, the documentation on what it does is effectively non existent, however there's an [extensive page on how to install it](http://www.dcm4che.org/confluence/display/ee2/Installation).  There's some man pages and --help dumps you can get from individual tools but no overall documentation to show you how to use the package, which program does what or the really useful stuff like 'configs for typical use scenarios'.

[XNAT](http://www.xnat.org/)

This is an enormous 'do everything' package that's actually free.  Or at least it appears to be, I left the page a bit fuzzy on that part.  However it actually does too much (yes that's possible) as it's a storage system and an entire workflow / processing engine.  If we wanted to uproot the entire way we do everything from project creation, to patient registration and introduce the ability to audit and QA all these different points simultaneously this package could do that happily.  It'll even act as the 'send to' target for scanners through it's [DicomServer](http://nrg.wustl.edu/projects/DICOM/DicomServer.jsp) package but it appears you have to buy into the whole XNAT system to utilize this piece.  You can't just use it as a storage system, you also have to use the project / subject management sections of the code as they are all interlinked.  This is again, great for a hospital and fairly unhelpful in our present research setting even if it is a very clean looking piece of software.


[Conquest](http://www.xs4all.nl/~ingenium/dicom.html)

Conquest is a free solution that seems to be fairly tweak able, down to the way you want your file names stored.  Like many of the systems here the documentation is a bit slap dash but it gets you there with a little plugging.  On top of this there is a community that appears to have the active participation of the developers behind it so that's promising.  It can also be back ended by a number of different database systems and used as a dicom router for people looking to build larger more complex configurations than what we are doing, or simple no database required configurations (exactly what we want).  A nice touch is that none of this is done at compile time, make sure everything is there, build, and the edit the ini file to do what you want.  This is the big sell against the CTN system we are using at the moment, ease of configuration and reconfiguration.


[PacsOne Server](http://www.pacsone.net/index.htm?)

PacsOne is one of those packages you look at and on the surface appears to be perfect.  Until you read the fine print and realize that the 'basic' version is deliberately stripped of all the features you'd actually want and the Premium Edition has all the major features people would be looking for to not actually go mad setting up their servers.  It's also the only one that's completely up to date as the basic system doesn't work with MySQL past version 4.0.x and is only available for windows.  Needless to say this was abandon early on in the search for a possible solution.

ClearCanvas:

Like the PacsOne Basic server ClearCanvas is Windows only, which isn't very helpful when all your servers run CentOS.  However if we were running a windows server somewhere this is most likely the package we would run.  It's open source, has a clean front end, supports plugins, is available in both x86 and x64 flavors, a support community and has clear documentation on how to install.  However it requires MS SQL server and there doesn't seem to be a way around this, and that could be considered a major problem depending on what your trying to do (like how we would rather not run that..).

TLDR:  
It should be considered generally unsurprising that there are a large number of payfor professional solutions to this problem, that tends to be the case with solving most problems.  What was surprising was how few workable solutions we found for making things work for free.  That said the CTN worked for us for many years quite faithfully, and it appears that Conquest will present us with a path forward as the underlying OS changes (since CTN is no longer seeing updates).  We have also found that bringing CTN forward requires relatively few tweaks and is more of a problem of making sure the correct packages are installed than anything else.  I will be posting my bosses notes on how we got this to compile once I've compiled them and confirmed them.  Conquest is also a capable system and we got it up in very little time, and are tweaking configs now to set it up to our liking.  I'll post this as well after we've completed the configuration and testing.

Brass Tacks:  
While I've found a solution that seems to do exactly what I want it to do the overall field of choice seems to suffer from the fact that this is a rather niche service requirement.  The professional systems seem nice a sleek but feel like they suffer from being the root of an up-sell to the companies other products.  On the other hand the free stuff tends to be tool chests commercial software was built upon or a pile of code drawn together by one or two individuals to suit their specific needs.  This isn't necessarily bad but it makes the approaches very environment specific and the maintenance path somewhat shaky.  On the other hand, I have what I want and need and I can go about my work without writing too much code, so who am I to complain?
