---
sidebar_position: 3
slug: /webmin/admin
tags:
  - Webmin
  - 虚拟桌面
  - Web 可视化 Linux 管理员工具
---

# 维护参考

## 场景

### 升级

Webmin 提供了可视化的在线升级功能，升级非常方便

![升级](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-upgrade-websoft9.png)

### 卸载

暂无方案

## 故障速查

除以下列出的 Webmin 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 


## 问题解答

#### Webmin 是否支持多语言？

支持（包含中文），控制台自由切换

#### 采用何种方式安装 Webmin ？

采用 rpm/deb 包的安装方式

#### Webmin 中是否包含 Apache？

默认不包含。但本部署方案中我们额外安装了 Apache

#### 新装模块仍在 Un-used Modules 菜单下？

安装模块后，点击【刷新模块】才可将模块自动显示在正常的菜单下

#### HTTP Tunnel 有什么作用？

待研究

#### 如何禁用 Webmin 继承操作系统账号？

默认的【Unix验证】 更改为 【设置为】，同时设置新密码和用户

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-usermode-websoft9.png)

#### 可否命令行修改 Webmin 后台密码？

Webmin 使用的是服务器 root 密码，因此用 `passwd` 系统命令即可