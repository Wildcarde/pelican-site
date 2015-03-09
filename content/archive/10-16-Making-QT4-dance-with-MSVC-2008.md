Title: Making QT4 dance with MSVC 2008
Date: 2008-10-16
Slug: making-qt4-dance-with-msvc-2008
Category: Howto
Tag: howto, development, qt4, msvc


Anyone who's read my previous blog post will know that I've become keenly interested in cross platform development, not so much for my own benefit but to guarantee my software doesn't just sit around and stagnate because there's an arbitrary stigma applied to it.

As such, I've elected to use QT4OS (open-source) for my projects here at work.



One thing I can say is, QT4OS does work in MSVC2008. However I have not figure out a way to generate proper make files for the QT Qmake system. So the whole 'cross-platform' thing is still stuck in a bit of a rut on my end. However you can generate Visual studio projects from the Qmake compatible make files and compile / modify those projects in Visual Studio. Intellisense also works with the QT4 packages if you have the header files configured properly.

First, lets go with getting a copy of QT4 so that we can start moving forward. There's a few places to do this.

The default download for windows is located here(note this link will take you to the download page, I suggest downloading the MinGW included version). This version will also include all the demo's, including the demo explorer, which are really helpful for showcasing particular technologies and behaviors.


If you'd like the latest greatest published version, the development versions are available here.


OK, after you have the system downloaded, pick a location and install it. I installed mine at D:\QT\

I should preface everything that follows by saying what I'm about to tell you to do will take a massive amount of room up. My QT folder takes up 8.9GB due to the fact that I have the MinGW build, 32-bit MSVC build and 64-bit MSVC builds all co-exsisting in sub folders. Depending on your OS and hardware configuration this will be smaller (if for example you don't need the 64-bit build like I do).

