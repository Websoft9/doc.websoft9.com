---
sidebar_position: 2
slug: /security-ddos
---

# DDoS 防御

分布式拒绝服务攻击(DDoS)是目前黑客经常采用的攻击手段，它的原理是：利用合理的服务请求来占用过多的服务资源，从而导致流量消耗或服务器无法正常对外提供服务。  

DDoS 防御常见的方案是增设 DDoS 防护服务，除此之外也可以在自己的网关层面（HTTP Server）做一定的控制：  

Websoft9 网关是基于 Nginx 的，Nginx 的 DDoS 防御参考官方博客：[Mitigating DDoS Attacks with NGINX and NGINX Plus](https://www.nginx.com/blog/mitigating-ddos-attacks-with-nginx-and-nginx-plus)
