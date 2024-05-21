---
sidebar_position: 2
slug: /credentials
---


# 用户账号

Websoft9 控制台与 Linux 系统共享同样的账户。  

即，理论上不管是 root 用户，还是普通用户，只要具备登录密码，都可以无障碍的登录到 Websoft9。 

![Websoft9 登录界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9/websoft9-loginpage.png)

## 设置用户

如果服务器上已经有了用户账号，请根据实际情况，进行额外的设置：  

### root 用户

如果 root 账号使用的是密钥对，需额外设置密码：  

1. 使用密钥对登录 Linux
2. 运行命令 `passwd` 为用户设置密码

### 普通用户

如果普通用户使用的是密钥对，需登录 Linux 后运行 `passwd` 设置密码。  

普通用户只要用于密码即可登录 Websoft9 控制台，但需进一步提升权限以方便在控制台进行各种操作。  

**任意**运行下面的提权命令**之一**，为普通用户设置权限：   

```
# 设置 Docker 权限
usermod -aG docker yourusername

# 设置 sudo 权限
usermod -aG sudo yourusername

# 设置 管理员 权限
  usermod -aG wheel yourusername
```

## 新增用户

### 命令行设置

将下面命令的 youruser（两处）和 yourpassword 修改成自己所需的值后，运行到服务器运行即可创建 Websoft9 所需的用户：

  ```
  sudo useradd -m -G docker -s /bin/bash youruser && echo "youruser:yourpassword" | sudo chpasswd
  ```

### 控制台设置

如果以 root 身份登录到 Websoft9 控制台后，可以很方便的增加更多用户：

1. 打开左侧菜单工具组中的【用户账户】页面

2. 点击【创建新账号】，根据引导创建一个用户

3. 再次对新创建的用户进行编辑，用户组项中选中 **docker** 即可
   ![赋予 docker 组权限](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9/websoft9-addgroupdocker.png)