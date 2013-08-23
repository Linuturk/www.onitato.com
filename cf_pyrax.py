#!/usr/bin/python
import pyrax

# Authentication
pyrax.encoding = "utf-8"
pyrax.set_setting("identity_type", "rackspace")
pyrax.set_setting("region", "ORD")
pyrax.set_credential_file(".pyrax_creds")

# Initiate the Cloud Files connection
cf_ord = pyrax.cloudfiles

# Upload the entire folder to the cloud files container.
print("Syncing all objects to %s container from folder %s." %
      (container, folder))
cf_ord.sync_folder_to_container(folder, container, delete=True,
                                include_hidden=True, ignore_timestamps=True)
print "Sync complete."
