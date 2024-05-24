---
sidebar_position: 1.2
slug: /domain-auth
---

# 设置应用的安全访问控制

Websoft9 网关

## 概述

安装应用后，我们发现可能还有更多的安全访问控制需求：

- 有些应用并没有设置密码（例如：Netdata），这样直接暴露给互联网用户是不合理的
- 有些应用只希望开放给部分用户，即白名单

Websoft9 的网关具备为此类应用设置密码或白名单访问，具体步骤如下：

1. 控制台依次打开：【网关】>【Access Lists】

2. 点击【New Access List】，新增一个访问控制项

   - Details: 输入英文名称
   - Authorization：输入账号密码
   - Access：allow 出输入可以访问的[白名单](https://nginx.org/en/docs/http/ngx_http_access_module.html#allow)，0.0.0.0/ 表示允许所有 IP 访问

3. 转到网关的：【Hosts】>【Proxy Hosts】项，编辑应用的配置文件，选择上面配置的 Access
   ![设置 Access](./assets/websoft9-gateway-setaccess.png)
