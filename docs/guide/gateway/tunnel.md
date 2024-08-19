---
sidebar_position: 3.1
slug: /gateway-tunnel
---

# 使用 SSH Tunnel 共享本地服务

[SSH Tunnel](https://github.com/anderspitman/awesome-tunneling) 是一种通过 SSH 协议将位于 NAT 或防火墙后面的本地服务暴露到 Internet 的技术。它通过 TCP/UPD, HTTP/HTTPS 等协议，加密数据传输，绕过防火墙限制，使用户请求能够通过域名转发到内部服务。阅读 [SSH Tunneling and Proxying](https://www.baeldung.com/linux/ssh-tunneling-and-proxying) 了解更多原理。  

使用 SSH Tunnel 共享本地服务，需注意：

- 主要用于非生产场景，开发环境
- 需符合所在国家/地区的法规
- 严禁非法应用使用


## 指南

下面介绍使用 SSH Tunnel 转发应用的几种场景：

### SSH Tunnel 实现域名穿透访问{#tunnel-domain}

当无法为应用准备域名，或本地服务器无法直接提供对外的 HTTP 服务时，采用下面的一条命令即可实现域名穿透访问应用：
```
docker run -it --init --rm --network websoft9 ekzhang/bore local -l <container_name> <container_port> --to bore.pub
```

### SSH Tunnel 实现端口转发{#ssh-port}

当容器的服务端口没有 expose 到宿主机时，可以通过宿主机 ssh 客户端将容器端口转发到宿主机。

1. 使用 `ssh` 连接到服务器（宿主机）

2. 获取容器的 IP 地址
   ```
   docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_name>
   ```

3. 将容器服务转发到宿主机端口，并允许外网访问
   ```
   # ssh -L 0.0.0.0:<host_port>:<container_IP>:<container_port> <user>@localhost
   ssh -L 0.0.0.0:9290:172.18.0.24:8080 root@localhost
   ```
4. 设置成功后，根据服务类型选择访问工具

   - HTTP 应用服务，可以通过本地浏览器访问
   - 数据库 TCP/UDP 服务，可以通过数据库本地客户端连接

## 推荐工具

SSH Tunnel 相关的工具有很多，请根据您的应用场景选择一个合适的：

- [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/)
- [Microsoft Dev tunnels](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/get-started)
- [tunnelmole](https://tunnelmole.com/)
- [bore](https://github.com/ekzhang/bore)
- [ngrok](https://ngrok.com/)
- [frp](https://github.com/fatedier/frp)
- [gost](https://github.com/ginuerzh/gost)

