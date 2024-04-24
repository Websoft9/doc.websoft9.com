---
sidebar_position: 1
slug: /tensorflow
tags:
  - TensorFlow
  - AI
  - ML
---

# TensorFlow Getting Started

[TensorFlow](https://www.tensorflow.org/) is an end-to-end open source machine learning platform. It has a comprehensive and flexible ecosystem, which contains a variety of tools, libraries and community resources. In terms of machine learning, it can easily build models, carry out reliable machine learning production anytime and anywhere, and conduct powerful research experiments.

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/tensorflow/tensowflow-gui-websoft9.jpg)

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:6006,80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for TensorFlow
4. [Get](./user/credentials) default username and password of TensorFlow

## TensorFlow Initialization

### Steps for you

1. Use the browser of your local computer to access the URL: *http:// domain name* or *http:// server public IP* to enter the login page  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/tensorflow/tensorflow-login-websoft9.png)

2. Use SSH to connect Server, run the following command to obtain the token:  

   ```
   $ docker exec -it tensorflow jupyter notebook list
   Currently running servers:
   http://0.0.0.0:8888/?token=c8929544462391e32bbf0d7763b7b5dda3ab00b2f14da5b9 :: /tf

   ```

3. Log in to the console and use jupyter (edit the source code)  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/tensorflow/tensorflow-main-websoft9.png)

4. Use SSH to connect Server, run the following command to start TensorBoard 

   ```
   $ docker exec -it tensorflow bash
   $ cd /usr/local/lib/python3.8/dist-packages/tensorboard && tensorboard --logdir=/data/logs --port 6006 --host 0.0.0.0
   ```

5. Using local Chrome or Firefox to visit the URL http://DNS:6006 or http://Internet IP:6006 to access TensorBoard


 > More useful TensorFlow guide, please refer to [TensorFlow Documentation](https://www.tensorflow.org/learn)


### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  


## TensorFlow QuickStart

Now, we run a TensorFlow sample for quick start:


## TensorFlow Setup

### TensorBoard Password


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage TensorFlow 


Run `docker ps` command, view all Containers when TensorFlow is running:

```bash
CONTAINER ID   IMAGE                                  COMMAND                  CREATED        STATUS         PORTS                                                                                  NAMES
f7e151917bec   tensorflow/tensorflow:latest-jupyter   "/bin/bash -c 'cd /u…"   15 hours ago   Up 2 minutes   0.0.0.0:6006->6006/tcp, :::6006->6006/tcp, 0.0.0.0:9001->8888/tcp, :::9001->8888/tcp   tensorflow
```


### Path{#path}

TensorFlow installation directory： */data/apps/tensorflow*  
TensorFlow notebooks directory： */data/apps/tensorflow/data/tensorflow*  

### Port{#port}

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 6006   | Access TensorBoard via HTTP | Optional   |



### Version{#version}

```shell
docker exec -it tensorflow grep "_VERSION =" /usr/local/lib/python3.8/dist-packages/tensorflow/tools/pip_package/setup.py| cut -d= -f2
```

### Service{#service}

```shell
sudo docker start | stop | restart tensorflow

```

### CLI{#cli}

TensorFlow provides a powerful command-line tool 'tfx', which can be installed by executing the following commands:  

```
source /data/apps/tensorflow/bin/activate
pip install tfx
```

 > tfx is only supported until 2.3.2, and installation may cause the TensorFlow version to be downgraded

### API

[API Documentation](https://tensorflow.google.cn/api_docs)

