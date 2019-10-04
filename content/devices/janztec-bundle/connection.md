---
title: Connecting to Cumulocity
layout: redirect
weight: 30
---
### Find the serial number

Run the following command to find out the serial number of your device:

```shell
$ grep Serial /proc/cpuinfo
Serial          : 000000001955c218
```

### Register and connect to Cumulocity

To connect your device to the Cumulocity platform, you first need to register it in your Cumulocity account.

Follow the instructions in [Device Management > Connecting devices](/guides/users-guide/device-management#connecting-devices) in the User guide to register and connect your device.

After connecting your device, you can for example remotely monitor the memory usage and system load of your device in the **Measurement** tab of the device or troubleshoot your device in the **Log** tab, see [Device Management > Device Details](/guides/users-guide/device-management#device-details) in the User guide.  