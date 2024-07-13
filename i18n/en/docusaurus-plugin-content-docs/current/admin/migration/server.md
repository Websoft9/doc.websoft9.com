---
sidebar_position: 3
slug: /migration-server
---

# Migrate entire server

Migrate entire server is a migration requirement that remains unchanged from the entire VM level, and is generally characterized by the following two use cases:  

## Cross-regional migration

Cross-region migration refers to the migration of different regions within the same cloud platform or infrastructure.    

You just need use **copy** action by your cloud infrastructure.  

## Cross-infrastructure migration

Cross-infrastructure migration is migrating origin virtual machines to another infrastructure.  

If cloud provider have "migration VM tools", it may easy for migration. Otherwise, you may need migration are as follows:

1. Install a set of required software on the virtual machines to be migrated: 

   - Cloud init
   - Virtio drivers
   - Other packages target cloud need

2. Create a virtual machine image at source cloud

3. Export the image to a file (format: vhd, RAW, etc.)

2. Upload the exported file to the object store of the target cloud platform.

3. Create a mirror in the cloud based on the uploaded file in the object store.

4. Create a virtual machine based on the image in the cloud.