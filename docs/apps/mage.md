---
title: Mage
slug: /mage
tags:
  - 集成数据
  - Mage
---

import Meta from './_include/mage.md';

<Meta name="meta" />

## 入门指南{#guide}

### 登录后台{#wizard}

1. Websoft9 控制台安装 Mage 后，通过 **我的应用** 查看应用详情，在 **访问** 标签页中获取登录信息。  

### 运行 Pipelines 范例{#pipelines}

下面将通过 MySQL 数据表 的迁移来运行 Pipelines：

1. 准备好两个数据库： 源数据库和目标数据库

2. 点击 **New Pipelines > Data intergration**， 输入名称后创建 pipline

3. **Select source** 选择 "MySQL"，在 **Configuration** 填写原数据库的信息（可以通过 **Test connection** 来验证数据库信息是否正确）

4. **Select stream** 中选中你想要迁移的表

5. **Select destination** 选择 "MySQL"，在 **Configuration** 填写目标数据库的信息（可以通过 **Test connection** 来验证数据库信息是否正确）

6. 点击左侧菜单 **Triggers > Run@once > Run now**, 执行完成后对应的表已经导入目标库

## 配置选项{#configs}

- 多语言（×）

## 管理维护{#administrator}

## 故障
