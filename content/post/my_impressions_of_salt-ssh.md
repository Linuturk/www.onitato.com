+++
title = "My Impressions of salt-ssh"
tags = ["saltstack", "salt-ssh", "opinion"]
topics = ["impressions"]
slug = "impressions-of-salt-ssh"
date = "2015-12-11"
description = "Why aren't you Ansible?"
+++

I've done a search and there seem to be a large number of issues related to salt-ssh usability with non-root users. I'd like to understand more about the perceived use case from Salt's perspective and give some feedback.

## Perceived use case
salt-ssh seems to be an answer to Ansible and Fabric where the ssh transport from a single laptop is useful for a system administrator to maintain a smaller set of infrastructure. My use case would be running from a virtualenv after pip installing salt-ssh. I would typically create a folder for a set of infrastructure and states. If I was executing the command from this directory I expect salt-ssh to look in this working directory for things like rosters and configuration files. The next place would be a folder `~/.salt-ssh` folder in my home directory. I would expect cache directories to be automatically created in that location. The final location would be the system wide settings in `/etc/salt`.

## Ideal workflow
The salt-ssh command should just work given the following actions on my part:
 1. Create a virtualenv and pip install salt-ssh
 1. Activate the virtualenv
 1. Make and change into a working directory.
 1. Create a roster file with the hosts I want to manage.
 1. A command like `salt-ssh "*" test.ping` should work without any further configurations assuming ssh keys are in place. (which brings me to my next point.)

## SSH Configuration
Another expectation on my part was that salt-ssh would make use of my existing `~/.ssh/config` configuration to connect to the various hosts in my roster. That includes pre-existing ssh keys, SSH proxy through a configured bastion, usernames, ports, and other settings allowed in this configuration file.

The auto creation of an ssh key is admirable for someone that hasn't used keys before but re-keying all my servers would be annoying. salt-ssh should try to detect existing keys in their default locations and only offer to generate one if it can't find a key.

## Saltfile
This line from the [documentation](https://docs.saltstack.com/en/latest/topics/ssh/#define-cli-options-with-saltfile) concerns me as well:

`The option keys specified must match the destination attributes for the options specified in the parser salt.utils.parsers.SaltSSHOptionParser.`

At the very least the documentation should link or document the config file parameters so we don't have to dig through the code to find them.

The options specified should either:
 1. Be fully documented in the code,
 1. Match the command line parameters, or
 1. Document the alternative names in the help text of `salt-ssh -h`.

## Ultimately...
the goal is to make it as easy as possible for me to go from 0 to salt-ssh with the smallest amount of pain possible. A confusing use case, complicated installation and configuration, ignoring existing SSH configurations, and undocumented options in `Saltfile` make this unnecessarily complicated.

## Another Use Case
If the goal of `salt-ssh` is to simply be an alternative transport for the existing use case of the `salt` command then my points are invalid. If we want to give users an easier introduction into SaltStack and lower the barrier to entry I think these changes are valid and necessary.
