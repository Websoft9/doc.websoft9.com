---
sidebar_position: 2
slug: /migration-from-websoft9
---

# Migrate from Websoft9

Websoft9 doesn't like vendor lock-in, we advocate open technology principles and product design philosophies.    

Websoft9 applications exist as Docker containers, making it easy to use Docker's native migration solution.  

Three steps for migrating from Websoft9:

```
#1 Create image from container
sudo docker commit appname image_name

#2 Export image to tar file
sudo docker save image_name > image_name.tar

#3 Reload tar file to container
sudo docker load < image-name.tar
```