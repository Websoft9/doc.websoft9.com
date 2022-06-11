---
sidebar_position: 100
slug: /cockpit
tags:
  - Web Panel
  - Visualization
  - Cockpit
  - DevOps
---

# Cockpit Getting Started

[Cockpit](https://cockpit-project.org/) is a Linux server panel tool maintained by RedHat. It has a strong open ability and can integrate various applications into the menu of the panel. If you are good at using it, you will find that it is one of the best panels in the container era. 

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cockpit/cockpit-gui-websoft9.png)

If you have installed Websoft9 Cockpit, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:15672** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Cockpit
4. [Get](./user/credentials) default username and password of Cockpit

## Cockpit Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL *http://DNS:15672* or *http://Internet IP:15672*, you will enter installation wizard of Cockpit
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cockpit/cockpit-login-websoft9.png)

2. Log in to Cockpit web console([Don't have password?](./user/credentials))  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cockpit/cockpit-bk-websoft9.png)

3. Set you new password from: 【Users】>【Admin】>【Permissions】>【Update this user】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/cockpit/cockpit-pw-websoft9.png)

> More useful Cockpit guide, please refer to [Cockpit Documentation](https://www.cockpit.com/documentation.html)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## Cockpit  QuickStart{#quickstart}

## Cockpit Setup{#guide}

### 子目录配置域名

Cockpit 配置域名有一定的特殊之处（[方案来源](https://caddy.community/t/example-cockpit/8283)）：

1. 先修改/etc/cockpit/cockpit.conf

```
[WebService]
Origins = https://example.com wss://example.com
ProtocolHeader = X-Forwarded-Proto
UrlRoot=/cockpit
```

2. 然后配置 proxy （以 Caddy 为例）
```
example.com {
    reverse_proxy /cockpit/* localhost:9090 {
        transport http {
            tls_insecure_skip_verify
        }
    }
}
```


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Cockpit 

### Path{#path}

### Port

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9099   | Cockpit 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |


### Version

```shell

```

### Service

```shell
sudo systemctl start | stop | restart | status cockpit
```

### CLI

### API

