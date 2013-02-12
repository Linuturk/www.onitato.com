Title: Pyrax Container Sync Update
Status: draft
Date:
Tags: pyrax, python, rackspace, cloud files
Category: rackspace
Slug: pyrax-container-sync-update
Author: Justin Phelps
Summary: My initial draft of the cf_pyrax.py script used in my automation deleted all the contents of a Cloud Files container, and then re-uploaded this content. This process was inefficient and also caused issues loading the site while this process was running.

My initial draft of the cf_pyrax.py script used in my automation deleted all the contents of a Cloud Files container, and then re-uploaded this content. This process was inefficient and also caused issues loading the site while this process was running.

I have now updated this script to use the new sync_folder_to_container method from pyrax. This method was introduced in pyrax in this [commit](https://github.com/rackspace/pyrax/commit/135657260a9545a2d5f48e673a182b18aebcbdc4). Make sure you update your pyrax modules before using this new script.

```
pip install --upgrade pyrax
```

I identifed this problem in Issue [#4](https://github.com/Linuturk/www.onitato.com/issues/4), and you can find the code changes in the following commits:
 * [05dfa58](https://github.com/Linuturk/www.onitato.com/commit/05dfa581c16b82a7d6cf2dccb0646d1927d3786a)
 * [06f0a10](https://github.com/Linuturk/www.onitato.com/commit/06f0a101e438a06698e3c9bfeead8791fdc75724)
 * [5dd41e1](https://github.com/Linuturk/www.onitato.com/commit/5dd41e1003a43db4ec6c0d6b651c55e227c58f4e)

There is an [interesting issue](https://github.com/rackspace/pyrax/issues/14) in pyrax where the default encoding doesn't seem to be set if you aren't using a pyrax.cfg. Make sure you leave the default encoding setting, or you will run into this problem as well.

You can download the new [cf_pyrax.py](https://github.com/Linuturk/www.onitato.com/blob/master/cf_pyrax.py) and get started with this more efficient process.
