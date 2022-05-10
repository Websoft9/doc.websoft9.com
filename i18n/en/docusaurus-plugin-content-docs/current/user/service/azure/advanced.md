---
sidebar_position: 3
slug: /azure/advanced
---

# Advanced

## Concept

### API/CLI

Refer to: [Azure API/CLI](https://docs.microsoft.com/en-us/cli/azure/)

## FAQ + Troubleshoot

If you have identified the problem for the reason is VM, refer to [Azure Virtual Machine Troubleshooting](https://docs.microsoft.com/en-us/azure/virtual-machines/troubleshooting/).

#### What Is the Username of VM?

It set by yourself when create VM

#### How to enable the root user of Azure?

By default, the root account is not enabled on Azure, in fact we can find a way to enable it.

Refer to: [Linux Connect](../azure#enableroot) chapter of this documentation.

#### What should I do if the VM's IP address changes after it restarts?

It is recommended to change to a static IP or set up a DNS provided by Azure for the server.

#### Can the image on the VM be replaced?

No

#### Can I use a temporary disk (/dev/sdb1) to store data?

Do not use a temporary disk (/dev/sdb1) to store data. It is only used for temporary storage. There is a risk of losing data that cannot be recovered.

#### What are the format requirements for VM credentials ?

Refer to:[Azure username and password requirements](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/faq#what-are-the-username-requirements-when-creating-a-vm)

#### Can't create VM from your image which from Marketplace?

We know using image or VHD to create VM is a reasonable operation for user on Azure Portal. But the Azure have a "issue" when image is from Marketplace for creating VM. If you delete your Wordpress VM and only retain the VHD, then create VM from VHD, you can also get the similar error.

Why this error?  I think when creating VM from your image, azure system will verify the subscription information of image, but azure portal have no selection for this

How to solve this?

1. Use Azure Powershell to get your image subscription plan of Marketplace
```
PS Azure:\> az vm image list --offer w9wordpress2 --all --output table
Offer         Publisher    Sku                          Urn                                                             Version
------------  -----------  ---------------------------  --------------------------------------------------------------  ---------
w9wordpress2  websoft9inc  wordpress52-lemp72-centos76  websoft9inc:w9wordpress2:wordpress52-lemp72-centos76:5.2.20000  5.2.20000
```

2. Create VM from your image, at the last step please download this template
https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-dltemplate-websoft9.png

3. Find the "resources" [  "properties[]" ]  item in the template, add the follow plan to properties[]
```
"plan": {
                "name": "wordpress52-lemp72-centos76",
                "publisher": "websoft9inc",
                "product": "w9wordpress2"}
```
4. Save the template
5. Click "Deploy"