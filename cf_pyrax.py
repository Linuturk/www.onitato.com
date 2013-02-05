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

# Empty the container
print "Deleting all objects in %s container." % container
cont.delete_all_objects()

# Confirm container is empty
while cont.get_objects() != []:
    print "Deletion in progress . . . "
    time.sleep(1)
else:
    print "Deletion complete."

# Upload the entire folder to the cloud files container.
print "Uploading all objects to %s container from folder %s." % (container, folder)
upload_key, total_bytes = cf_ord.upload_folder(folder, container)

while total_bytes != pyrax.cloudfiles.get_uploaded(upload_key):
    uploaded_bytes = pyrax.cloudfiles.get_uploaded(upload_key)
    print "Still uploading %i out of %i" % (uploaded_bytes, total_bytes)
    time.sleep(1)
else:
    print "Upload of %i bytes complete." % total_bytes
