Title: Send Email for yum-cron Update
Status: draft
Tags: email, yum, yum-cron, yum-updatesd
Category: tutorial
Slug: send-email-for-yum-cron-update
Author: Justin Phelps
Summary: When using yum-cron, you might want to receive email notifications when updates are applied. Here is how you enable these notifications for CentOS.

When using yum-cron, you might want to receive email notifications when updates are applied. Here is how you enable these notifications for CentOS. This article assumes a properly configured mail service.

## Installing yum-cron

Install yum-cron using the yum package manager:

```bash
yum install yum-cron
```

## Configure yum-cron

Modify the **/etc/sysconfig/yum-cron** file and add your email address to the **MAILTO** line.

```bash
MAILTO=email@address.com
```

Be sure to read up on the other settings in this file. You can disable automatic updates and only have the system send the notification.

## Start yum-cron

Start the service, and enable it to automatically start on system boot.

```bash
chkconfig yum-cron on
service yum-cron start
```

That's all you need to do. If you don't receive an email, make sure your mail daemon is configured and working properly.
