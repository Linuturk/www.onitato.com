+++
title = "IRC Logging Bot"
date = "2014-02-11"
tags = ["irc", "pierc", "python", "logging"]
topics = ["tech"]
slug = "irc-logging-bot"
description = "Implement logging for your favorite IRC channels."
+++

*This article is in response to a [request](https://github.com/Linuturk/www.onitato.com/issues/3) by Ryan Jung. [Request](https://github.com/Linuturk/www.onitato.com/issues?state=open) your own article.*

One of the disadvantages of using IRC over another chat medium is the lack of logging while you aren't connected to the server. In this article, I will describe the process I used to implement logging for my favorite IRC channels.

## The Environment

[Pierc](https://github.com/classam/pierc) is my choice of logging bot for this article. It logs the contents of IRC channels to a MySQL instance, and presents an easy to use web interface.

We will need to install the following packages on Fedora to get started:

```bash
yum install httpd mysql mysql-server php php-mysql MySQL-python
```

Make sure you configure httpd and mysql to start on boot:

```bash
chkconfig httpd on
chkconfig mysqld on
```

Finally, we will need to setup an unprivileged user for pierc to run under:

```bash
useradd pierc
passwd pierc
```

Login as the pierc user, and let's begin the configuration.

## Pierc Logger

Installation and configuration instructions for Pierc can be found [here](http://classam.github.com/pierc/). I'm going to run through them at a higher level here.

1. Create a database for pierc to use. Create a limited user with full permissions on this new database, and jot down the account details for future reference.
1. Obtain the [latest copy](https://github.com/classam/pierc/tarball/master) and unpack this in the pierc user's home directory.
1. Copy the example configuration files (irc_config and mysql_config) and fill in the appropriate values.
1. Populate the database with the necessary tables by running the following command:

```bash
python pierc_db.py
```

## Pierc Web Interface

The downloaded package also includes a web folder that contains all the files necessary for the web interface. Copy this to your Apache Document Root. You will need to copy the *config.php.example* file to *config.php* and then modify the necessary values to connect to the MySQL database.

## Start Pierc

Start a *tmux* or *screen* session, and run the following command to start Pierc. You can then detach from your *tmux* or *screen* session, and Pierc will continue to run.

```bash
python pierc.py
```

You should see a new user join your IRC channels. This user will have the name you configured in irc_config.txt as **nick:**. That's your new bot, happily logging all the channel's messages to the database server. Browse to your server's web interface, and you should see the logs appear. Good Work!
