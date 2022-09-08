---
sidebar_position: 1
slug: /administrator/security_insertcode
---

# 代码植入问题处理

代码植入是一种通过将【病毒代码】插入到应用程序或系统程序中的一种伪装方式，它通常有如下几种存在：  

* 应用程序的源码被植入
* 病毒代码以单独的文件夹形式存在
* 数据库的表中被插入数据或代码
* 系统内核被植入，产生病毒常驻进程（不容易被发现）

## 标准流程

虽然以上问题比较棘手，但实际上诊断这些问题存在标准化的流程：

1. 使用类似 [sitecheck.sucuri.net] 这种网站安全分析平台，对网站进行初步分析
2. 手工探索与诊断
   ```
   # 目录全文检索
   grep -r search_term <directory>
   
   # 查看可以进程
   ps -ef
   
   # 查看资源占用
   top
   
   # 查看账号
   cat /etc/passwd
   
   # 查看登录日志
   lastb
   
   # 检测是否有 SSH 隧道（外部绕开正常登录的手段）
   ps -ef | grep -v grep| grep "sshd: root@notty"
   
   # 检查定时任务
   crontab  -l
   ```
3. 使用[Datalog](https://www.datadoghq.com/) 或 [Cloudcare](https://www.cloudcare.cn/) 这种在线的监控平台，对系统进行深度的分析。 

## 范例

下面以 WordPress 为例，介绍系统被代码植入后的处理方案。  

1. 通过在线安全检查网站[sitecheck.sucuri.net](https://sitecheck.sucuri.net)进行排查，初步定义被植入的内容

3. 登录WordPress后台，安装安全插件[Wordfence Scan Enabled](https://wordpress.org/plugins/wordfence/)

5. 运行Wordfence Scan Enabled，启动网站健康检查
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-wordfence-websoft9.png)
   
4. 对于“Critical”标记的结果，手工一一处理

## 工具

其他扫描工具：

1. Quttera Web Malware Scanner 
2. Anti-Malware Security and Brute-Force Firewall 
