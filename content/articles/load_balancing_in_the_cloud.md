Title: Load Balancing in the Cloud
Tags: rackspace, cloud, load balancing, load balancer
Category: rackspace
Slug: load-balancing-in-the-cloud
Author: Justin Phelps
Summary: Load balancing is performed by a device or service acting as a single endpoint to your application or site. This device then spreads the requests it receives across multiple backend nodes. There are benefits to using a load balancer in your configuration.

*This article is in response to a [request](https://github.com/Linuturk/www.onitato.com/issues/2) by Shawn Laasch and Jordan Rinke. [Request](https://github.com/Linuturk/www.onitato.com/issues) your topic today! This article will focus on [Rackspace Cloud Load Balancers](http://www.rackspace.com/cloud/load-balancing/).*

## Cloud Load Balancers

Load balancing is performed by a device or service acting as a single endpoint to your application or site. This device then spreads the requests it receives across multiple backend nodes. There are benefits to using a load balancer in your configuration:

 * Easily add and remove servers from your configuration without DNS updates.
 * Automatically remove failed nodes from your configuration with Health Monitoring.
 * Cache content on the load balancer to lighten the load on the application servers.
 * Centralize the management of SSL Certificates.

Rackspace recently launched Open Cloud Servers and other related cloud services. Cloud Load Balancers did not undergo any major revisions during this launch. Cloud Load Balancers are provisioned with both IPv4 and IPv6 addresses.

## Other Load Balancing Options

There are other methods of load balancing that don't involve Cloud Load Balancers. I can't claim expertise in these other methods, but I am mentioning them for completeness.

### HAProxy

[HAProxy](http://haproxy.1wt.eu/) is a free, very fast and reliable solution offering high availability, load balancing, and proxying for TCP and HTTP-based applications. It is particularly suited for web sites crawling under very high loads while needing persistence or Layer7 processing. Supporting tens of thousands of connections is clearly realistic with todays hardware.

### nginx

[nginx](http://nginx.org/) [engine x] is an HTTP and reverse proxy server, as well as a mail proxy server, written by Igor Sysoev. For a long time, it has been running on many heavily loaded Russian sites including Yandex, Mail.Ru, VKontakte, and Rambler. According to Netcraft nginx served or proxied 12.81% busiest sites in February 2013.

### DNS Round Robin

[Round Robin DNS & DDNS](http://en.wikipedia.org/wiki/Round-robin_DNS) is a technique of load distribution, load balancing, or fault-tolerance provisioning multiple, redundant Internet Protocol service hosts, e.g., Web servers, FTP servers, by managing the Domain Name System's (DNS) responses to address requests from client computers according to an appropriate statistical model.

## Conclusion

Besides Rackspace Cloud Load Balancers, I have to say my favorite method of load balancing is HAProxy. The reason I prefer HAProxy over the other methods is the robust [Status Page](http://demo.1wt.eu/) that is available by default. This gives you tons of insight into the traffic hitting your systems.

**See this site's disclaimer for information on the accuracy of this post.**
