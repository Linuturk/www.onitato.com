+++
title = "Deploying to Rackspace using salt-cloud"
date = "2014-02-11"
tags = [ "rackspace", "salt", "salt-cloud", "configuration management" ]
categories = ["tech"]
slug = "deploying-to-rackspace-using-salt-cloud"
description = "Deploying Rackspace Cloud servers using salt-cloud."
+++

These instructions should be a nice and easy start to deploying Rackspace Cloud servers using the [salt-cloud](https://github.com/saltstack/salt-cloud) tool. Just follow along exactly, and at the end you should have a fully functional salt-cloud deployment tool.

## Dependencies

I'm performing my installation on a Debian 7 (Wheezy) server, where my salt-master already exists. The following two commands should install salt-cloud, and all the necessary dependencies. This assumes you are already using the Python tool pip.

```bash
apt-get install sshpass
pip install salt-cloud apache-libcloud
```

## Configuration

Here are the configuration files we need to put in place. Replace the appropriate sections with your account information.

### /etc/salt/cloud.providers.d/rackspace.conf

```yaml
my-rackspace-config:
  # Set the location of the salt-master
  #
  minion:
    master: saltmaster.yourdomain.com

  # Configure Rackspace using the OpenStack plugin
  #
  identity_url: 'https://identity.api.rackspacecloud.com/v2.0/tokens'
  compute_name: cloudServersOpenStack
  protocol: ipv4

  # Set the compute region:
  #
  compute_region: DFW

  # Configure Rackspace authentication credentials
  #
  user: username
  tenant: 123456
  apikey: xxxxxxxxxxxxxxxxxxxxxxxxxxxx

  provider: openstack
```

Be sure to replace the appropriate sections with your specific information:

* **my-rackspace-config** can be whatever label you want to use. Depending on your use case, it might make sense to identify specific regions by this name.
* **saltmaster.yourdomain.com** should be replaced with your salt-master's DNS name.
* **compute_region** should be set to the region where you want to deploy resources. Options include DFW, ORD, SYD, and IAD if you have a US Rackspace account.
* **user** should be the username associated with your account.
* **tenant** is your Rackspace Account Number. This can be found at the top, right of your [Rackspace Control Panel](https://mycloud.rackspace.com).
* **apikey** can be found in the [Rackspace Control Panel](https://mycloud.rackspace.com) as well. Just go to your Account Settings and look for the API Key.

### /etc/salt/cloud.profiles.d/openstack.conf

Here you define the different server profiles. These will determine options such as server size and operating system. Here's mine:

```yaml
openstack_512:
  provider: my-rackspace-config
  size: 512MB Standard Instance
  image: Debian 7 (Wheezy)
```

To see a listing of available sizes and instances, run the following commands. Make sure your provider file is in place, or this won't work.

```bash
salt-cloud --list-sizes=my-rackspace-config
salt-cloud --list-images=my-rackspace-config
```

## Deployment

Now, let's deploy a test instance of the server we just defined.

```bash
salt-cloud -p openstack_512 testinstance
```

This should start outputting information on the process. The longest wait in this process will be the server's build. Once it completes, you'll see the output of salt-cloud logging into the server and running various commands to bootstrap the system. At the end, you should see output similar to the following:

```yaml
testinstance:
    ----------
    _uuid:
        None
    driver:
    extra:
        ----------
        created:
            2013-08-22T20:00:50Z
        flavorId:
            2
        hostId:
            
        imageId:
            23b564c9-c3e6-49f9-bc68-86c7a9ab5018
        key_name:
            None
        metadata:
            ----------
        password:
            sosecret
        tenantId:
            123456
        updated:
            2013-08-22T20:00:50Z
        uri:
            https://iad.servers.api.rackspacecloud.com/v2/123456/servers/UUID
    id:
        UUID
    image:
        None
    name:
        testinstance
    private_ips:
        - 10.x.x.x
    public_ips:
        - 2001:
        - x.x.x.x
    size:
        None
    state:
        3
```

To delete this test instance, just run the following command. It will prompt for confirmation before actually deleting the instance.

```bash
salt-cloud -d testinstance
```

As you can see, this makes spinning up resources using SaltStack very easy, and automatically ties these new resources into your salt-master. Now go populate your profiles, and also checkout [maps](https://salt-cloud.readthedocs.org/en/latest/topics/map.html) to automate the deployment of many machines at once.

## References

The salt-cloud documentation was crucial to putting together this article:

* [Install Salt Cloud](https://salt-cloud.readthedocs.org/en/latest/topics/install/index.html#using-easy-install-to-install-salt-cloud)
* [Getting Started With Rackspace](https://salt-cloud.readthedocs.org/en/latest/topics/rackspace.html)
