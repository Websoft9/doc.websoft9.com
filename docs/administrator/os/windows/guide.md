---
sidebar_position: 5
slug: /windows
---

# 指南

## 场景

###  Visual Studio CI/CD

我们知道 Visual Studio 除了是一个广泛支持多种开发语言的代码编辑器之外，它也支持多种生成（构建编译）方案：

* IDE
* CMake
* MSBuild 命令行
* Azure Pipelines

Visual Studio 所有发行版中均包含 MSBuild。在 Visual Studio IDE 中编写代码，使用 MSBuild 来运行生成

详细参考：[docker-visualstudio](https://github.com/Websoft9/docker-visualstudio)

### PHP 集成包

本书所讲述的PHP集成包（用于Windows）包括：WAMP,WAMPServer,phpStudy,XAMPP

选择哪一个集成包，取决于您的需求和偏好，首先我们列出对比：

|  | WAMP | WAMPServer | phpStudy | XAMPP |
| :--- | :--- | :--- | :--- | :--- |
| 支持的语言 | php | php | php | php,java |
| php多版本 | 单一版本 | php5.6/php7.0切换 | php5.2/php5.3/php5.5/php7.0 | 单一版本 |
| PHP扩展安装 | 可以 | 可以 | 可以 | 可以 |
| 应用服务器 | Apache | Apache | Apache+Nginx | Apache+Tomcat |
| 数据库 | MySQL | MySQL | MySQL | MySQL |
| 数据库管理工具 | phpMyAdmin | phpMyAdmin | phpMyAdmin | phpMyAdmin |
| 是否开源 | 开源 | 开源 | 开源 | 开源 |
| 图形化界面 | 是 | 是 | 是 | 是 |
| 是否支持HTTPS | 支持配置 | 支持配置 | 支持配置 | 支持配置 |
| 是否支持多站点 | 支持 | 支持 | 支持 | 支持 |
| 是否支持IP访问 | 支持 | 支持 | 支持 | 支持 |

## 参数

### 路径{#path}

* IIS 网站根目录： *C:\inetpub\wwwroot*

### 端口{#port}

* 远程桌面端口： 3389

### 命令行{#cmd}

Windows 有两个命令 shell：命令 [shell](https://docs.microsoft.com/zh-cn/windows-server/administration/windows-commands/windows-commands) 和 [PowerShell](https://docs.microsoft.com/zh-cn/powershell/scripting/overview)。 每个 shell 是一种软件程序，它提供你与操作系统或应用程序之间的直接通信，同时提供用于自动执行 IT 操作的环境。  

PowerShell 旨在扩展命令行界面的功能，以运行称为 cmdlet 的 PowerShell 命令。 cmdlet 与 Windows 命令类似，但提供更可扩展的脚本语言。 可以在 powershell 中运行 Windows 命令和 powershell cmdlet，但命令 shell 只能运行 Windows 命令，而不能运行 powershell cmdlet。  

为获得最新的最新 Windows 自动化，建议使用 PowerShell，而不是 Windows 命令或 Windows 脚本宿主来实现 Windows 自动化。  

#### Shell

Shell 命令大多数时候与系统中的应用程序直接对应。例如：[msiexec](https://docs.microsoft.com/zh-cn/windows/win32/msi/command-line-options) 即指 [Windows Installer](https://docs.microsoft.com/zh-cn/windows/win32/msi/windows-installer-portal)。

> 静默安装参数（Silent Install  Parameters）是 Windows 自动化安装中最棘手、最重要的活动。  

```
# 安装程序
Msiexec /package Application.msi /quiet
Msiexec /uninstall Application.msi /quiet
Msiexec /update msipatch.msp /quiet
Msiexec /uninstall msipatch.msp /package Application.msi / quiet

# 查询静默安装参数（有些软件不支持）
./Application.exe /?

# 打开记事本
notepad
```



#### PowerShell

PowerShell 既可以用在 Windows，也支持 Linux，PowerShell 使用“动词-名词”名称对来命名 cmdlet。    

先运行下面几个命令做做实验，积累具体的使用经验。  

```
# 查看版本
$PSVersionTable

# 调用集成脚本环境
ise

# 显示帮助
help

# 获取所有的 cmdlet
Get-Command

# 获取所有的 -ParameterName 参数值为 ComputerName 的 cmdlet
Get-Command -ParameterName ComputerName

# 获取所有的命令的动词（谓词）
Get-Verb

# 显示命令帮助
Show-Command Get-EventLog
help Get-EventLog

# 打印当前位置
Get-Location

# 安装 Powershell 软件库
Install-PackageProvider -Name NuGet -Force

```

### 服务{#service}

服务随操作系统自动启动，如果手工修改配置参数后，需要重新启停服务："开始”-> “管理工具”->“服务”中重启服务。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/windows/windows-ssui-websoft9.png)

