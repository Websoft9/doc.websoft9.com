---
sidebar_position: 1
slug: /jenkins
tags:
  - Jenkins
  - DevOps
---

# Jenkins Getting Started

[Jenkins](https://www.jenkins.io) is a self-contained, open source automation server which can be used to automate all sorts of tasks related to building, testing, and delivering or deploying software.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins_is_the_hub_CD_Devops.png)  

If you have installed Websoft9 Jenkins, the following steps is for your quick start


## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Connect your Server and get **[default username and password](./user/credentials)** of Jenkins
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Jenkins.

## Jenkins Initialization

### Steps for you

1. Using local browser to visit the URL *http://DNS* or *http://Server's Internet IP*, you will enter initial wizard of Jenkins
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/jenkins/jenkins-installstart-websoft9.png)

2. Connect Server and run command `sudo cat /var/lib/jenkins/secrets/initialAdminPassword` to Unlock Jenkins

3. Login the Jenkins console  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/jenkins/jenkins-installcustomer-websoft9.png)

4. Install plugins   
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/jenkins/jenkins-installing-websoft9.png)

5. Create user for Jenkins  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/jenkins/jenkins-installusers-websoft9.png)

> More useful Jenkins guide, please refer to [Jenkins Documentation](https://www.jenkins.io/zh/doc/)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## Jenkins QuickStart

This task【Build Github repository by Jenkins】 is for your Jenkins QuickStart

1. 在 GitHub设置 Personal access tokens，用于 Jenkins 连接
 ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-wizard2-websoft9.png)

2. Jenkins全局系统设置中，连接 GitHub
 ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-wizard3-websoft9.png)
 ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-wizard4-websoft9.png)
 ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-wizard5-websoft9.png)

3. 创建一个构建任务：输入任务名，按流程分别输入 Github项目 URL，账号密码等信息
 ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-wizard6-websoft9.png)
 ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-wizard7-websoft9.png)
 ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-wizard8-websoft9.png)
 ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-wizard9-websoft9.png)
 ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-wizard10-websoft9.png)
 ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-wizard11-websoft9.png)

4. 在对应Github 项目修改后，push提交；Jenkins完成自动化构建部署
 ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-wizard12-websoft9.png)

## Jenkins Setup

### Install plugin{#installplugin}

Login to Jenkins, open：【【Manage Jenkins】>【Plugins Manager】 to manage and install all plugins

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins_installemailplugin-websoft9.png)

### Configure SMTP{#smtp}

1. Install the Jenkins plugin [Email Extension](https://plugins.jenkins.io/email-ext/)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins_installemailplugin-websoft9.png)

2. Prepare your [SMTP parameter](./administrator/smtp)

3. Log in Jenkins Console, open 【Manage Jenkins】>【Configure System】, set you SMTP
   ![Jenkins SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins_configuresmtp-websoft9.png)

4. Test it

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Jenkins

### Port

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 8080   | Jenkins original port | Optional   |


### Version

```shell
jenkins -v
```

### Service

```shell
sudo systemctl start | stop | restart | status jenkins
```

### CLI

Jenkins has a [built-in command line interface](https://www.jenkins.io/doc/book/managing/cli/) that allows users and administrators to access Jenkins from a script or shell environment.

```shell
java -jar jenkins-cli.jar [-s JENKINS_URL] [global options...] command [command options...] [arguments...]
```

### API

Jenkins provides machine-consumable remote access [API](https://www.jenkins.io/doc/book/using/remote-access-api/) to its functionalities
```
curl JENKINS_URL/job/JOB_NAME/buildWithParameters \
  --user USER:TOKEN \
  --data id=123 --data verbosity=high
```