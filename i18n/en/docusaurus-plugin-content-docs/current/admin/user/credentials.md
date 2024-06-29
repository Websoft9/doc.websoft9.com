---
sidebar_position: 2
slug: /credentials
---


# 用户账号

Websoft9 控制台与 Linux 系统共享同样的账户，使用系统的 PAM（可插拔认证模块）进行身份验证。  

即，理论上不管是 root 用户，还是普通用户，只要具备登录密码，都可以无障碍的登录到 Websoft9。 

请选择下面的一种用户账号方式：  

## 将 root 转为 Websoft9 用户{#convert-root}

root 用户已经是具有最高权限的 Websoft9 账号：

- 如果 root 账号使用密码，直接使用账号密码登录 Websoft9
- 如果 root 账号使用密钥对，需 SSH 连接到 Linux，运行命令 `sudo passwd root` 设置密码后再登录 Websoft9

## 将普通用户转为 Websoft9 用户{#convert-normal}

针对于普通用户，请根据下面的步骤检查或设置为可以登录 Websoft9 的账号：

- 如果使用密钥对，需 SSH 连接到 Linux，运行命令 `passwd` 设置密码

- 如果普通用户不具备 **Docker | sudo | 管理员** 权限之一，需运行下面**对应的**赋权命令：   
    ```
    # 设置 Docker 权限（推荐）
    usermod -aG docker yourusername

    # 设置 sudo 权限
    usermod -aG sudo yourusername

    # 设置 管理员 权限
    usermod -aG wheel yourusername
    ```

## 新增用户{#add}

### 在 Websoft9 控制台新增用户（推荐）{#add-console}

1. 登录到 Websoft9 控制台后，通过左侧菜单工具组，打开 **用户账户** 页面

2. 点击**创建新账号**，根据引导创建一个用户，并设置密码

3. 对新建用户进行编辑操作，为**用户组**多选拉下项设置为 **docker**
   ![赋予 docker 组权限](./assets/websoft9-addgroupdocker.png)

### 使用命令行新增用户{#add-command}

1. 使用 `root` 账号 SSH 连接到服务器

2. 运行下面的新增用户命令，其中 youruser（两处）和 yourpassword 需提前修改成自己所需的值
    ```
    sudo useradd -m -G docker -s /bin/bash youruser && echo "youruser:yourpassword" | sudo chpasswd
    ```


