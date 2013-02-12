#!/usr/bin/python
import pyrax, time

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
print "Uploading all objects to %s container from folder %s." % (container, folder)
upload_key, total_bytes = cf_ord.sync_folder_to_container(folder, container, delete=True, include_hidden=True, ignore_timestamps=True)

count = 0
timeout_error = 0

while total_bytes != pyrax.cloudfiles.get_uploaded(upload_key):
    uploaded_bytes = pyrax.cloudfiles.get_uploaded(upload_key)
    print "Still uploading %i out of %i" % (uploaded_bytes, total_bytes)
    time.sleep(1)
    count += 1
    if count > 60:
        timeout_error = 1
        break
else:
    if timeout_error == 0:
        print "Upload of %i bytes complete." % total_bytes
    else:
        print "Upload progress timed out. You might want to re-run the upload."
