+++
title = "Deploying Ansible Tower using HEAT"
tags = [ "ansible", "tower", "heat", "hot", "template" ]
category = ["tech"]
slug = "deploying-ansible-tower-using-heat"
date = "2014-03-10"
description = "Try Ansible Tower using HEAT."
+++

Deploying Ansible Tower isn't hard, but automating a server build and triggering the installation lowers the barrier of entry for trying out Tower. This article will describe the HEAT Template I've created to automate this process.

# Anatomy of a HEAT Template

Templates are broken into several main sections. I'm going to describe each one of them so you fully understand the process. Follow along here: [Ansible Tower HEAT Template](https://github.com/rackspace-orchestration-templates/ansible-tower)

## Description and Version

It is important that the Version information you specify matches the HEAT version in use. The description should describe the overall goal of the template.

```yaml
heat_template_version: 2013-05-23

description: |
  A template that deploys an Ansible Tower node.
```

## Parameters

Parameters are inputs that make the template more flexible. They allow you to define dynamic portions of the configuration without having separate templates for different server sizes.

The parameters I define for the template are:

* Server Flavor (size)
* Server Name
* Key Name (for ssh access)
* HTTP location for the Ansible Tower installer.
* The folder name that is extracted from the tarball.
* Various password definitions for the installer to use.

```yaml
parameters:

  flavor:
    description: Rackspace Cloud Server flavor
    type: string
    default: 1GB Standard Instance
    constraints:
      - allowed_values:
        - 1GB Standard Instance
        - 2GB Standard Instance
        - 4GB Standard Instance
        - 8GB Standard Instance
        - 15GB Standard Instance
        - 30GB Standard Instance
        description: must be a valid Rackspace Cloud Server flavor.

  server_name:
    description: The instance name
    type: string
    default: ansible-tower

  key_name:
    description: Nova keypair name for ssh access to the server
    type: string

  ansible_tower_tarball:
    description: Location of the Ansible Tower installer
    type: string
    default: http://releases.ansible.com/ansible-tower/setup/ansible-tower-setup-latest.tar.gz

  ansible_release_folder:
    description: Folder name that is extracted from the installer
    type: string
    default: ansible-tower-setup-1.4.5

  ansible_admin_pass:
    default: password
    hidden: true
    description: Ansible admin password
    type: string
    constraints:
    - length:
        min: 1
        max: 41
      description: must be between 1 and 41 characters
    - allowed_pattern: "[a-zA-Z0-9]*"
      description : must contain only alphanumeric characters.

  postgres_admin_pass:
    default: AWsecret
    hidden: true
    description: Postgres admin password
    type: string
    constraints:
    - length:
        min: 1
        max: 41
      description: must be between 1 and 41 characters
    - allowed_pattern: "[a-zA-Z0-9]*"
      description : must contain only alphanumeric characters.

  rabbitmq_admin_pass:
    default: AWXbunnies
    hidden: true
    description: Postgres admin password
    type: string
    constraints:
    - length:
        min: 1
        max: 41
      description: must be between 1 and 41 characters
    - allowed_pattern: "[a-zA-Z0-9]*"
      description : must contain only alphanumeric characters.
```

## Resources

Resources are the actual compute, database, and load balancer resources required for your environment. In this specific case, I have a single resource (Rackspace Cloud Server) and some basic configuration defined in user_data. You'll also see variable definitions that reference the parameters we defined above.

Some useful things to know about the user_data section:

* All commands run in /root
* The result of these commands are typically logged in /root/cfn-userdata.log
* Commands like cd will actually change your working directory.
* Anything that exits non-zero will cause the deployment to fail.

Typically, you want to use these commands to bootstrap your server into a complete configuration management tool.

```yaml
resources:

  ansible_tower:
    type: "Rackspace::Cloud::Server"
    properties:
      key_name: { get_param: key_name }
      flavor: { get_param: flavor }
      image: Ubuntu 12.04 LTS (Precise Pangolin)
      name: { get_param: server_name }
      user_data:
        str_replace:
          template: |
            #!/bin/bash -v
            # Install dependencies
            apt-get install python-pip curl -y
            pip install ansible
            # Pull and extract the installer
            wget -ct0 %ansible_tower_tarball%
            tar xzf ansible-tower-setup-latest.tar.gz
            # Modify groupvars
            sed -i 's/pg_password: AWsecret/pg_password: %postgres_admin_pass%/' %ansible_release_folder%/group_vars/all
            sed -i 's/admin_password: password/admin_password: %ansible_admin_pass%/' %ansible_release_folder%/group_vars/all
            sed -i 's/rabbitmq_password: "AWXbunnies"/rabbitmq_password: "%rabbitmq_admin_pass%"/' %ansible_release_folder%/group_vars/all
            sed -i 's/httpd_server_name: localhost/httpd_server_name: %server_name%/' %ansible_release_folder%/group_vars/all
            sed -i 's/ - localhost/ - %server_name%/' %ansible_release_folder%/group_vars/all
            # Copy everything to working directory and install
            cd %ansible_release_folder%
            ./setup.sh
          params:
            "%ansible_tower_tarball%": { get_param: ansible_tower_tarball }
            "%ansible_release_folder%": { get_param: ansible_release_folder }
            "%ansible_admin_pass%": { get_param: ansible_admin_pass }
            "%postgres_admin_pass%": { get_param: postgres_admin_pass }
            "%rabbitmq_admin_pass%": { get_param: rabbitmq_admin_pass }
            "%server_name%": { get_param: server_name }
```

## Outputs

Outputs should contain information useful to the person deploying the template. This can include things like URL's to access resources and their associated credentials. You also should probably include IP address information as well.

```yaml
outputs:

  public_ip:
    value: { get_attr: [ ansible_tower, accessIPv4 ] }
    description: The public IP address of the server

  private_ip:
    value: { get_attr: [ ansible_tower, privateIPv4 ] }
    description: The private IP address of the server
```

# Ansible Tower

Ansible Tower is a solid graphical interface that gives you visibility into your Ansible jobs and a REST API. You currently get access to this with 10 nodes, for free. See [Ansible's Site](http://www.ansible.com/tower) for more information and pricing.
