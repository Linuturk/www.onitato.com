#!/usr/bin/python
import pyrax

# Set variables for the various options
username = ""
apikey = ""
region = ""
folder = ""
container = ""

# Set the identity class
pyrax.set_setting("identity_type", "rackspace")
# Set the default region
pyrax.set_default_region(region)
# Set the default encoding
pyrax.encoding = "utf-8"
# Set my credentials
pyrax.set_credentials(username, apikey)
# Initiate the Cloud Files connection
cf_ord = pyrax.cloudfiles

# Upload the entire folder to the cloud files container.
print("Syncing all objects to %s container from folder %s." %
      (container, folder))
cf_ord.sync_folder_to_container(folder, container, delete=True,
                                include_hidden=True, ignore_timestamps=True)
print "Sync complete."
