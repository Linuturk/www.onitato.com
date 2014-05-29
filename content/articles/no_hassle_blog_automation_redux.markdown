Title: No Hassle Blog Automation Redux
Tags: drone, pelican, jenkins, blog, automation
Category: tutorial
Slug: no-hassle-blog-automation-redux
Author: Justin Phelps
Date: 2014-05-29 0:00
Summary: Due to the difficulty in maintaining a full Jenkins instance, I have revisited the blog automation issue and have replaced Jenkins with Drone.

Due to the difficulty in maintaining a full Jenkins instance, I have revisited the blog automation issue and have replaced Jenkins with Drone. Making use of a tool like Drone greatly simplifies the setup process and lowers the barrier of entry for this type of project.

## Requirements

There are a few requirements for this setup:

* Rackspace Cloud Account
* Existing Pelican Blog
* Github Account
* Linux Administration Knowledge

You should also read my [original article](|filename|/articles/no_hassle_blog_automation.markdown).

## Drone

There are two options here for using Drone.

#### Drone.io

Register a free account at [Drone.io](https://drone.io/).

Using Drone.io's free service has some disadvantages. You can't specify custom docker images for your testing. There also isn't a direct method to publish your blog output to Rackspace Cloud Files. I recommend you make use of the second option and run your own instance.

#### Open Source Drone

Run your own Drone instance using my [Ansible Drone Role](https://github.com/rack-roles/drone). Some key points of this setup include:

* The use of the undocumented *$DRONE_BUILD_DIR* environmental variable. This is the working directory where the git checkout is placed.
* The use of parameters {{rax_username}} and {{rax_apikey}}. You define these in your Drone instance settings. This feature allows you to keep secrets secure.
* Make sure the container you define is published to the CDN, and is enabled to serve as a Web Site. You can now enable this through the Rackspace Cloud Control Panel.

Documentation and install instructions are available on [Drone's Github Page](https://github.com/drone/drone#getting-started). You can follow these instructions if you are unfamiliar with Ansible.

## Docker

I maintain a Trusted Build in the Docker Registry for Pelican. The image name is [linuturk/ubuntu-pelican](https://index.docker.io/u/linuturk/ubuntu-pelican/). We will be using this image to simplify our .drone.yml.

Remember, if you are using the free account provided by Drone.io, you won't be able to use this image.

## .drone.yml

This file is used by the open source Drone.io to define the build process. You can find my current .drone.yml file [in my repository.](https://github.com/Linuturk/www.onitato.com/blob/master/.drone.yml)

```yaml
image: linuturk/ubuntu-pelican
script:
  - make -C $DRONE_BUILD_DIR html
publish:
  swift:
    username: {{rax_username}}
    password: {{rax_apikey}}
    auth_url: https://identity.api.rackspacecloud.com/v2.0
    region: ORD
    container: www.onitato.com
    source: $DRONE_BUILD_DIR/output
    branch: master
```

There are three main sections to this file:

* **image**: This defines the Docker image to use for the build.
* **script**: This defines the commands to run for the build process.
* **publish**: This is set to publish the contents of the output directory to Rackspace Cloud Files.

The only options you should have to change for your deployment are *region* and *container*.

## Setup

Here is a high level overview of the setup steps:

1. Create a container in Cloud Files, and make sure you configure the Website Settings and ensure it is published to the CDN.
1. Setup a DNS record for your domain to point to the CDN URL provided by Cloud Files.
1. Install and configure an instance of the open source Drone project.
1. Register your Drone instance with Github. Here's a [quick guide](http://drone.readthedocs.org/en/latest/setup.html#github).
1. Use the Drone web interface to add your repository to Drone. This process also automatically creates the necessary webhooks in Github.
1. Configure the necessary [Parameters](https://github.com/drone/drone#params-injection) for the swift publish option.
1. Add the .drone.yml file to your repository. Commit and push this change, and Github will notify Drone to process a build.
1. Review the build in the Drone web interface to ensure it was published successfully.

That should be all you need to do. Good luck!
