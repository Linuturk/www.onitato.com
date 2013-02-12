#!/usr/bin/python
import pyrax, time
print "Encoding:", pyrax.encoding
pyrax.encoding = "utf-8"

# Set variables for the various options
username = ""
apikey = ""
region = ""
folder = ""
container = ""

# Set the default region
pyrax.set_default_region(region)

# Set my credentials
pyrax.set_credentials(username, apikey)

# Initiate the Cloud Files connection
cf_ord = pyrax.cloudfiles

# Create the container object
cont = cf_ord.get_container(container)

# Upload the entire folder to the cloud files container.
print "Syncing all objects to %s container from folder %s." % (container, folder)
cf_ord.sync_folder_to_container(folder, container, delete=True, include_hidden=True, ignore_timestamps=True)
print "Sync complete."
