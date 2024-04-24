---
sidebar_position: 1
slug: /aws
---

# Guide

## Manage EC2

### Start, Stop and Terminate

You can change the instance state on EC2 console, including:

- Start
- Stop
- Reboot
- Terminate
- Recover

![aws EC2 state Websoft9](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-ec2state-websoft9.png)

If you want to automatically recover the instance when it becomes impaired due to an underlying hardware failure or a problem that requires AWS involvement to repair, you need to enable [CloudWatch alarms](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html) previously.




### Connect EC2

#### For Linux{#connectlinux}

Command is the basic operation of the Linux system. AWS supports three ways to connect by Command:

| Tool                                                  | Instructions                                                     |
| ------------------------------------------------------ | ------------------------------------------------------------ |
| A standalone SSH client                                  | Download [putty](https://putty.org/) and other SSH clients to local computer to connect to Linux. |
| Hosting SSH client based on my browser (Alpha)               | Connect from AWS console website, the prerequisite is to install [EC2 Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-set-up.html) on your instance. |
| A Java SSH client directly connected from my browser（Java required） | Directly connect from AWS console website, the prerequisite is to **install Java plugin**. |


Taking **Hosting SSH client based on my browser** as an example, steps for how to connect to a Linux server are as follows:

1. Refer to [Set up EC2 Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-set-up.html) to install EC2 Instance Connect module（For Websoft9 image, the module is installed by default, just skip this step.）

2. Login to AWS EC2 console, open 【Instance】> 【Connect】and choose the second way to connect.
   ![command line](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-connectmethods-websoft9.png)

3. Click 【Connect】, a window opens and you are connected to the instance.

After you're connected to the server through command line, the following two most common examples of operations are required.

##### Sample1: Get password

For security reasons, each time a user deploys, a unique random database password is generated and stored in the service. Just require the following command to view:

```shell
sudo cat /credentials/password.txt

//result
MySQL username:root
MySQL Password:@qDg1Vq1!V
```

##### Sample2: Enable root user{#enableroot}

For security and regulatory requirements, AWS does not open the Linux root account by default, and only provides users with a common account. If you wish to use the root account, enable it by following the steps below:

```shell
sudo su
sudo sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config
sudo systemctl restart sshd
sudo passwd root
```

#### For Windows

Before you use local computer's Remote client to connect Windows Server, you should complete these steps: 

1. Login to AWS console, choose the instance which you want to connect to, click 【Connect】 and then click 【Get Password】 in the pop-up window.
   ![aws get password](http://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-winconnect-websoft9.png)

2. Upload the key pair stored locally.
   ![aws upload key pairs](http://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-winconnectpw-websoft9.png)

3. Click 【Decrypt Password】, then the password will be displayed on the interface.
   ![aws Decrypt Password](http://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-winconnectgpw-websoft9.png)


### Create EC2

The introduction below is about how to launch instance on AWS.  

The basic condition for launching instance is to prepare a boot disk file for the system disk for the instance. The most common template file is image.  

Steps below are about how to launch instance based on image:  

1. Login to AWS Management Console, and click 【EC2】.
   ![log in](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-ec2-websoft9.png)

2. Enter EC2 Dashboard, and click 【Launch Instance】to create Instance.
   ![launch instance](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-addec2-websoft9.png)

3. When choosing AMIs, click 【View all public and private AMIs】 and search keyword "websoft9" to see the list of images.
   ![choose image of Websoft9](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-ec2image-websoft9.png)

4. Select the image you need.

5. Finish the following steps, which require you to choose instance type, VPC, set key pair and more.
   ![create instance](http://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-ec2createpw-websoft9.png)

6. Wait several minutes after completing creating EC2, and the image is started as the system disk of the instance, that is, the image is automatically deployed to the instance.

### Key Pair for EC2{#keypair}

When launching instance, AWS requires key pair to log in. Steps for how to create key Pair are as follows:

1. Login to AWS console, open 【EC2 Dashboard】>【NETWORK & SECURITY】>【Key Pairs】and click 【Create Key Pair】.
   ![create key pair](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-createkeyps-websoft9.png)

2. Name the key pair, such as "myKey".
   ![name](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-keypsname-websoft9.png)
   
3. Store key pair file **myKey.pem** into the local computer.

### Change EC2 Type

Follow the steps below to change instance type：

1. Login to AWS console and stop the instance.

2. Open 【Actions】>【Instance Settings】>【Change Instance Type】.
   ![adjust configuration](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-configures-websoft9.png)

3. Complete new settings, then start the instance.

### Get EC2 logs

You can get system log on EC2 console：

1. Login to AWS console and stop the instance.

2. Open 【Actions】>【Instance Settings】>【Get System Log】.
   ![get system log](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-getsyslogs-websoft9.png)
3. Complete the new settings, then start the instance.
   ![display system log](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-syslogs-websoft9.png)


### Backups EC2{#backup}

We know that no one (organization) can guarantee that the EC2 will always be up and running. If EC2 fails to start or fails to connect, what would happen without backups? Is it worthwhile to try?

If there is a backup, it can be restored, which greatly reduce the loss.

For AWS, to create backup for EC2 is based on automatic snapshot for the volume of EC2.

There are two entries to create backups on AWS console:

#### Snapshot Backup

##### Automatic Backup{#snapautobackup}

1. Login to AWS console.  

2. Open【EC2】>【ELASTIC BLOCK STORE】>【Lifecycle Manager】>【Create Snapshot Lifecycle Policy】.
    ![Snapshot lifecycle policy](http://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/en/aws/aws-snapshotauto-websoft9.png)  

3. Follow the prompts to complete the settings.

##### Manual Snapshot 

Steps for manual snapshot on demand are as follows:

1. Login to AWS console and open EC2 Dashboard.  

2. Open 【ELASTIC BLOCK STORE】>【Volumes】 and choose volume to 【Create Snapshot】.
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-createsnapshot-websoft9.png)  

3. Name the snapshot before creating.

#### AWS Backup service

AWS Backup is the specific backup service for AWS resources.

1. Login to AWS console, open 【Services】>【Storage】>【AWS Backup】 and create Backup plan.
   ![AWS Backup service](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-backupservices-websoft9.png)
2. Choose to start from an existing plan and begin to create on-demand backup, that is, to choose the protected resources as you need.
   ![AWS Backup service](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-backupres-websoft9.png) 

3. Choose EBS (disk) as the resource type and choose the volume ID.
   ![AWS Backup service](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-backupres2-websoft9.png) 
   
4. Complete the settings.

### Upgrade EC2

AWS offers [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/) solution, which can help you automate collecting software inventory, patching applications OS, launching system VMs, and configuring Windows and Linux.

1. Login to AWS Management Console and open 【AWS System Manager】 service.

2. Open 【Instances & Nodes】>【Patch Manager】to enter the manage interface.
![launch system manager](http://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/en/aws/aws-sysmupdate-websoft9.png)

3. Follow the guide to complete upgrading.

## Disk, Snapshot and Image

Key connection between snapshots and image are as follow:

* A snapshot can be created based on the disk.

  A snapshot is a "photographing" of a disk. As the name suggests, it is to back up the data of a disk at a certain point in time. It is a backup method.

* A image can be created based on a snapshot, but the image cannot be directly converted into a snapshot.

* Based on the image, you can create an instance directly, and you can create a image directly based on the instance.  

Summary: (volume --> snapshot) --> (image - instance)

### Volumes (Disk)

For AWS, volume can be a separate computing resource (created separately, billed separately, managed separately, etc.) and can be integrated into an instance as a component.

#### Create Volume

1. Login to AWS console and open EC2 Dashboard.

2. Open 【ELASTIC BLOCK STORE】>【Volumes】 to create volume.
   ![create volume](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-createvolume-websoft9.png)
   
3. Complete volume type, size and other settings, then check before creating.
   ![volume settings](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-createvolume2-websoft9.png)
   
4. Attach the volume created to the instance.
   ![attach volume](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-volumeaddec2-1-websoft9.png)
   
   ![attach volume](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-volumeaddec2-2-websoft9.png)
   
5. Log in to the instance, and complete volume initialization to make it available.
    - For Windows, view official document [Making an Amazon EBS volume available for use on Windows](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-using-volumes.html)
    - For Linux, view official document [Making an Amazon EBS volume available for use on Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html) 

6. Complete all settings and the volume is available.

#### Detach Volume

To detach volume from the instance, refer to the steps below:

1. Login to AWS console and open EC2 Dashboard.  

2. Open 【Instances】, choose the instance from which the volume will be detached and click 【Stop】.  

3. Open【ELASTIC BLOCK STORE】>【Volumes】, choose the volume and click 【Detach Volume】.
   ![detach volume](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-detachvolume-websoft9.png)

> The volume detached remains in the storage account and wouldn't be deleted.

#### Modify Volume

If the volume is not attached to instance, it can be modified.

1. Login to AWS console and open 【EC2->ELASTIC BLOCK STORE】>【Volumes】.  

2. Choose the volume need to modify and open 【Actions】>【Modify Volume】.
   ![modify volume](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-ddiskin-websoft9.png)  

3. Set new size.

> In most cases, the volume can only increase in size, but can not decrease.

### Create Snapshots

For AWS, to create Snapshots based on the volume.

1. Login to the AWS console and open EC2 Dashboard.  

2. Open 【ELASTIC BLOCK STORE】>【Volumes】 and choose volume to create Snapshot.
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-createsnapshot-websoft9.png)

3. Name the snapshot before creating.

### Create Image

As mentioned before, image can be created based on snapshots, and instance.

#### Instance to Image

1. Login to AWS console.  

2. Choose the instance, and open 【Actions】>【Image】>【Create image】.
![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-ec2toimage-websoft9.png)   

3. Follow the prompts to complete it.

#### Snapshots to Image

1. Login to the Aws console and open EC2 Dashboard.  

2. Open 【ELASTIC BLOCK STORE】>【Create Snapshot】 and list all snapshots.
3. Choose from the list of snapshots and create image based on it.
   ![Snapshots](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-snapshot-websoft9.png)

## Network and Security

### Internet IP{#ip}

**View IP**  

1. Login to AWS console.  

2. Choose the instance, and you can see the **Public IP** and **Public DNS**.
   ![View IP](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-getip-websoft9.png)  

3. If the instance does not have a public IP address entry (or is empty), you need to refer to the next section to mount a public IP address.


**Mount IP**  

If the created instance does not have a public IP address, as long as there is a free (or newly purchased) public IP address, the AWS console can mount the public network IP address to the instance.The specific steps are as follows: 

1. Login to AWS console.  

2. Choose the instance and open 【Actions】>【Networking】>【Manage IP Addresses】.
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-manageip-websoft9.png)

3. Click 【Allocate an Elastic IP】.
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-assignip-websoft9.png)

4. Follow the prompts to complete the action.

### Security Group{#securitygroup}

A security group is a function of managing the EC2 port, which is a channel for access application from external access. Let's take **opening port 80** as an example to introduce you to the use of security groups.

1. Login to AWS console and open 【EC2】>【Instances】.  

2. Open 【Description】and then click the name of Security groups.
   ![ec2 edit security group](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-changesg-websoft9.png)
3. Enter the setting interface, click 【Inbound】and 【Edit】.
   ![ec2 edit](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-sfin-websoft9.png)
4. Edit inbound rule and add a new one.
   ![ec2 edit rule](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-set80sg-websoft9.png)
3. Save it.

## Domain Name{#domain}

General skill such as applying for a domain name and resolving domain names will not discussed in this document.  

Here we introduce a more useful domain feature of AWS: AWS provides DNS services for each instance.  

### DNS for EC2

AWS provides public public DNS services for each instance.

When the instance is configured with a dynamic IP address, the IP address may change each time the instance is restarted. As a result, the domain name needs to be re-resolved, which brings unnecessary trouble to the operation and maintenance. AWS's DNS function can help us avoid this problem.

1. Login to AWS console and open 【Instance】>【Description】.
   ![view DNS](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-getip-websoft9.png)  

2. Copy the public DNS.

### Route 53

Route 53 is the platform for applying domain, domain resolution and management. You can use Route 53 to register domain names, transfer existing domains, route traffic for your domains to your AWS and external resources and check the health of your resources.

1. Login to AWS console and choose Route 53 in 【Networking & Content Delivery】.
   ![Route 53](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-route53-websoft9.png)
2. Start to manage domains.
   ![Route 53](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-route53start-websoft9.png)