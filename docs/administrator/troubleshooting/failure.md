---
sidebar_position: 3
slug: /troubleshooting/failure
---

# 组件失效故障

## 特征

一个系统的子系统（或组件）失效，会导致周边依赖此系统的其他系统出现故障。

系统（组件）的失效特征包括：不可操作、损坏、无法启动、非计划停止、锁定、商业因素（欠费）、安全事故等

## 故障

#### 服务器无法重启？

主要原因大多数为启动程序出现障碍，请联系云平台官方修复

#### phpMyAdmin 出现 Error during session...错误？

错误原因：PHP 的 session.save_path 路径目录的权限设置不正确。  
解决方案：打开WinSCP，运行如下命令即可  
~~~
chown -R root:nginx /var/lib/php/session
echo 'chown nginx. -R /var/lib/php' >> /etc/cron.daily/0yum-daily.cron
~~~

#### 容器无法启动？

最常见的原因是用户没有按照该容器的要求，设置必须的环境变量，导致容器启动失败

```shell
#查看容器日志，name是容器名称
sudo docker logs name
```

#### Docker service 无法启动？

先通过 `systemctl status docker` 和 `journalctl -xe` 查看错误日志。

* 如果错误日志是  Unit docker.socket entered failed state，表明系统缺少 docker 用户组，运行 `groupadd docker` 增加用户组

#### root 账户修改文件权限， 报错 "Operation not permitted"，不允许操作

使用root修改文件权限，如下。查看文件属性也不是 i 属性导致。

```
$ chmod 750 index.php
chmod: changing permissions of ‘index.php’: Operation not permitted
$ lsattr index.php
-------------e-- index.php
```

出现这种情况有可能是云平台的安全防护导致。例如：阿里云的云安全中心有【网页防篡改】保护，如果为文件/目录添加了该保护，在系统中修改文件/目录 权限就会被禁止。  
![](https://libs.websoft9.com/Websoft9/blog/zh/2020/12/linux-safe-websoft9.png)

