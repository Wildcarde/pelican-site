Title: Using Dropbox in Windows to Automatically Sync Fixed Folders
Slug: Dropbox-sync-fixed-folders
Date: 2011-01-24
Category: Howto
Tags: Dropbox, Howto, Symlinks, Windows


Or, How to Seamlessly Backup All your Save Game Files

I thought I'd pass this on in the midst of everything else I'm doing as it hit me in an epiphany earlier this week.  In this demonstration I'm going to use my 'My Games' folder inside My Documents area for an example but this will work with any Directory you want to sync anywhere on your hard drive.

This is done using Vista/7's support for 'symbolic links', a feature that has been available for eons in the unix world.  This feature has some caveats in windows that are not present in the unix world however.  You can only create symbolic links to folders, not files.  Shortcuts to files work similarly, but I'm not sure they can be invoked seamlessly like a symbolic link (thou the help does claim it can make file symbolic links so there is something to it).  Also, you can not create symbolic links to or from network shares, even if they are mapped as a network drive, so what I'm discussing here would not work for backing things up to a SharePoint or Samba share for instance.  I'm not sure you would want to anyway, if you did, then this data would be unavailable when you are not on the correct network (or a network at all for that matter).

From here I'm going to assume you have DropBox installed already, and you've got a folder you want to exist everywhere, so lets get rolling.  First copy the folder you want to keep everywhere to a sensible location inside your DropBox area.  In my case I'm backing up my gaming information in the 'My Documents/My Games' folder for demonstration purposes.  In my DropBox area I added a 'Gaming' folder to my DropBox and copied the 'My Games' folder in it's entirety copied over to this location.  After this move the non DropBox folder aside (do not delete it until you've confirmed your in good shape, if at all).  I would also write out the 'Target' folder path and the full path for this location in your DropBox folder on a piece of paper for reference, you will need both full paths shortly.

After this you've got to bring up a standard old administrative empowered command line prompt (hit the windows key then type CMD and right click on `cmd.exe` selecting `Run as Administrator`).  From here on you'll need to utilize the `mklink` command provided in the path, this command is administrative privileged so please make sure you do start it up correctly to save some grief.  You can get a rundown of the function using `mklink /?` as well as in the provided link.  After this you can run from anywhere the following (adjusted as appropriate for what you wish to make a link from and to):

`mklink /D "c:/users//My Documents/My Games/" "c:/users//My Documents/My Dropbox/Gaming/My Games/"`

Now if you go back to your My Documents folder you'll see a folder icon with a shortcut type sub icon on it.  This indicates your in good shape and it should work fine at this point.

TLDR:  
This works surprisingly well with very little effort on your part individually.  Effectively it's doing exactly what you'd expect it to do without any massaging, which is awesome and pretty rare these days.  Now all you have to do is replicate this configuration on each computer with DropBox installed and your in good shape generally speaking.  I do notice a large number of files get updated when I play video games, and I'm not clear what the implications of this are for systems with drastically different capabilities (for say your games config files).  But all in all it works.

Brass Tacks:  
As to the caveat above in the 'generally speaking' comment, I haven't tested this extensively for video games and the like.  I have read that there are some implications with rapidly updating files and DropBox on the forums (I seem to have lost the link).  However DropBox seems to be of the opinion that corruption is impossible based on their open service logs so to each their own.  Also remember that DropBox is NOT a backup service, it is a sync service (an extremely chatty one from a networking standpoint).  You should still make sure you've got a backup of anything you put on there in case of some sort of corruption caused by either your own hardware or the service.
