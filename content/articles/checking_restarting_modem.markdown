Title: Checking and Restarting a Modem
Tags: motorola, sb6141, bash, automation
Category: tech
Slug: checking-restarting-modem-sb6141
Author: Justin Phelps
Date: 2015-08-12 0:00
Summary: My ISP is less than reliable so I decided to automate my modem restarts.

My ISP is less than reliable so I decided to automate my modem restarts. I'm using a Motorola SB6141 and I can access a web based interface at **192.168.100.1**.

Using a combination of **curl**, **grep**, and **sed**, I was able to scrape the necessary pages to get information about the modem's status. The script then checks the status and restarts the modem if it detects a fault. The script uses curl to GET a specific URL with the necessary parameters. This GET request triggers the modem's restart.

That line looks like this:
```
curl -m 5 -s $HOST/reset.htm?reset_modem="Restart Cable Modem" &> /dev/null
```

It uses the following arguments:

 * **-m** - Sets the max time for the curl command. This is so the script doesn't hang.
 * **-s** - Silences a portion of curl's output.
 * **&> /dev/null** - Redirects all remaining output to /dev/null.

You can find the script [in this GitHub repository](https://github.com/Linuturk/modem-restart-script/blob/master/modemCheck.sh). Hope this works for you as well. **Automate all the things!**
