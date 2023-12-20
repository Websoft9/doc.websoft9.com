---
sidebar_position: 1
slug: /azure
---

# Guide

## Manage VM

The following lists the common operations of VM management, and the VM status can be modified in the Azure console, including:

### Connect VM

The username and password or key pair is set by yourself when VM created. 

![img](http://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-createvmsshkey-websoft9.png)

Azure provides two web-based SSH tools that can be logged in without an account.

- Method 1: Log in to the Azure Portal, open the VM -> Operations, click "Run command"

![Run command on Azure](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-runcmd-websoft9.png)

- Method 1: Log in to the Azure Portal, open the VM -> Support+troubleshooting, click "Serial console"

![Run command on Azure](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-runcmd2-websoft9.png)

> If you are not used to using the online SSH command line tool provided by the cloud platform, download the SSH client tool (e.g [putty](https://putty.org/)), configure the login information and then connect to Linux.

After connecting to the server through the command line, the following two most common examples for you:

##### Sample: Get database password

For security reasons, each time a user deploys, a unique random database password is generated and stored in the service. Just require the following command to view:

```shell
cat /credentials/password.txt

//result
MySQL username:root
MySQL Password:@qDg1Vq1!V
```

##### Sample: Enable the root account{#enableroot}

For security and regulatory requirements, Azure does not open the Linux root account by default, and only provides users with a common account. If you wish to use the root account, enable it by following the steps below:

```shell
sudo su
sudo sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
sudo systemctl restart sshd
sudo passwd root
```

### Create VM

Here's how to create a VM on Azure.  

The most basic condition for creating a virtual machine is to prepare a boot disk file for the system disk for the virtual machine. There are two types of template files: one is a image that we are very familiar with, and the other is a VHD (virtual disk) file.  

Therefore, there are two ways to create a VM: image-based creation and system-based disk creation.  

#### Image-based Creation

1. Log in to the Azure Portal and open: VM -> Create a virtual machine

2. Select the appropriate image when creating the VM (this is the most important step)
   ![image.png](http://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-createvmbyimage-websoft9.png)

> Image sources are: official image, Marketplace image and Customized image. If you use the customized image source, the disk can only choose the hosting mode.

3. Set the account password, network, security group, etc.

4. "Review + create" after you pass, click "Next"

#### VHD Creation

1. Log in Azure Portal, click "All Resources", find a disk that has been unattached
   ![image.png](http://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-createvmbydisk-websoft9.png)
2. Click the "Create VM"
3. Set the account password, network, security group, etc.
4. "Review + create" after you pass, click "Next"

#### Key pairs

When creating a VM, some users prefer to use the SSH key pair as the login credentials.

![image.png](http://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-createvmsshkey-websoft9.png)

Since Azure needs to provide its own SSH public key, it requires the user to prepare in advance.

Take PUTTYGEN (KEY GENERATOR FOR PUTTY ON WINDOWS) as an example to illustrate how to create an SSH public key.

1. Download and Install [PUTTYGEN](https://www.ssh.com/ssh/putty/windows/puttygen).

2. Click "Generate"    
   ![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/en/putty/puttygen-generate-websoft9.png)

3. Public key and Private key is OK, you can copy public to Azure(format starting with "ssh-rsa") ,and Save the public key and private key on your local computer for backups  
   ![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/en/putty/puttygen-generatesave-websoft9.png)

4. When connect Linux on your local computer, you can use private key for authentication   


### Upgrade VM

Azure have provided a complete [Automatic upgrade solution](https://aka.ms/updatemanagement)

1. Login Azure Portal, Click the "Update management" on Operation section, then "Enable" it
  ![Enable update management](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-enableupdate-websoft9.png)
2. Wait for minutes and the Azure will create an update solution. Click "Schedule update deployment" to start set update policy
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-updateset-websoft9.png)


### Resize VM

The VM size can be adjusted, login Azure Portal, and then open: Settings -> Size, click the "Resize" button.

![Resize VM](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-configures-websoft9.png)

### Redeploy VM

In some special cases, the user intends to restore the VM to its original state, but it is desirable to keep all VM configuration options and associated resources reserved. At this time, we need to use the "re-deployment" operation.

1. Select the VM and select the **Redeploy** in the Support+troubleshooting section
  ![Re-deployment](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-resetstart-websoft9.png)
   
2. To confirm the action, select the Redeploy button:
  ![Confirm Reset](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-resetbutton-websoft9.png)

3. When the VM is ready for redeployment, the VM's Status changes to Updating, as shown in the following example:
   ![Updating](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-resetupdate-websoft9.png)

4. When the VM is started on a new Azure host, the Status changes to Starting, as shown in the following example:
   ![Starting](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-resetstarting-websoft9.png)

5. After the VM completes the boot process, the Status returns to Running, which indicates that the VM was successfully redeployed:
   ![Running](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-resetruning-websoft9.png)


### Backup VM

We know that no one (organization) can guarantee that the VM will always be up and running. If the VM fails to start or fails to connect, what would happen without backups? Is this worthwhile to try?

If there is a backup, it can be restored to the state at the time of backup, greatly reducing the loss.

Azure Portal-> All service ->Storage, the "Recovery Services vaults" service is for backup of VM:

![Recovery Services vault](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-backuprs-websoft9.png)



Below we explain how to set up backups for existing VMs and create VMs.

#### Existing VM settings

For the VM that has been created, set the automatic backup strategy, please refer to the following figure.

![set backcup](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-backupstart-websoft9.png)

#### Create VM settings

When creating a VM, we can set up automatic backup mode.

1. Create a VM, backup items under the Management tab, Enable backup
   ![enable backup](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-backupmanage-websoft9.png)

2. Select an already created vault name or create a new vault name and set a backup policy
   ![backup policy](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-backuppolicy-websoft9.png)

3. Increasing the frequency of backups is a good choice when budget allows.

## Disk, Snapshot and Image

The reason we put Disk, snapshots and image together is because there is a certain relationship between the them, and even there is an alternate relationship.  

There are several special concepts in Azure's disk management, explained in advance:

* Managed Disk: Hosted by Azure Public Store
* Un-Managed disk: The disk can only be managed by the storage account under the account, not as an independent resource.
* Storage account: Azure provides a storage account function, the so-called storage account, which is an entry that can manage the disk.

### Data Disk

We know that a data disk is different from the system disk and is mainly used to store data.

#### Add Data Disk

1. Login Azure Portal, select the VM and Stop it
2. Open the Setting->Disks of Stopped VM, click the button "Add data disk"
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-addddisk-websoft9.png)
3. Set the disk name,size and other information
   ![setting datadisk](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-addddisk2-websoft9.png)
4. Connect to OS to initialize disk
    - Windows, please refer to Azure official documantation [Initialize Windows disk](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/attach-managed-disk-portal#initialize-a-new-data-disk)
    - Linux, please refer to Azure official documantation [Initialize Linux disk](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/attach-disk-portal#connect-to-the-linux-vm-to-mount-the-new-disk)
5. Finish adding data disk

#### Detach Data Disk

1. Login Azure Portal, select the VM and Stop it
3. Open the Setting->Disks of Stopped VM
4. Click the "Edit" on the top of Disks page
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-ddiskds-websoft9.png)
5. Then, click the detach icon like below
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-ddiskds2-websoft9.png)
6. Once detach disk, please save it
7. Start VM

> The disk detach didn't deleted, it remain in the storage account

#### Change Size

You can change the Size or change the Account type of Data Disk when the disk is not mounted to VM

![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-ddiskin-websoft9.png)

> In most times, the disk can only increase size, not reduce size.

### Create Snapshot

1. Login to [Azure Portal](https://portal.azure.com/)
2. Open the All Services->Compute->Snapshots
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-snapshot-websoft9.png)
3. Then, Click the "+Add" or "Create snapshot" in the Snapshots page
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-createsnapshot-websoft9.png)
4. Follow the prompts to complete the creation from **source disk** to snapshot

### Create Image

As mentioned earlier, image can be created based on snapshots, and image can be created based on VM.

#### VM to Image

1. Login to [Azure Portal](https://portal.azure.com/)
2. Open the VM, and click the "**Capture**" 
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-vmtoimage-websoft9.png)
3. Follow the prompts to complete the next steps
4. It's worth noting that the Capture operation also deletes the VM while creating the image.

#### Snapshot to Image

1. Login to [Azure Portal](https://portal.azure.com/)
2. Open the All Services->Compute->Snapshots
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-snapshot-websoft9.png)
3. You can see all image listed
4. Select the snapshot and create image for it


## Network and Security

### Public IP Address{#ip}

**View it**  

1. Login Azure Portal
2. In the Overview of VM, you can see the Public IP Address directly
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-publicip-websoft9.png)
3. If the VM does not have a public IP address entry (or is empty), you need to refer to the next section to mount a public IP address.


**Mount it**  

When the created VM does not have a public IP address, as long as there is a free (or newly purchased) public IP address, the Azure console can mount the public network IP address to the virtual machine. The specific steps are as follows:

1. Login Azure Portal
2. Open the VM->Networking, then the Network Interface item
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-networkinterface-websoft9.png)

2. On the details of Network Interface, open the "IP configuration" item and click the "ipconfig1"
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-ipconfig-websoft9.png)

3. Existing public network IP mount operation on ipconfig1
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-ipconfig1-websoft9.png)

4.If there is no public network IP option, you can create a new one.
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-createip-websoft9.png)

**Static IP**

The default option for creating a VM is to create a dynamic IP. You can also choose to create a static IP.

![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-createstaticip-websoft9.png)

### Security Group{#securitygroup}

A security group is a function that manages a VM port, which is a channel for access application from external access. Let's take the port of **as an example** to introduce you to the use of security groups.

1. Open your VM->Networking, you can see the Security Group setting of VM
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-networkset-websoft9.png)

2. Click "Add inbound port rule" and input the rules like below
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-safegroup80-websoft9.png)

3. Save it

## Domain Name{#domain}

General techniques such as applying for a domain name and resolving domain names are not discussed in this document.

Here we introduce a more useful domain name feature of Azure: Azure provides DNS services for each virtual machine.

When the VM is configured with a dynamic IP address, the IP address may change each time the VM is restarted. As a result, the domain name needs to be re-resolved, which brings unnecessary trouble to the operation and maintenance. Azure's DNS function is to help us avoid this problem.

1. Login Azure Portal, Open the Overview of VM, Click the "Configure" of DNS name
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-opendns-websoft9.png)
2. Input your DNS name label, e.g "mysite", then Save it
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-setdns-websoft9.png)
3. Complete this setting, you can visit URL http://mysite.centralus.cloudapp.azure.com to this VM's applications