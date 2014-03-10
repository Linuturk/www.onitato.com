Title: Deploying Ansible Tower using HEAT
Status: draft
Tags: ansible, tower, heat, hot, template
Category: tutorial
Slug: deploying-ansible-tower-using-heat
Author: Justin Phelps
Date: 2014-03-10 0:00
Summary: Deploying Ansible Tower isn't hard, but automating a server build and triggering the installation lowers the barrier of entry for trying out Tower. Here are the steps necessary for deploying Ansible Tower using a HEAT template I created.

Deploying Ansible Tower isn't hard, but automating a server build and triggering the installation lowers the barrier of entry for trying out Tower. Here are the steps necessary for deploying Ansible Tower using a HEAT template I created.

#Anatomy of a HEAT Template

Templates are broken into several main sections. I'm going to describe each one of them so you fully understand the process.

##Description and Version

It is important that the Version information you specify matches the HEAT version in use. The description should describe the overall goal of the template.

```
heat_template_version: 2013-05-23

description: |
  A template that deploys an Ansible Tower node.
```
