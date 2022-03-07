---
sidebar_position: 2
slug: /xampp/admin
tags:
  - XAMPP
  - DevOps
---


# 维护参考

## 系统参数

本预装包包含 XAMPP 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

| **项** | **路径或说明** |
| :--- | :--- |
| 操作系统 | Windows Server |
| 配置要求 | 最低配置建议1核2G |
| Web服务 | WAMPServer |
| 默认根目录 | C:\xampp\htdocs |
| PHP配置文件 | C:\xampp\php\php.ini |
| Apache虚拟主机文件--根目录对应的文件 | C:\xampp\apache\conf\extra\httpd-vhosts.conf |
| 日志文件 | 请通过XAMPP面板查看 |
| Java安装目录 | C:\Program Files (x86)\Java |
| Tomcat安装目录 | C:\xampp\tomcat Java |
| Tomcat日志文件 | 请通过XAMPP面板查看 |
| Tomcat Manager App | 请通过http://ip/9panel的运维工具进入（登录账号:tomcat/tomcat） |
| Tomcat面板 | 管理地址:http://ip:8080/manager/html（登录账号:tomcat/tomcat） |
| MySQL数据目录 | C:\xampp\mysql |
| MySQL配置文件 | C:\xampp\mysql\my.ini |
| MySQL管理地址 | [http://服务器公网IP/phpmyadmin](http://服务器公网IP/phpmyadmin) |
| 9Panel访问地址 | [http://服务器公网IP/9panel](http://服务器公网IP/9panel) |

### 路径

### 证书

### 端口号

### 版本号

### 服务

*服务随操作系统自动启动，如果手工修改配置参数后，需要重新启停服务。**

*   **方法一**：远程桌面点击XAMPP图标，然后点击需要启动或停止的服务 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xampp/xampp-ss-websoft9.png)
*   **方法二**：打开xampp安装的文件夹，点击对应的服务启停exe/bat文件 
	 MySQL start: \xampp\xampp_start.exe 
     MySQL stop: \xampp\xampp_stop.exe 
     Apache start: \xampp\apache_start.bat 
     Apache stop: \xampp\apache_stop.bat 
     MySQL start: \xampp\mysql_start.bat 
     MySQL stop: \xampp\mysql_stop.bat 
     Mercury Mailserver start: \xampp\mercury_start.bat 
     Mercury Mailserver stop: \xampp\mercury_stop.bat 
     FileZilla Server start: \xampp\filezilla_start.bat 
     FileZilla Server stop: \xampp\filezilla_stop.bat

## 备份

### 全局自动备份

所有的云平台都提供了全局自动备份功能，基本原理是基于**磁盘快照**：快照是针对于服务器的磁盘来说的，它可以记录磁盘在指定时间点的数据，将其全部备份起来，并可以实现一键恢复。

```
- 备份范围: 将操作系统、运行环境、数据库和应用程序
- 备份效果: 非常好
- 备份频率: 按小时、天、周备份均可
- 恢复方式: 云平台一键恢复
- 技能要求：非常容易
- 自动化：设置策略后全自动备份
```

不同云平台的自动备份方案有一定的差异，详情参考 [云平台备份方案](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

### 程序手工备份

程序手工本地备份是通过**下载应用程序源码和导出数据库文件**实现最小化的备份方案。

下面以列表的方式介绍这种备份：
```
- 备份范围: 数据库和应用程序
- 备份效果: 一般
- 备份频率: 一周最低1次，备份保留30天
- 恢复方式: 重新导入
- 技能要求：非常容易
- 自动化：无
```

手工本地备份主要是通过下载应用程序文件和备份导出数据库文件，建议备份周期每月一次，备份文件保存6个月左右。下面就具体的备份操作进行说明：

1. 通过WinSCP将网站目录完整的下载到本地（如果文件数量比较多，建议压缩后再下载） 
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/winscp-download-websoft9.png)
2. 通过浏览器访问：http://公网IP/phpMyAdmin ，进入数据库管理界面)
3. 左侧菜单中选择所需的数据库，顶部导航栏上选择“导出”标签 
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-export-websoft9.png)
4. 选择导出方式和格式（建议SQL），点击“执行”，导出文件后下载到本地
5. 将程序文件和数据库文件放到同一个文件夹，根据日期命名，备份工作完成

## 恢复


## 升级

### 系统级更新

## 故障处理

我们收集使用 XAMPP 过程中最常见的故障，供您参考：
> 服务器相关故障的诊断和解决，与云平台密切相关，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 网站打不开

#### 网站访问慢或不稳定

#### 服务无法启动

#### 数据库连不上


## 常见问题