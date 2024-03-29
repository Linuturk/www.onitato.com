+++
title = "Running a Wesnoth Server"
date = "2012-12-08"
tags = ["fedora", "multiplayer", "tutorial", "wesnoth", "wesnoth-server"]
topics = ["tech"]
slug = "running-a-wesnoth-server"
description = "Play together."
+++

[The Battle for Wesnoth](http://www.wesnoth.org/) is a turn based strategy game that has unique and fun campaigns and great multiplayer maps. Playing on the official server is fun, but sometimes you'll want a private server on which you and your close friends can play.

![The Battle for Wesnoth](/images/wesnoth_logo.jpg)

# Installing the Server Software

Most popular Linux distributions have the **wesnoth-server** package available in their repositories. For this example, I'll be installing this service on a machine running Fedora 17. To install the Wesnoth multiplayer service, run the following command as root on your machine.

```bash
yum -y install wesnoth-server
```

**yum** is the name of the package manager for Fedora. It manages the software that is installed on your computer. The **-y** option tells yum that you say yes to any questions it will ask. The **install** portion of the command tells it to install the next argument **wesnoth-server**, which is the software package name. The necessary software should be downloaded and installed automatically.

# Configuring and Starting the Service

Now that the service is installed, it is time to configure it to start when the server boots, and make sure users can access it through your firewall. You are running a firewall, right? To have this service start on boot with Fedora, run the following command.

```bash
systemctl enable wesnothd
```

Systemctl is the replacement for the chkconfig and service utilities, and is used for controlling various aspects of your system. The enable command tells systemctl to enable the wesnothd service to start on boot. Now, let's actually start the service.

```bash
systemctl start wesnothd
```

Similar to the last command, we are now telling systemctl to start the wesnothd service. Now let's figure out what port this service is running on so we can open the firewall.

# Opening the Firewall

Now we will use the **netstat** command to determine on which IP and port the wesnothd service is listening.

```bash
netstat -tulnp
```

You should see a line similar to the following in your output:

```bash
tcp        0      0 0.0.0.0:15000           0.0.0.0:*               LISTEN      3151/wesnothd
```

As you can see, the wesnothd service is listening for traffic on any IP and port 15000. This is the port we will need to open in the firewall. We will need to edit the file **/etc/sysconfig/iptables** and restart the iptables service. Add the following to this file using your favorite text editor. This text should go at the end of the other INPUT statements.

```text
-A INPUT -m state --state NEW -m tcp -p tcp --dport 15000 -j ACCEPT
```

Now, restart the service by running the following:

```bash
systemctl restart iptables
```

Your server is now allowing traffic to the wesnothd service. Give your friends your server's IP address, and have fun!
