#!/usr/bin/python
import pyrax
import argparse


# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('container', type=str)
parser.add_argument('folder', type=str)
parser.add_argument('region', type=str)
parser.add_argument('credentials', type=str)
args = parser.parse_args()

# Settings
container = args.container
folder = args.folder
region = args.region
credentials = args.credentials

# Authentication
pyrax.encoding = "utf-8"
pyrax.set_setting("identity_type", "rackspace")
pyrax.set_setting("region", region)
pyrax.set_credential_file(credentials)

# Initiate the Cloud Files connection
cf_ord = pyrax.cloudfiles

# Upload the entire folder to the cloud files container.
print("Syncing all objects to %s container from folder %s." %
      (container, folder))
cf_ord.sync_folder_to_container(folder, container, delete=True,
                                include_hidden=True, ignore_timestamps=True)
print "Sync complete."
