Title: No Hassle Blog Automation
Date: 2013-2-5 22:00
Tags: blog, rackspace, jenkins, pelican, git, github, cloudfiles
Category: tutorial
Slug: no-hassle-blog-automation
Author: Justin Phelps
Summary: Managing a blog can be a hassle. Operating system updates, blog software updates, and server security take up tons of time. Don't forget about scaling your blog if you get popular. Inspired by the Rackspace DevOps post -  http://devops.rackspace.com/the-new-devops-blog.html on their new blog format, I've setup my own version using Pelican - http://blog.getpelican.com/ instead of Octopress -  http://octopress.org/.

Managing a blog can be a hassle. Operating system updates, blog software updates, and server security take up tons of time. Don't forget about scaling your blog if you get popular. Inspired by the [Rackspace DevOps post](http://devops.rackspace.com/the-new-devops-blog.html) on their new blog format, I've setup my own version using [Pelican](http://blog.getpelican.com/) instead of [Octopress](http://octopress.org/).

## Resources

This tutorial will assume you have two systems to manage your blog.

 * Local Workstation
 * Remote Server

The local workstation will be used to manage your blog posts, as well as uploading the content. This system will need git and Pelican installed.

The remote server will be used to generate and upload the HTML for your blog. This system will need git, Pelican, Jenkins, and pyrax installed.

## The Tools

Let's take a look at the tools we will need to automate our blog:

 * [git](http://git-scm.com/)
 * [Pelican](http://blog.getpelican.com/)
 * [Jenkins](http://jenkins-ci.org/)
 * [Github](https://github.com/)
 * [pyrax](http://docs.rackspace.com/sdks/guide/content/python.html)
 * [Rackspace Cloud Files](http://www.rackspace.com/cloud/files/)

Now I'm going to detail out the setup instructions for each tool.

### git

We are going to use git to provide a method of version control for our blog posts. In addition, we will be pushing our code to Github.com. A full git tutorial is outside the scope of this post. If you need a crash course in git, checkout this [awesome tutorial](http://try.github.com/).

Installing git should be fairly simple. Instructions for various operating systems can be found [here](http://git-scm.com/downloads). Install this on your local workstation and remote server.

### Pelican

Installing Pelican is simple assuming you have pip available on your system. I've found the following method best for installing both pip and pelican. If you don't have access to the **easy_install** command, try finding the **python-setuptools** package in your repositories.

Do this for your local workstation, as well as your remote server.
```python
easy_install pip
pip install pelican Markdown
```

Once you have this installed on your local workstation, you need to generate the necessary files using **pelican-quickstart**. You will need to run this in the git repository we clone from Github. I highly recommend the [Pelican Quick Start Documentation](http://docs.getpelican.com/en/3.1.1/getting_started.html) to help you with the details of configuring Pelican.

**Note:** Do not generate your html on your local workstation. We are going to configure Jenkins to do this for us automatically on the remote server. No need to clutter our git repository with this output.

### Jenkins

#### Installation

Jenkins will need to be installed on the remote server only. Installation instructions for Jenkins can be found [here](http://jenkins-ci.org/). Check the right side of the page for your operating system. I chose CentOS 6.3 for my Jenkins server.

After installtion, be sure your service starts on boot and your firewall configuration has port 8080 open.

#### Security

I highly recommend enabling Security for your Jenkins instance. There is an [existing page](https://wiki.jenkins-ci.org/display/JENKINS/Standard+Security+Setup) on this topic. I made use of the **Unix user/group database** option, as well as allowing **Logged-in users can do anything**.

#### Install Plugins

Go ahead and update the existing plugins on your system. In addition, install these additional plugins:

 * Jenkins GIT plugin
 * GitHub API Plugin
 * GitHub plugin
 * Github Authentication plugin

Restart Jenkins after these install succesfully.

#### Configuring a New Job

Configure a new job as a **free-style software project**. Let's update the following options on the configuration page:

 * **Discard Old Builds** - Choose your retention history.
 * **GitHub project** - Full link to the Github repository we create later.
 * **Source Code Management** - Git.
 * **Repository URL** - Specify the URL of this remote repository. This uses the same syntax as your git clone command.
 * **Branches to build** - I specified master in my configuration.
 * **Build Triggers** - Build when a change is pushed to GitHub.
 * **Build** - Add an Execute shell build step for the following commands:
```
/usr/bin/make html
```

```
/usr/bin/python /var/lib/jenkins/.scripts/cf_pyrax.py
```

Put these in separate build steps. Be sure to save your settings.

#### Locate your hook URL

Login to Jenkins, and browse to **Manage Jenkins > Configure System**. Look for **GitHub Web Hook** towards the bottom of the page, and expand the help option on the right. This should provide you with a hook URL we'll use later. It should look similar to the following:

> http://servername:8080/github-webhook/

This should be all we need to do with Jenkins for now. Let's move on to Github.

### Github

Github will be the central repository for our blog's code. It will also be the launch point for the rest of our automation.

1. Create a public repository for your code. Use whatever name you want. I suggest you allow Github to create the README.md file for you automatically.
1. Clone this repository to your local machine.
1. As discussed in the Pelican section, use **pelican-quickstart** to setup the necessary files on your local workstation. Feel free to push your changes to your repository. **Caution:** Make sure nothing in your code contains sensative information. Once added to a git repository, it is available forever, even if you delete the local copy.
1. Edit the settings for your repository, and choose ** Service Hooks**. Locate **Jenkins GitHub Plugin** in the list, and enter your Jenkins Hook URL. Don't forget to activate the hook and Update settings.

### pyrax

Installation instructions for the pyrax modules can be found [here](http://docs.rackspace.com/sdks/guide/content/python.html). We are relying on pip again for this installation. This should be installed on the remote server.

**Note:** Be sure to install the **keyring** module before installing the pyrax module. The pyrax installation will fail unless you install keyring first.

I've written a script to automatically empty a Cloud Files container and upload the static content Pelican generates with the **make html** command. The source for this script can be found on [my Github](https://github.com/Linuturk/www.onitato.com/blob/master/cf_pyrax.py).

Modify this script with your specific information, and place it on your remote server in the **/var/lib/jenkins/.scripts/cf_pyrax.py** directory. Make sure the permissions and ownership of this folder and file allow the Jenkins service access. You will notice this matches the Build step we added earlier in the Jenkins section.

### Rackspace Cloud Files

If you don't have a Rackspace Cloud Account, you will need to [sign up](https://cart.rackspace.com/cloud/).

Once you have the account, make note of your username and apikey. Once you have access to your control panel, create a Cloud Files container, and publish it to the CDN. You will need to set a relatively low TTL for your container after publishing it to the CDN. Make sure you have the following information to add to your pyrax script:

 * Username
 * ApiKey
 * Region
 * Container Name
 * Folder on your Jenkins server where Pelican outputs your static files.

**Caution:** Do not add this to your git repository with this sensative information in the script. Your ApiKey should be protected at all costs.

## Putting it all Together

### Final Steps

Now that all the pieces are in place, let's make the necessary updates to our DNS settings so our blog is live. The following records will need to be created:

 * CNAME record for **www.domain.com** pointing to the CDN URL provided by Cloud Files.
 * URL Redirect for **domain.com** pointing to **www.domain.com**.

**Note:** If your DNS provider doesn't support URL Redirects natively, you should point to a web server with the necessary redirect in place.

### Daily Workflow

Now, let's define the workflow for updating your blog:

1. Create your content in the necessary format and location in your git repository.
1. Commit this new content or changes to your repository.
1. Push these changes to Github.
1. Github will notify Jenkins that changes have been made.
1. Jenkins will pull the latest changes from Github.
1. Jenkins will run the necessary Pelican command to generate the static content.
1. Jenkins will run the cf_pyrax.py script to empty your Cloud Files container, and then upload the latest static content.
1. Your updates are now live!

## Final Notes

Good work! If everything went well, you now have a hassle free, automated blog. I recommend you read through the [Pelican documentation](http://docs.getpelican.com/en/3.1.1/), and play with themes for your blog. Feel free to reference my settings and file struction on [my Github](https://github.com/Linuturk/www.onitato.com).
