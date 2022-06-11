---
sidebar_position: 3
slug: /tensorflow/admin
tags:
  - TensorFlow
  - AI
  - ML
---

# TensorFlow Maintenance

This chapter is special guide for TensorFlow maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide


### TensorFlow Upgrade

TensorFlow installed by pip, so the upgrade is very easy for it

```
# Active Python virtual environment for TensorFlow
source /data/apps/tensorflow/bin/activate

# Upgrade
pip install -U TensorFlow
```


## Troubleshoot{#troubleshoot}

In addition to the TensorFlow issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  


> Please refer to [official document](https://www.tensorflow.org/install/errors) for more trouble shooting

## FAQ{#faq}

#### How is TensorFlow installed?

Use pip install in the Python virtual environment

#### Is there a web-base GUI database management tools?

Yes, TensorBoard is on it, visit by *http://Internet IP:6006*

#### TensorFlow 实现 GPU 支持需要哪些条件？

需要 NVIDIA® GPU显卡以及驱动程序和工具。详细请参照[TensorFlow GPU 支持软硬件要求](https://www.tensorflow.org/install/gpu)