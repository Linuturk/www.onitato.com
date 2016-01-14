Title: Retrying Server Builds with Ansible
Status: draft
Tags: Rackspace, tutorial, ansible, retry
Category: Rackspace
Slug: retrying-server-builds-with-ansible
Author: Justin Phelps
Date: 2016-01-14 0:00
Summary: A common problem with building multiple servers in the cloud is an intermittent failure in one build that can stop your entire deployment process. With the right retry logic you can avoid this problem with Ansible.

A common problem with building multiple servers in the cloud is an intermittent failure in one build that can stop your entire deployment process. With the right retry logic you can avoid this problem with Ansible.

<script src="https://gist.github.com/Linuturk/2771d55e6304dbc14824.js"></script>

I'm using [until](http://docs.ansible.com/ansible/playbooks_loops.html#do-until-loops) to check the output from the rax module. Using the [length](http://jinja.pocoo.org/docs/dev/templates/#length) Jinja2 filter, I can check if the correct number of instances have been created. This should retry the task 3 times with a delay of 5 seconds between attempts.

I've built and destroyed between 1 and 100 servers in multiple regions and the Ansible playbook didn't bomb out once. Hopefully you won't have to deal with failed builds manually anymore.
