+++
title = "Pyrax Container Sync Update"
date = "2014-02-11"
tags = ["pyrax", "python", "rackspace", "cloud files"]
topics = ["tech"]
slug = "pyrax-container-sync-update"
description = "Less data transfer."
+++

My initial draft of the **cf_pyrax.py** script used in my automation deleted all the contents of a Cloud Files container, and then re-uploaded this content. This process was inefficient and also caused issues loading the site while this process was running.

I have now updated this script to use the new **sync_folder_to_container** method from pyrax. This method was introduced to pyrax in this [commit](https://github.com/rackspace/pyrax/commit/135657260a9545a2d5f48e673a182b18aebcbdc4). **Make sure you update your pyrax modules before using this new script.**

```bash
pip install --upgrade pyrax
```

I identified this problem in Issue [#4](https://github.com/Linuturk/www.onitato.com/issues/4), and you can find the code changes in the following commits:

* [05dfa58](https://github.com/Linuturk/www.onitato.com/commit/05dfa581c16b82a7d6cf2dccb0646d1927d3786a)
* [06f0a10](https://github.com/Linuturk/www.onitato.com/commit/06f0a101e438a06698e3c9bfeead8791fdc75724)
* [5dd41e1](https://github.com/Linuturk/www.onitato.com/commit/5dd41e1003a43db4ec6c0d6b651c55e227c58f4e)

There is an [interesting issue](https://github.com/rackspace/pyrax/issues/14) in pyrax where the default encoding doesn't seem to be set if you aren't using a pyrax.cfg. Make sure you leave the default encoding setting, or you will run into this problem as well.

You can download the new [cf_pyrax.py](https://github.com/Linuturk/www.onitato.com/blob/84d2b873e12a39e505a9ef27e4d55a4fd30cc206/cf_pyrax.py) and get started with this more efficient process.

**Update:** You might want to check out [turbolift](https://github.com/cloudnull/turbolift) for your Cloud Files uploading needs. You can see usage in my [circle.yml](https://github.com/Linuturk/www.onitato.com/blob/master/circle.yml#L8).