After the directory is fully installed it's time to start making copies so we can compile the versions we are interested in. I'm working with version 4.4.3 so I copied the original version naming one folder 4.4.3x86 and a second folder 4.4.3x64 just to keep everything clear. This also allows you to build both of them without having to rebuild (something you really really don't want to do).

Next you must setup the environmental variables to reflect the settings that are necessary.

Specifically the the location of the new QT folders /bin must be added to the system PATH variable. This can be done in two ways either in the 'User Variables' or the 'System Variables'. I tend towards setting it in the user variables for clarity.

The location of the environmental variables is generally the same if your in XP or Vista. Open the control panel and go to the 'System' program. In System access the 'Advanced' tab and select 'Environmental Variables' at the bottom of the screen.

After that, restart the system. This needs to be done so that the Environmental Variables are all in play, if anyone knows another way to do this in windows let me know please, having to do this is maddening.

Ok, now that the files are all where you want them and the env vars are all setup. It's time to break out those good 'ole Dos skills, you know, dir, cd, the 2 everyone should know.

If you've never used it before your going to open up the 'Visual Studio 2008 Command Prompt'. This can be found in the Visual Studio folder in your start menu under 'Visual Studio Tools'. For those of you on an 64-bit machine you will have two separate consoles you can start, start one of each. The bit rate of the console dictates how QT is built so navigate the 64-bit version of the console to the root folder of your QT 64-bit build, and the 32-bit version to the location of your 32-bit build.

After you've navigated to the root of each of the build sites you'd like to setup the following command will get you started.

configure -platform win32-msvc2008

This is correct for both the 32-bit and 64-bit versions, it's a legacy thing. Stupid, but a legacy thing.

This command is going to take some time to run (like 10 minutes or so).

Afterwards in each console type the command 'nmake'. This runs Microsofts make function, yes even MS has one.

This will take hours, go watch a movie, take a somone to dinner or go exercising. If anybody complains, show them this from the ever hilarious XKCD.


Once this is all done your going to need to actually configure visual studio to make it all come together. This is going to require a few quick configurations and compiling should be setup.

These configuration options can be found by loading up Visual Studio and navigating to Tools-&gt;Options.

In here you'll want to navigate to 'Projects and Solutions' then on to the 'VC++ Directories' sub heading.

From here there's a few things you need to do. Specifically you must configure the locations of the \bin, \include, \lib, \src. (include,lib and src pictured below).


A few things to catch here, I've highlighted three things. One the location all this setup starts at 'VC++ Directories'. After that there's the platform listing. If your using a 64-bit system you'll have to set this up twice, once for the Win32 Platform, and a second time x64 Platform. All that must be configured is an entry in the 'include' area pointing to the appropriate include folder on your hard drives. For the more advanced users you could substitute the very definite D:\QT\ with an environmental variable (storing much the same value), or even separate ones for each platform so it's easier to replace them with newer versions latter. Don't forget to make sure your putting the x86 includes and such under the Win32 Platform listing and the x86-64 (x64) under the x64 platform listing. If you don't get this right, your programs will compile but when attempting to link will fail (you can't link a 32-bit app to a 64-bit library).


Don't forget to add the Library Files as well, this will let VC++ linking work properly for projects being built inside the studio IDE.



Finally configure the \src directory, this will make sure you have access to the actual functiono definitions your working with. This is important for when you do things like right clicking on a function or object and selecting the 'browse to definition' option to review the actual implementation code.

At this point if you try to build a project it may or may not work depending on how you attempt to build it.

For a quick example, I created a completely empty C++ project using the 'New Project' command and simply selecting to make a empty project. After that I dumped a little example code into it:

This probably will not run if you try to run it right now. This is because your missing one final piece of the puzzle that brings it all together (however at this point intellisense should work).



This last piece is to tell the project's linker you need the specific lib files in question. The ones I'm going to list here is what I've been using for all my testing because it seems to cover the full gamut of things that are being used for the example programs. You'll have to decide which ones are appropriate for your project on a project by project basis but these will get most if not all of the examples up and running. Remember the below listing is my 'Cover All Bases / Quick and Dirty' approach for the examples, and shouldn't be used for anything more than getting you rolling, after which take out the ones you don't need so as not to bloat the linking on system.

To modify the linker right click on your projects title and select "Properties". This will open the Project properties page, at which point you need to navigate to "Configuration Properties -&gt; Linker -&gt; Input". Once here you must modify the additional dependencies, which you can either do as a space separated list or my preferred way by opening the dialog box and editing them as line items.



My listings for the win32 (Debug) platform are as follows:
opengl32.lib
glu32.lib
gdi32.lib
user32.lib
D:\Qt\4.4.3x86\lib\Qtmain.lib
D:\Qt\4.4.3x86\lib\QtSvg4.lib
D:\Qt\4.4.3x86\lib\QtOpenGL4.lib
D:\Qt\4.4.3x86\lib\QtGui4.lib
D:\Qt\4.4.3x86\lib\QtCore4.lib

It is important to not you have a number of choices on how to populate these lists, including using separate lib files for each platform (recommended if you want it to work). As well as separate libs for Debug and Release builds (or any other builds you care to use). This allows a significant level of flexibility, but also introduces a rather large level of overhead in managing the lib connections. If anyone knows a better way to do this, again PLEASE let me know I hate doing all this stuff in 12-step format.

TLDR:
For people looking to toy with QT this is all you should need to do to get up and running. You'll be able to build MSVC projects against QT and compile the example programs form their project files (these project files are generated by running the command 'qmake -tp vc -spec win32-msvc2008' in the root of the demo of interest (using the visual studio console). And that's all you have to do. It's a bit time consuming but it gets QT4 up and running happily native to MSVC.

Brass Tacks:
This of course has a few holes in it. First QT4 like all versions of QT likes using it's own make system called qmake, so that you don't have to write multiple make files for each you wish to work on. Also it doesn't allow you to design UI's inside the Visual Studio system, instead requiring you to use the QT Designer program to generate the .ui files. These caveats aren't terribly huge problems until programs get larger or are building on many different systems. I'm currently trying to locate a solid reliable way to generate make files either directly via Visual Studio, or from the Visual Studio project files so that I can build in Mac and Linux environments. The 'makefile project' file give me some hope as you can even tell it to use the qmake command when building, but I've yet to track down how everything there is supposed to work. Once I've solved that, it will be posted here as well.

Update: If you use the 'QT' label to show all articles pertaining the QT programming, you will see a new 'Part 2' article. This article discusses the VSaddin that allows you to more easily integrate QT and Visual Studio. You will still need the above instructions for building against the MSVC compilers however.

Update 2: Anyone that has tried to use these instructions for 4.5 or 4.6 will notice they do not work due to a compilation error. I've written a new blog update that explains what to do located here.
