+++
title = "Connecting to IRC"
date = "2012-11-27"
tags = [ "irc", "tutorial" ]
topics = [ "tech" ]
slug = "connecting-to-irc"
description = "IRC is easy."
+++

IRC stands for Internet Relay Chat. Here is the first paragraph from the Wikipedia article on [IRC](http://en.wikipedia.org/wiki/Internet_Relay_Chat):

> Internet Relay Chat (IRC) is a protocol for real-time Internet text messaging (chat) or synchronous conferencing. It is mainly designed for group communication in discussion forums, called channels, but also allows one-to-one communication via private message as well as chat and data transfer, including file sharing.

Connecting to an IRC server isn't hard. You just need the right IRC client, and a little bit of information.

## Choosing your Client

### One Size Fits All

Many popular chat clients already include the IRC protocol. If you are using one of these, you can connect without installing any additional software:

 * [Pidgin](http://pidgin.im/)
 * [Adium](http://adium.im/)
 * [Empathy](http://en.wikipedia.org/wiki/Empathy_(software))

If you aren't already using one of these clients, you might want to consider them. They allow you to connect to multiple chat networks, without the need for running multiple clients.

### Dedicated IRC Client

If you are like me, you want to separate a group chat experience from the one-on-one experience of other instant messenger clients. Here are some popular dedicated client choices:

 * [irssi](http://www.irssi.org/) - My preferred client.
 * [X-Chat](http://xchat.org/)
 * [mIRC](http://www.mirc.com/)

X-Chat or mIRC are good choices for Windows users and beginners.

## Gathering your Connection Information

To connect, you will need several pieces of information:

 * **Server** - You will need a server to connect to! There are many popular IRC networks out there. I run a channel on the [Freenode](http://freenode.net/) network. You would use the server name **irc.freenode.net** to connect to this network.
 * **Nickname** - You will also need to choose a **nickname** to identify yourself on this server. I use the nickname *Linuturk*. You will need to come up with your own.
 * **Channels** - Once you are connected to a server, you have to choose which channels to join. Channels are group chat sessions about a particular topic. You can join me on Freenode in the channel **#onitato**. There are also many other popular channels, like **##linux** and **#ubuntu**.

Once you have this information, you need to know where to put this information for your specific client. Please see the documentation for the client you chose. It should describe the process in detail.

## I'm Connected, Now What?

After you have successfully connected to a server, the first thing you need to do is register your nickname with the IRC Services. This will ensure no one else can use your nickname without knowing your password. To do this we will have to send commands to a special nickname on the server. There are two bots on a typical IRC server that you can work with: **ChanServ** and **NickServ**.

### Working with Bots

Bots are automated systems that you send commands to accomplish tasks.

 * **ChanServ** is responsible for channel operations, such as registering channels and performing other administrative tasks.
 * **NickServ** is responsible for nickname operations, including registering and protecting your chosen nickname. This should be the first bot you interact with when connecting to a server.

You can send commands to these bots by sending them a private message. Private messages work for bots, and other users on the server (depending on the configuration). Every private message begins with the "/msg" command.

On the popular Freenode network, use the following format to register your nickname:

> Syntax: REGISTER <password> <email-address>

For example, **"/msg NickServ REGISTER SecretPassword email@address.com"**.

Now that your nickname is registered, be sure to update your client to use this password when it connects to this server. You have to identify with NickServ when you connect using this username. For example, **"/msg NickServ IDENTIFY SecretPassword"**.

Bots are powerful tools and all of their features can't be discussed in one article. To see the full command list for a bot, and to get additional help for these tools, run the following command:

> /msg BotName help

On most networks, that will output a listing of commands and short descriptions of their use.

## Join a Channel

Now that you are identified with NickServ on your IRC server, you can join a channel! Just type "/join #channelname". A new tab or window should open up, and you will be in the channel and ready to chat. Congratulations, you are using IRC!
