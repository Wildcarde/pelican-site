Title: Windows 7 Workstation Configuration using Group Policies
Slug: Windows7-Workstation-Conf-GP
Date: 2010-06-20
Category: Sysadmin
Tags: Windows 7, Workstation, Sysadmin, Group Policy

As some of you may be aware, the old Beta's of Windows 7 had a feature included for user profiles called 'Guest Mode'. This was a sand boxing technology based on the 'Windows Steady State' software that has been available for a while for XP and Vista. Sadly, it was removed from the RC and RTM versions of the OS with no clear reason why and to the disappointment of a number of users (there is also no idication that Steady State is slated to make a Win 7 appearance). The main reason it was unfortunate to see it go was that this sand boxing allowed you to construct a workstation that behaved like a dynamic kiosk effectively. The idea being any changes made to the OS were never actually committed to the OS so even if your users did 'Very Bad Things' (TM) the log-off action would undo those bad things. This is great, it gives your users a wide range of freedom and you the peace of mind to know you won't have to unfuck a workstation every three days. But sadly, it's gone, which means we need to walk a grittier path to get the result we want (and really, we still won't get there...).

At first glance it would appear that what we are looking for is the Local Group Policy editor. This is not necessarily the case. This tool, invoked by typing gpedit.msc into the start menu has all the settings we could ever want to manipulate.  However, it applies those manipulations to everyone on the computer, which isn't terribly helpful when all of a sudden you've incapacitated yourself (and possibly disabled your machine in the 'now you need to wipe the OS' sort of way).  While this isn't good for a workstation it does let you install some handy tweaks on your system (quickbar anyone?).


gpedit.msc, this is what you don't want.

So how do we setup group policies on a computer without incapacitating ourselves in the process? Instead use 'Run' and type in 'mmc', this brings up the Microsoft Management Console, a customizable interface for tweaking well... everything.  In this case we are interested in adding two items to the console for working with.  To do this just hit 'Ctrl+M', or use the add command in the 'File' menu.  This will bring up the 'Add or Remove Snap-ins' window where you can bring in the editors we are interested in here.  Under the 'Available snap-ins' find the 'Group Policy Object Editor', highlight it and select 'Add'.


Group Policy Object Editor Wizard
Select 'Browse' and change 'Local Computer' to the 'Non-Administrators' group under the 'Users' tab in the resultant menu.  Do this again but selecting 'Administrators' this time.  If you've done it right you should have a window like the following.


MMC with Addins Configured

At this point any changes made to the 'Non-Administrators' entry will change settings for anyone without Admin privileges associated with their ID.  This isn't a perfect solution but it will let you lock down some of the more annoying habits of the average user.

TLDR:
This works pretty well for locking a system down.  It can even do things like blocking a system from allowing USB memory sticks if your concerned about that level of security.  You can impose pasword update / lockout requirements for the system to tighten it down even further.  It also lets you replace 'explorer.exe' with alternative gui environments which is useful if you want to make a console of some nature (a custom Rainmeter interface perhaps?).

Brass Tacks:
The big fail that I see in this setup is that it's restricted to only Administrator / Non-Administrator sub divisions.  You can't make a smaller group of users that are really locked down, some high level users and then a full access option.  Asside from that the fact that there is no proper way to import / export the policies is problematic (even getting a printable log of the policies requires logging in as the given user and using a command line tool).  I believe you can just copy the policy file that is generated but this is fairly clunky, this means setting up several computers with restricitions can become a chore quickly.  My understading is that a full fledged active directory server can fix these complaints but I'm not intimately familiar with that technology so I won't speak to it here.