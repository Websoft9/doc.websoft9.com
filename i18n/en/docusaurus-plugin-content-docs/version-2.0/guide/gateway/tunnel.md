---
sidebar_position: 3.1
slug: /gateway-tunnel
title: "Share local service to Internet"
---

# Share local service with public URL

[SSH Tunnel](https://github.com/anderspitman/awesome-tunneling)  is a powerful technology and tool to securely open your localhost to the internet and control who has access, so you can easily test and debug your application and database from virtually anywhere. Create, host, and connect to your first dev tunnel in seconds.  

Use SSH Tunnel to share local services with care:

- Mainly used in non-production scenarios, development environments
- Comply with the regulations of your country.
- Use by illegal applications is strictly prohibited.

## Concepts

Three steps to integrate **SSH Tunnel** with Websoft9:  

1. Prepare or register public **SSH Tunnel server** service for Internet

2. Install **SSH Tunnel client** at your host machine and configure it

3. Excuse client command to create public access for any application to Internet

## Tutorial

The following describes several scenarios for sharing application services using SSH Tunnel:

### Share local service with public URL{#tunnel-domain}

If not have domain for Websoft9, or you server can not provide HTTP for Network limit, just run below command to share local service with public URL:  

```
docker run -it --init --rm --network websoft9 ekzhang/bore local -l <container_name> <container_port> --to bore.pub
```

Then, you can use local browser to access application by URL: `http://bore.pub:<port>`  

### Share local service to host port{#ssh-port}

If you container not exposed to host machine, you can use `sss` command to share it to host machine target port: 

1. Use `ssh` to connect server (host machine)

2. Get the container IP address
   ```
   docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_name>
   ```

3. Share container port with host machine and allow any IP access
   ```
   # ssh -L 0.0.0.0:<host_port>:<container_IP>:<container_port> <user>@localhost
   ssh -L 0.0.0.0:9290:172.18.0.24:8080 root@localhost
   ```

4. Use the suitable tool to access your application, e.g

   - For HTTP service, use your local browser
   - For Database service(TCP/UDP), use your local DB client


## More tools

SSH Tunnel 相关的工具有很多，请根据您的应用场景选择一个合适的：

- [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/)
- [Microsoft Dev tunnels](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/get-started)
- [tunnelmole](https://tunnelmole.com/)
- [bore](https://github.com/ekzhang/bore)
- [ngrok](https://ngrok.com/)
- [frp](https://github.com/fatedier/frp)
- [gost](https://github.com/ginuerzh/gost)
