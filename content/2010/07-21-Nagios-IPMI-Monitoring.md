Title: Nagios IPMI Monitoring
Date: 2010-07-21
Slug: Nagios-IPMI-Monitoring
Category: Sysadmin
Tags: Nagios, Monitoring, IPMI, Python

Anyone that's familiar with Nagios knows that there are certain things it can do very well and other things it tends to be.. lacking on.  IPMI is one of those ones that gets a bit complicated, there are a few different packages out there for doing it but none of them really do what you want them to do for integrating into the way Nagios 'thinks'.

There are a few reasons for this, mostly tied to the way that traditional IPMI software interfaces 'think'.  They are configured for direct monitoring and notification instead of integration into bigger systems.  This poses a major problem for the nagios integration which is direct query based.  However there's a newish toolbox with a few commands that turn that on it's head.  This package is the FreeIPMI package which provides the command ipmi-sensors which allows the dumping of all sensors and the ability to ask for specific sensor numbers.  Based on this information we wrote a new IPMI handler for Nagios that lets us request the status of specific sensors and import that status straight into Nagios.  This file is 'check_ipmi.py' (cleverly named, i know) and is available on the PNI toolbox repository [here.](https://gist.github.com/Wildcarde/293dec367f4e4419b511)

Other than python the only thing this command needs to work is for FreeIPMI to be installed.  This doesn't however get you all the way done, you need a bit of information before you can jump into the configuration of Nagios itself.  Specifically you need a list of the ID's and sensor names so you know what your monitoring.  You can dump this information by using the command.

`impi-sensors -h hostname -u username -p password`

This will dump a large amount of information onto your screen that should look like.

> (this is a partial sensor list for a Sunfire X2200)  
 640: CPU 0 Temp (Temperature): 40.00 C (NA/95.00): [OK]  
 704: CPU 1 Temp (Temperature): 41.00 C (NA/95.00): [OK]  
 768: Ambient Temp0 (Temperature): 36.00 C (NA/75.00): [OK]  
 832: Ambient Temp1 (Temperature): 41.00 C (NA/75.00): [OK]  
 1632: CPU0 DIMM0 (Memory): [OK]  
 1680: CPU0 DIMM1 (Memory): [OK]  
 1728: CPU0 DIMM2 (Memory): [OK]  
 2400: POST Error (System Firmware): [Unknown]  
 2448: Eventlog (Event Logging Disabled): [OK]  
 2496: System Event (System Event): [OK]  
 2544: Critical INT (Critical Interrupt): [OK]  
 2592: Watchdog (Watchdog 2): [OK]  

By default the command will assume the 'good' result for any given sensor is '[OK]'.  This can be overridden however.  You can also request several sensors simultaneously if you so choose.

So, all that's left is to configure your host listings, services and commands to set everything up now.

Here's my command configurations (a bit stripped down looking as I've lifted them from the configuration pane on the nagios front end):

`check_ipmi $USER1$/check_ipmi.py -n $_HOSTIPMIADDRESS$ -s $ARG1$
check_ipmi_with_expect $USER1$/check_ipmi.py -n $_HOSTIPMIADDRESS$ -s $ARG1$ -e $ARG2$`

There are two things to note, one two commands have been specified, you could do a single command I suppose but this seemed cleaner to me.  The `$_HOSTIPMIADDRESS$` is a variable defined in the host's definition to allow a second IP address to be associated with the host (see the [nagios documentation](http://nagios.sourceforge.net/docs/3_0/customobjectvars.html)) for how to do this.

Followed by the service definitions (also lifted from the configuration pane):

> Node0 CPU 2 Overtemp check_ipmi!122
 Node0 CPU 2 Status check_ipmi_with_expect!41!'[Processor Presence detected]'

These are lifted from Node0 of a storage cluster of IBM servers, the magic numbers here are derived from a dump of those machines ipmi-sensors output.  Note the second one provides the expected 'good' responce for that particular sensor, anything besides that value being returned is treated as a failure.  These could easily be made to be treated as warning instead of critical alerts with a tweak to the python script being called.

TLDR:  
This system will allow you to directly collect stats on your hardware's built in sensors (assuming you have hardware sensors).  The sensors function tends to give you alot of the critical information you would need to have on your computer including device faults temperature issues and things of that nature.

Brass Tacks:  
I've run into two problems with the script so far.  The more annoying one is that sometimes the IPMI / BMC board sometimes goes out to lunch and stops responding for a few minutes and this will generate errors that are effectively meaningless.  The second is that it currently doesn't support the ipmi-chassis command which is entirely my fault as a result of time and other projects.  The ipmi-chassis system provides information on the current power status for the system so you could use Nagios's dependant services feature to prevent Nagios from generating errors for services from a server if that server is currently powered down (it would help if I could figure out how to use the dependant service feature of course...).  Due to the nature of IPMI it will still happily respond as long as there is wall power to the chassis as it runs even if the computer is not 'on' in the classic sense.
