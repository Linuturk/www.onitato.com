Title: Automated Blog
Date: 2013-2-5 22:00
Tags: blog, rackspace, jenkins, pelican, git, github, cloudfiles
Category: tutorial
Slug: automated-blog
Author: Justin Phelps
Summary: Managing a blog can be a hassle. Operating system updates, blog software updates, and server security take up tons of time. Don't forget about scaling your blog if you get popular. Inspired by the [Rackspace DevOps post](http://devops.rackspace.com/the-new-devops-blog.html) on their new blog format, I've setup my own version using [Pelican](http://blog.getpelican.com/) instead of [Octopress](http://octopress.org/).

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

Installing git should be fairly simple. Instructions for various operating systems can be found [here](http://git-scm.com/downloads).

### Pelican

Installing Pelican is simple assuming you have pip available on your system. I've found the following method best for installing both pip and pelican. If you don't have access to the **easy_install** command, try finding the python-setuptools package in your repositories.

Do this for your local workstation, as well as your remote server.
```python
easy_install pip
pip install pelican Markdown
```

Once you have this installed on your local workstation, you need to generate the necessary files using **pelican-quickstart**. You will need to run this in the git repository we clone from Github.

### Jenkins
### Github

Github will be the central repository for our blog's code. It will also be the launch point for the rest of our automation.

1. Create a public repository for your code. Use whatever name you want. I suggest you allow Github to create the README.md file for you automatically.
1. Clone this repository to your local machine.

This is enough to get us started. Now we 

### pyrax
### Rackspace Cloud Files
