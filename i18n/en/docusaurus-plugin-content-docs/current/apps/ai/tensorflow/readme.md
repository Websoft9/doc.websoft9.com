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

1. Use SSH to connect Server, run the following command to check the status of TensorFlow
   ```
   sudo systemctl status tensorflow
   ```

2. Using local Chrome or Firefox to visit the URL http://DNS:6006 or http://Internet IP:6006 to access TensorBoard


 > More useful TensorFlow guide, please refer to [TensorFlow Documentation](https://www.tensorflow.org/learn)


### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

**Why should I run `source /data/apps/tensorflow/bin/activate`?**

This TensorFlow used Python environment for deployment


## TensorFlow QuickStart

Now, we run a TensorFlow sample for quick start:

1. Use SSH to connect Server, running the sample script by the following commands
   ```
   cd /data/apps/tensorflow
   source /data/apps/tensorflow/bin/activate
   python tensorflow_test.py
   ```

2. Login to TensorBoard, you can see the graph changed
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/tensorflow/tensorflow-simpletest-websoft9.png)


## TensorFlow Setup

### TensorBoard Password

This deployment solution use the Nginx htpasswd for TensorBoard authentication, refer to [Nginx .auth_basic](./nginx#authbasic)

### Web-based GUI - TensorBoard


[TensorBoard](https://www.tensorflow.org/tensorboard/) is the TensorFlow's visualization toolkit, TensorBoard provides the visualization and tooling needed for machine learning experimentation:

1. Use local browser to access the URL *http://DNS:6006* or *http://Server's Server's Internet IP:6006* to login

2. Input username and password ([Don't have password?](./user/credentials)), you can see the console of TensorBoard
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/tensorflow/tensorflow-board-websoft9.png)

3. TensorBoard screenshots
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/tensorflow/tensorboard.gif)

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage TensorFlow 


????????????`docker ps`?????????????????? TensorFlow ?????????????????? Container???

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


??????????????? TensorFlow ??????????????????

### Path{#path}

TensorFlow installation directory?????*/data/apps/tensorflow*  
TensorFlow ?????????????????*/data/logs/tensorflow*  
TensorFlow ?????????????????*/data/apps/tensorflow/conf*  

### Port{#port}

| ????????? | ??????                                          | ????????? |
| ------ | --------------------------------------------- | ------ |
| 6006   | ?????? HTTP ?????? TensorBoard | ??????   |



### Version{#version}

```shell
/data/apps/tensorflow/bin/tensorboard --version_tb
```

### Service{#service}

```shell
sudo systemctl start | stop | restart tensorflow

```

### CLI{#cli}

TensorFlow ???????????????????????????????????? `tfx`?????????????????????????????????

```
source /data/apps/tensorflow/bin/activate
pip install tfx
```

 >tfx????????????2.3.2????????????????????????TensorFlow????????????

### API

[API Documentation](https://tensorflow.google.cn/api_docs)

