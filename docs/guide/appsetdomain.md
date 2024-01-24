---
sidebar_position: 1.1
slug: /guide/appsetdomain
---

import DocCardList from '@theme/DocCardList';
import {useCurrentSidebarCategory} from '@docusaurus/theme-common';

# 设置应用的域名

Websoft9 提供了域名和证书配置的图形化界面--[网关](../function/gateway)，大大减轻了用户的负担。  

为应用设置域名（包含HTTPS证书）的前提首先需要：[准备域名](../reference/domain)。域名准备好之后，根据自身的需求完成对应的设置：

## 配置域名

为应用配置域名有两种方式：

- 一次配置，所有应用生效，我们称之为**全局域名**；
- 每个应用单独配置，我们称之为**单设域名**

### 全局域名{#global-domain}

全局域名只需要做一次域名解析和绑定，即可被所有应用使用，具体步骤：

1. 从域名注册服务商的控制台，增加一个**泛域名解析**。假设域名为：websoft9.cn，[泛解析](../reference/domain.md#wildcard)的设置为：  

   - 记录类型：A
   - 主机记录：*.inner  （注意 *. 的使用，这是泛解析的关键）
   - 记录值：服务器公网IP

2. 解析成功后，可以任意使用以 inner.websoft9.com 为**后缀**的子域名。下面是测试范例：  
   ```
   ping app1.inner.websoft9.com
   ping app2.inner.websoft9.com
   ping app3.inner.websoft9.com
   ```

3. 从 Websoft9 控制台的【设置】栏目，设置全局域名
   ![Websoft9 控制台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9/websoft9-settings-globaldomain.png)

4. 进入应用商店的任意一个应用，点击【安装】后会看到全局域名已经被默认关联到应用
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9/websoft9-setdomain-app.png)

5. 输入任意一个应用名称，例如：erpnext，安装过程中就自动为应用绑定了 erpnext.inner.websoft9.cn 这样的域名

### 单设域名{#single-domain}

单设域名即每个应用都需要做一次域名解析和域名绑定操作：

1. 从域名注册服务商的控制台，增加一个**域名解析**。假设域名为：websoft9.cn，解析的设置为：  

   - 记录类型：A
   - 主机记录：wordpress
   - 记录值：服务器公网IP

2. 进入应用商店的任意一个应用，进入【安装】界面后，点击【+添加域名】按钮
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9/websoft9-setdomain-adddomain.png)

3. 绑定所需的域名，安装过程中就自动绑定该域名

## 常见问题

#### 全局域名与单设域名可以同时并存吗？

可以

#### 设置全局域名后，可以指定应用禁用它吗？

可以，在安装应用时点击【禁用】按钮就可

#### 域名必须在安装时绑定吗？

安装后绑定域名实际上就等**同于更换域名**。大部分域名支持在安装后绑定，但也有极少域名不支持安装后绑定
