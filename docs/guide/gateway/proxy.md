---
sidebar_position: 2.2
slug: /gateway-proxy
---

# 为应用设置反向代理访问

如果您的应用未通过 Websoft9 应用商店部署，本教程将指导您配置反向代理以便将应用发布至互联网。  

支持两种类型的反向代理服务：

- [HTTP 反向代理](#http)
- [TCP/UDP 反向代理](#stream)

## 原理

Websoft9 控制台默认集成 [NPM](https://nginxproxymanager.com/guide/) 作为反向代理服务（Reverse Proxy），作为后端应用与用户之间的访问桥梁。  

反向代理是一种流行的网关服务器工作模式，它允许网关收来自客户端的请求，并将这些请求转发到**后端服务（运行中的应用）**。当后端服务处理完这些请求后，网关再将响应返回给客户端。

Websoft9 反向代理服务的工作流程如下：

1. 客户端发送请求到反向代理服务 NPM。
2. NPM 接收到请求后，根据配置决定将请求转发到哪个后端容器服务。
3. 后容器服务处理请求，并将响应返回给 NPM。
4. NPM 再将后端服务器的响应转发给客户端。

## 条件

- 开启服务器安全组的 80, 443 端口

- 获取后端服务的访问的访问地址和端口号

  - 当后端服务运行在容器中时，**容器名** 可作为访问地址
  - 当后端服务直接运行在服务器中时，Docker 的 **websoft9** 网络作为访问地址
  - 提供后端服务准确的端口号

## 设置 HTTP 转发{#http}

Proxy Host 即一个实现代理转发的**虚拟主机**，它可以将一个运行在服务器或容器内部的应用，通过 Nginx 虚拟主机的 proxy 功能，把应用绑定到域名发布出去，供 Internet 用户访问。  

### 快速创建一个 HTTP 转发

1. 控制台依次打开：【网关】>【Hosts】>【Proxy Hosts】项

2. 点击【Add Proxy Host】，注意重要信息的填写：

   - Domain Names: 一个或多个域名

   - Scheme：应用被代理之前的访问的协议（一般都是 HTTP）

   - Forward Port
      
     - 容器类应用填写容器端口
     - 非容器类应用填写服务器端口

   - Forward Hostname / IP：应用当前可以访问的地址。
     - 容器应用，填写容器名称（container_name）
     - 非容器应用，打开 Websoft9 控制台，通过：【容器】>【Networks】，查看 websoft9 网络的 IPV4 Gateway
       ![](./assets/websoft9-container-gateway.png)

### Proxy Host 的 Advanced 设置{#proxy-advanced}

Advanced 是一个 server 级作用域（非 location / 作用域），但可以自定义 location / 覆盖默认值

下面是一个可以覆盖默认 location / 的全局设置：  

```
location / {
        add_header       X-Served-By $host;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Scheme $scheme;
        proxy_set_header X-Forwarded-Proto  $scheme;
        proxy_set_header X-Forwarded-For    $proxy_add_x_forwarded_for;
        proxy_set_header X-Real-IP          $remote_addr;
        proxy_pass       $forward_scheme://$server:$port$request_uri;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection upgrade;
    }
```

### Proxy Host 增加 Location 指令{#proxy-location}

直接把指令的内容（参考下面的模板）复制到设置框（通过 location 【齿轮】图标打开）

```
proxy_pass http://$server:8080; 
proxy_http_version 1.1;
proxy_set_header Host $http_host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
```

### 为 Proxy Host 设置 HTTPS

Websoft9 的网关支持自动证书和上传证书两种类型，具体参考：[HTTPS 设置指南](./domain-https)

### 应用安全访问控制{#access-auth}

Websoft9 的网关支持密码和白名单等访问控制，具体参考：[应用安全访问控制指南](./domain-auth)

## 设置 TCP/UDP 转发{#stream}

网关的 **Streams** 功能可以设置 TCP/UDP 端口转发，非常合适数据库这种期望临时开启外网访问的应用：  

1. 控制台依次打开：【网关】>【Hosts】>【Streams】项

2. 填写好 Incoming Port 以及被转发的 Forward Host 和 Forward Port
