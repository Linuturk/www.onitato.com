+++
title = "Ansible's Rackspace Dynamic Inventory Plugin"
date = "2014-02-18"
tags = [ "rackspace", "ansible", "inventory", "plugin" ]
categories = [ "tech" ]
slug = "ansible-rackspace-dynamic-inventory"
description = "The Rackspace dynamic inventory plugin is a powerful tool."
+++

# How do I install it?

Installing inventory plugins isn't intuitive, and the documentation available on this process isn't immediately clear. The instructions found on this page [Ansible Documentation](http://docs.ansible.com/intro_dynamic_inventory.html) can be adapted for the Rackspace plugin.

It boils down to this for the Rackspace plugin:

1. Grab the latest version of rax.py from the plugins/inventory folder on GitHub. [Raw GitHub Link](https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/rax.py)
1. Place this file on your Ansible master. The location doesn't matter that much, but convention says to put it in /etc/ansible/rax.py.
1. Make this script executable by issuing **chmod +x /etc/ansible/rax.py**.
1. As the user that runs Ansible, create the following file at *~/.rackspace_cloud_credentials*: (Be sure to replace the appropriate values with your Rackspace username and apikey.)

```Ini
[rackspace_cloud]
username = my_username
api_key = 01234567890abcdef
```

Target the rax.py script in your ansible run: **ansible -i /etc/ansible/rax.py webserver -m ping**

Now your inventory is dynamic using Rackspace!
