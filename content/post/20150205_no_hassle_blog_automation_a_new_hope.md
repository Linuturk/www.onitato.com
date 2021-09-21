+++
title = "No Hassle Blog Automation - A New Hope"
tags = ["circleci", "pelican", "blog", "automation"]
topics = ["tech"]
slug = "no-hassle-blog-automation-a-new-hope"
date = "2015-02-05"
description = "No more servers."
+++

In this third installment of my No Hassle Blog Automation series, I remove the necessity for running any infrastructure of my own. Drone has been replaced with a hosted solution at [CircleCI](https://circleci.com/). Their support is amazing, and their circle.yml format made configuration easy. Take a look at the [first](|filename|/articles/no_hassle_blog_automation.markdown) and [second](|filename|/articles/no_hassle_blog_automation_redux.markdown) installments of this series.

# Requirements

There are a few requirements for this setup:

* Rackspace Cloud Account
* Cloud Files Container\*
* Existing Pelican Blog
* GitHub Account

\* This container should be [configured to serve a static site](http://www.rackspace.com/blog/point-and-click-your-way-to-a-cloud-files-static-website-with-the-control-panel/).

# circle.yml

This file is used by CircleCI to define the test and build process. You can find my current circle.yml file [in my repository.](https://github.com/Linuturk/www.onitato.com/blob/master/circle.yml)

```yaml
test:
  override:
    - make html
deployment:
  production:
    branch: master
    commands:
      - turbolift -u $RAXUSER -a $RAXAPIKEY --os-rax-auth $RAXREGION upload -s $HOME/$CIRCLE_PROJECT_REPONAME/output -c $CONTAINER
```

There are two sections to this file:

* **test**: This defines the commands to run to test your code. In this instance, we are simply running the make html command provided by Pelican.
* **deployment**: This defines the commands to run if tests pass successfully. In this case, if tests pass on the master branch, it will issue the turbolift command.

You will need to set the following environment variables in the CircleCI Project configuration:

* **RAXUSER** - Rackspace Cloud user name.
* **RAXAPIKEY** - Rackspace Cloud api key.
* **RAXREGION** - Cloud Files region where your container is located.
* **CONTAINER** - Name of your Cloud Files container.

# requirements.txt

You will also need to add a requirements.txt file to your Pelican blog repository. CircleCI will look at this file and install the listed pip packages. The contents should look like this:

```text
pelican
Markdown
turbolift
```

This is much easier than manually installing things via pip myself.

# Setup

Here is a high level overview of the setup steps:

1. Create a container in Cloud Files, and make sure you configure the container to serve a static site.
1. Setup a CNAME record for your domain to point to the CDN URL provided by Cloud Files.
1. Sign in to CircleCI and link your Pelican blog repository.
1. Configure the necessary Environment Variables in CircleCI.
1. Add the circle.yml file to your repository. Commit and push this change, and GitHub will notify CircleCI to process a build.
1. Review the build in CircleCI to ensure it was published successfully.

That should be all you need to do. Good luck!
