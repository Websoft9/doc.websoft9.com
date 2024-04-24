---
sidebar_position: 1
slug: /faq
---

# Technology FAQs

We categorize technical FAQs: 

* Application initialization
* Maintenance
* Security

If you can't find FAQ you need, please go to [Troubleshoot homepage](./troubleshoot) or contact our [Customer Success Team](./helpdesk)。  

## Application initialization{#setup}

#### Can't access the app start page?{#blank}

Common reasons are as follows:

* Your TCP:80 of Security Group Rules is not allowed
* You have access the incorrect URL
* You have deploy another product which is not targeted
* You instance have network problem
* Product error

No matter what the reason, if there is no problem, please contact our [Customer Success Team](./helpdesk)

#### How to configure Security group?

Refer to: [Security group Settings for Cloud](./administrator/firewall#security)  

#### What's the credentials and password?

Password for database is stored in a particular file of your server: `/credentials/password.txt`. 

More detail please refer to: [Credentials](./user/credentials)

#### How can connect or login Server?

More detail please refer to: [Cloud Guide](./user/cloud#connect)

#### How to upload files to Server?

FTP is not installed in the system by default, but you can manage files in an **easier** way:

* Windows server: Connect by [Remote Desktop](./user/cloud#connectwindows), then copy and paste files.
* Linux Server: Connect by [SFTP](./user/cloud#connectlinux) and manage files by visualization interface.

#### Can't connect to the server?

The following figure shows the primary causes of instance login failures and their probabilities. If you cannot connect to an instance, we recommended you use the diagnosis tool and perform troubleshooting as instructed below.

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/common/ecs-cannotconnect.png)

#### Nginx 502 error?{#nginx502}

Nginx 502 is Nginx 502 Bad Gateway which means error is at the backend service for Nginx.  

* Resource not enough for backend service
* Backend service is stopped

So, you should make sure you can access your backend service first, then use Nginx to proxy it

#### How can I get all service of app?

```
sudo docker ps -a
```

#### How to configure the domain?

More detail please refer to: [Domain for application](./administrator/domain)

#### Can I access app if no domain?

Yes, access it by Internet IP

## Maintenance

#### The app Service can't start?

Two aspects of investigation:  

1. Check the computing resource
    ```shell
    # process
    ps aux

    # disk
    df -lh

    # memory
    free -lh
    ```

2. Check the logs of your app
    ```shell
    # App log of container
    docker logs appname

    # App logs of Systemd
    systemctl status appname
    journalctl -u appname
    ```

#### What path of app, data, configuration? 

Refer to: [Parameter by default](./administrator/parameter)

#### How to manage database?

Refer to: [Database GUI](./user/dbgui)

#### How to set HTTPS?

Refer to: [HTTPS Settings](./administrator/domain_https) 

#### How to check error logs?

Refer to: [Check logs](./troubleshoot/logs) 

#### Port is used and service can't start?{#portconflict}

Run command `netstat -tunlp` to check used port on Server

#### Redirect error?{#redirect}

**Cause**: Infinite loop or redirect target does not exist   
**Solution**：Analyze the `.htaccess` file in the root directory of the website to see if there are infinite loop rules

#### Docker container can't start?{#containernotstart}

```shell
sudo docker logs appname
```

#### Docker service can't start?{#dockernotstart}

Run the command `systemctl status docker` and `journalctl -xe` to check logs  

If error message is *Unit docker.socket entered failed state*, you can run `groupadd docker` command to solve this issue 

## Security

#### How to set a perfect backup strategy?

Refer to: **[Backup and Restore](./administrator/backup)**

#### Any security vulnerabilities in image?

It is certain that there are no security vulnerabilities by default because any image have been passed strict security checks by Cloud Platform.  

#### Why new vulnerabilities from Cloud?

The software itself is constantly upgraded and iteratively developed, and vulnerabilities are always growing in the cycle from discovery to patching. The image includes: operating system, middleware, database, language and other software packages, and any software package may have vulnerabilities.  

The latest vulnerabilities will be discovered, and the cloud platform will immediately notify users, which is a good thing.  
