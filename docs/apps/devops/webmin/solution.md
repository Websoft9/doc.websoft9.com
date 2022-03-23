---
sidebar_position: 2
slug: /webmin/solution
tags:
  - Webmin
  - 虚拟桌面
  - Web 可视化 Linux 管理员工具
---

# 场景方案

## 模块

待研究

## 自动化包

Websoft9 为 Webmin 配套提供了大量基于 Ansible 的[自动化安装包](https://github.com/search?q=org%3AWebsoft9+role_)，您可以很方便的为服务器安装 MySQL, Nginx, PostgreSQL, Java, PHP, Node, Python, Ruby 等基础环境。  

下面以 MySQL 为例进行说明：

1. 找到 MySQL 项目地址，例如：https://github.com/Websoft9/role_mysql

2. 运行下面的命令，开始安装
   ```
   git clone https://github.com/Websoft9/role_mysql.git
   ansible-playbook role_mysql/tests/test.yml
   ```

其他的组件的安装方式是一样的。  