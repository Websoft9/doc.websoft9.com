---
sidebar_position: 2.2
slug: /gateway-proxy
---

# 为应用设置反向代理访问

使用 Websoft9 应用商店部署应用，平台会自动为您的应用生成基于反向代理的域名绑定。   

对于非商店部署的应用，本教程将引导您手动配置反向代理，以实现应用的互联网发布。

Websoft9 支持两种类型的反向代理服务：

- [HTTP 反向代理](#http)
- [TCP/UDP 反向代理](#stream)

## 原理

Websoft9 控制台默认集成 [NPM](https://nginxproxymanager.com/guide/) 作为反向代理服务（Reverse Proxy），作为后端应用与用户之间的访问桥梁。  

反向代理是一种流行的网关服务器工作模式，它允许网关收来自客户端的请求，并将这些请求转发到**后端服务（应用）**。当后端服务处理完这些请求后，网关再将响应返回给客户端。

Websoft9 反向代理服务的工作流程如下：

1. 客户端发送请求到反向代理服务 NPM。
2. NPM 接收到请求后，根据配置决定将请求转发到哪个后端容器服务。
3. 后容器服务处理请求，并将响应返回给 NPM。
4. NPM 再将后端服务器的响应转发给客户端。

## 条件{#pre}

- 开启服务器安全组的 80, 443 端口

- 获取后端服务的**访问地址和端口号**

  - 当后端服务运行在容器中时，**容器名** 作为访问地址，容器端口作为被转发的端口
  - 当后端服务直接运行在服务器中时，**[docker0 网桥](#gateway)** 作为访问地址，后端服务实际端口作为被转发的端口
  - 确保您了解后端服务所使用的协议类型，是 HTTP 还是 TCP/UDP

## 转发 HTTP/HTTPS{#http}

在 Websoft9 托管平台的网关模块中，**Proxy Host** 是专门负责 HTTPS 反向代理功能的一个组件。   

### 快速创建 HTTP 转发（绑定域名）{#create}

1. 进入 Websoft9 控制台 "网关" 模块，依次打开菜单： > "Hosts" > "Proxy Hosts"

2. 点击 "Add Proxy Host"，新建 HTTP 转发

   - Domain Names: 一个或多个域名

   - Scheme：后端服务自身的访问协议（默认 HTTP）

   - Forward Hostname 和 Forward Port 即[后端服务的访问地址和端口号](#pre)

   ![](./assets/websoft9-npm-createhttp.png)
  
3. 点击 "Save" 后，网关中便新增了一个 server 级别的虚拟主机配置。

### 自定义 location 指令{#proxy-location}

Websoft9 网关管理界面支持对已有的 HTTP 转发增加个性化的 location 设置

1. 进入 Websoft9 控制台 "网关" 模块，编辑目标 Proxy Hosts

2. 打开 "Custom Locations" 标签页，开始设置 location, Forward Hostname 等
   ![](./assets/websoft9-npm-addlocations.png)

3. 点击**齿轮图标**显示指令输入框，指令范例如下
    ```
    #proxy_pass http://$server:8080; 
    proxy_http_version 1.1;
    proxy_set_header Host $http_host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    ```

### 自定义 server 级全局指令

Websoft9 网关管理界面支持对已有的 HTTP 设置个性化的 server {} 的全局指令

1. 进入 Websoft9 控制台 "网关" 模块，编辑目标 Proxy Hosts

2. 打开 "Advanced" 标签页，开始设置

3. 下面是一个可以覆盖默认 location / 的全局设置：  

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

### 开启 SSL

参考：[HTTPS 设置指南](./domain-https)

### 设置访问控制

参考：[应用安全访问控制指南](./domain-auth)

## 转发 TCP/UDP {#stream}

在 Websoft9 托管平台的网关模块中，**Streams**  是专门负责 TCP/UDP 方向代理功能的一个组件。

1. 控制台依次打开：【网关】>【Hosts】>【Streams】项

2. 填写好 Incoming Port 以及被转发的 Forward Host 和 Forward Port

> TCP/UDP 转发适用于临时开启数据库类应用的外网访问。 

## 相关操作

### 查看 docker0 网桥地址？{#gateway}

Docker 服务默认会创建一个 docker0 网桥（其上有一个 docker0 内部接口），它在内核层连通了其他的物理或虚拟网卡，这就将所有容器和本地主机都放到同一个物理网络。   

有两种查看 docker0 网桥地址的方法：

- 服务器中运行 `docker network inspect bridge | grep Gateway` 查看
- 打开 Websoft9 控制台，通过："容器">"Networks"，查看 websoft9 网络的 IPV4 Gateway
  ![](./assets/websoft9-container-gateway.png)