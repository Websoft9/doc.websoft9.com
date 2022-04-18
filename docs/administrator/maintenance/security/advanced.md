---
sidebar_position: 2
slug: /security/advanced
---

# 常用安全组件使用

服务器的安全是一个看不见但非常重要的要点。

参考阅读：[Linux 服务器的基本安全](https://sollove.com/2013/03/03/my-first-5-minutes-on-a-server-or-essential-security-for-linux-servers/)

#### Fail2ban

Fail2ban 是一个对服务器日子进行监控并采取相应的措施的安全软件。比如：它从日志中发现某个多次尝试登陆但失败的IP，此时它会将其判别为尝试攻击的IP。

#### unattended-upgrades

unattended-upgrades 是一个自动升级补丁的软件。它的工作哲学是与长期未更新的安全漏洞相比，升级的危害相对更小一点。
```
apt-get install unattended-upgrades
vim /etc/apt/apt.conf.d/10periodic
```

#### clamav 基本使用

1.更新病毒库 命令 : freshclam 2\. 扫描: 2.1 扫描所有用户的主目录就使用 clamscan -r /home 2.2 扫描您计算机上的所有文件并且显示所有的文件的扫描结果，就使用 clamscan -r / 2.3 扫描您计算机上的所有文件并且显示有问题的文件的扫描结果， 就使用 clamscan -r –bell -i /

#### LMD 基本使用

扫描:maldet –scan-all /var #扫描 /var 目录

#### rkhunter基本使用

更新:rkhunter –update

扫描恶意软件和检查系统基本安全:rkhunter –check

#### Lynix 基本使用

检测: lynix audit system -Q #检测系统安全问题 并提出一定得建议


