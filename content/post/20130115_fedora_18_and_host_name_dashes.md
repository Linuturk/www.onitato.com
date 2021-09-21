+++
title = "Fedora 18 and Host Name Dashes"
date = "2013-01-15 23:07:00"
tags = ["18", "dashes", "fedora", "hostname", "hostnamectl"]
topics = ["impressions"]
slug = "fedora-18-and-host-name-dashes"
description = "Annoying problem for sure."
+++

I ran into an interesting problem today when installing the newly released [Fedora 18](https://fedoraproject.org/). It was quite annoying, so I wanted to document it here.

![Fedora 18](/images/f18_screenshot.png)

Using the new installer, I configured my computer's host name to **subdomain.domain.com** on the network setup page. After I finished the installation, I noticed my host name was still the default **localhost.localdomain**. I tried the usual tricks to set the host name, but all the following tactics failed:

* **/etc/sysconfig/network** by setting **HOSTNAME=subdomain.domain.com**
* Using the **hostname subdomain.domain.com** command.
* Changing the **System Settings > Details > Device name** field.

I was able to get the host name set, but instead of **subdomain.domain.com**, the host name was displayed as **subdomain-domain-com**. No matter what I did, I couldn't get the correct host name.

It turns out, there's a new place to configure your host name in Fedora 18. Just edit the **/etc/hostname** file, add your host name, and restart your computer. Simple as that.

**Update:** Several readers have pointed out the **hostnamectl** utility. Using this tool, you can set the host name properly on a Fedora 18 system. The syntax for this change is:

> **hostnamectl set-hostname subdomain.domain.com**
