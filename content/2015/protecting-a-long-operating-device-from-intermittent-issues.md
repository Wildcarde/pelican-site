Title: Protecting a Long Running Data Collection Device
Date:
Slug: protecting-long-operating-device-from-intermittent-issues
Category: Sysadmin
Tags:
Status: draft

We acquired a new lab at work and with it several very expensive pieces of equipment.  One of these systems is an electron microscope that generates large blocks of data which must be transferred to our central file store so they can be processed by larger computational resources and be made available to the lab at large.  One of the challenges this device presents is that the act of collecting data is actually destructive to the sample in question, the local workstation also has a severely limited amount of storage available to the OS and general storage. The device is also run for stretches up to 6 months long at a time, pausing just long enough to change out samples one time per week. It's effectively a fountain of data generating about 1TB per month in it's current configuration.

One solution would be to mount the remote file system and stream the data directly to the central system, this solution presents some problems however.  Now downtimes of that shared resource are pinned to times when the EM microscope is down, and the scope is down if there is an unplanned outage on the file server.  While outages like this are rare, being able to easily maintain the file-system independent of what is arguably a free standing device is a must for security patching and system upgrades so this approach is a no go.
