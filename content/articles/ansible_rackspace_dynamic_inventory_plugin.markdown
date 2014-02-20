Title: Ansible's Rackspace Dynamic Inventory Plugin
Date: 2014-2-18 0:00
Tags: rackspace, ansible, inventory, plugin
Category: Rackspace
Slug: ansible-rackspace-dynamic-inventory
Author: Justin Phelps
Summary: The Rackspace dynamic inventory plugin is a powerful tool, but the use of this plugin isn't well documented. Here's a quick tutorial on how to get started with this plugin.

#How do I install it?

Installing inventory plugins isn't intuitive, and the documentation available on this process isn't immediately clear. The instructions found on this page [Ansible Documentation](http://docs.ansible.com/intro_dynamic_inventory.html) can be adapted for the Rackspace plugin.

It boils down to this for the Rackspace plugin:

1. Grab the latest version of rax.py from the plugins/inventory folder on Github. [Raw Github Link](https://raw.github.com/ansible/ansible/devel/plugins/inventory/rax.py)
1. Place this file on your Ansible master. The location doesn't matter that much, but convention says to put it in /etc/ansible/rax.py.
1. Make this script executable by issuing **chmod +x /etc/ansible/rax.py**.
1. As the user that runs Ansible, create the following file at *~/.rackspace_cloud_credentials*:(Be sure to replace the appropriate values with your Rackspace username and apikey.)
```
[rackspace_cloud]
username = my_username
api_key = 01234567890abcdef
```

Target the rax.py script in your ansible run: **ansible -i /etc/ansible/rax.py webserver -m ping**

Now your inventory is dynamic using Rackspace!
