---
sidebar_position: 2
slug: /linux/admin
tags:
  - Linux
  - 虚拟桌面
  - Linux 操作系统
  - GNOME
  - KDE
  - Xfce
  - Mate
---

# 维护参考

## 故障处理

此处收集使用 Linux 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何判断端口是否放通？
除了检查本机防火墙和云控制台安全组之外，可以通过 **telnet** 去连接

#### root账户修改文件权限， 报错 "Operation not permitted"，不允许操作
使用root修改文件权限，如下。查看文件属性也不是 i 属性导致。

```
[root@iZ2ze3eh720u9x5c1hdhwyZ yanbian]# chmod 750 index.php
chmod: changing permissions of ‘index.php’: Operation not permitted
[root@iZ2ze3eh720u9x5c1hdhwyZ yanbian]# lsattr index.php
-------------e-- index.php

```

出现这种情况有可能是云平台的安全防护导致。
如 阿里云的云安全中心有【网页防篡改】保护，如果为文件/目录添加了该保护，在系统中修改文件/目录 权限就会被禁止。

![](https://libs.websoft9.com/Websoft9/blog/zh/2020/12/linux-safe-websoft9.png)


#### 磁盘满了如何查询哪些文件比较大？

```
# 查看当前目录下各文件、文件夹的大小
du -h –max-depth=1 *

# 查询当前目录总大小
du -sh

# 显示直接子目录文件及文件夹大小统计值
du -h –max-depth=0 *
```

#### 如何查询服务器日志？

运行命令`tailf /var/log/messages`

#### 服务启动失败怎么办？

当linux服务启动失败的时候，系统会提示我们使用 `journalctl -xe` 命令来查询详细信息，定位服务不能启动的原因。


#### 同一IP反复刷新页面导致服务器403错误处理
mod_evasive是Apache防御攻击的模块，有助于防止DoS、DDoS以及对Apache服务器的暴力攻击。它可以在攻击期间提供规避行动，并通过电子邮件和系统日志工具报告滥用行为。该模块的工作原理是创建一个IP地址和URI的内部动态表，并拒绝以下任何一个IP地址：
- 每秒请求同一页多次
- 每秒对同一个孩子发出50多个并发请求
- 暂时列入黑名单时提出任何要求

如果满足上述任何条件，则发送403响应并记录IP地址。
#### 查看Apache模块清单
```
apachectl -M
```
#### 修改配置项
在conf.d目录下找到mod_evasive.conf文件，进行配置（根据网站安全实际需求来）
![](https://libs.websoft9.com/Websoft9/blog/zh/2020/12/Apache-403-mod_evasive-conf-websoft9.png)

#### PHP extension 与 PHP Package有什么区别？
为了便于理解，我们认为PHP extension是一种编译后的二进制文件，放在php的bin目录下，供所有应用调用
PHP Package是一种源码包，用户的项目若要用到源码包，需要通过Github下载，并引入到自己的项目中，或者通过composer工具下载

#### 字符编码问题
Ubuntu参考：https://help.ubuntu.com/community/Locale

#### Systemd 是可以用于处理开机一次性运行脚本？

可以，将 Tpye=oneshot 即可

```
[Unit]
Description=Switch-off Touchpad

[Service]
Type=oneshot
ExecStart=/usr/bin/touchpad-off

[Install]
WantedBy=multi-user.target
```

#### 如何查询当前服务器的连接数？
```
ps aux | grep httpd | wc -l
```

#### 如何设置 /tmp, /var/tmp 目录的清理策略？

以CentOS为例，修改 */usr/lib/tmpfiles.d/tmp.conf* 即可

#### Linux 系统有哪些时间？

```
$ timedatectl status
Local time: Tue 2021-11-23 10:08:06 CST
Universal time: Tue 2021-11-23 02:08:06 UTC
RTC time: Tue 2021-11-23 10:08:04
    Time zone: Asia/Shanghai (CST, +0800)
    NTP enabled: yes
    NTP synchronized: yes
    RTC in local TZ: yes
    DST active: n/a
```

* Local time: 你自己手表上的时间
* Universal time：世界统一时间
* Real Time Clock：RTC, CMOS or BIOS clock
* System clock：系统时间，开机的时候读取 RTC 时间

NTP 是指网络时间服务，用于校对时间。 