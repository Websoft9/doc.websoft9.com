---
sidebar_position: 1.3
slug: /gateway-cloudflare
---

# Cloudflare App services

[Cloudflare application services](https://www.cloudflare.com/application-services/products/) is the web app security and delivery services run from a unified, cloud-native platform of security and connectivity solutions. Cloudflare application services help you block DDoS attacks and bad bots, close zero-days and other vulnerabilities, cache and accelerate content, manage APIs, and more.

## Integrated with Websoft9

Cloudflare App services can integrated with Websoft9 to build secure, scalable, highly available web front ends.  

- [Load balancing for backend service at Websoft9](#lb)
- [Proxy to single backend service  at Websoft9](#proxy)


## Load balancing for backend services{#lb}

Cloudflare offers a variety of application services for [load balancing](https://www.cloudflare.com/application-services/products/load-balancing/), which can enhance the performance, reliability, and security of your web applications. Here are some key features and benefits of Cloudflare's load balancing services:  

1. **Global Load Balancing**: Distributes traffic across multiple servers worldwide for improved speed and reduced latency.

2. **Health Checks**: Monitors server health and redirects traffic if a server fails.

3. **Automatic Failover**: Switches traffic to backup servers during primary server outages.

4. **Geo-Steering**: Directs users to the nearest server based on their location.

5. **Session Affinity**: Keeps users connected to the same server for consistent sessions.

## Proxy to single backend service{#proxy}

Cloudflare can provide multi-layered protection and optimization for your single backend service. To achieve this, you simply need to point your domain's DNS settings to Cloudflare and configure your backend service address in Cloudflare's dashboard. This way, all traffic will be forwarded to your backend service through Cloudflare.

In this case, Cloudflare can still provide valuable functionalities:  

1. **DDoS Protection**: Even with a single backend service, Cloudflare can provide robust DDoS protection to prevent malicious traffic attacks.

2. **Web Application Firewall (WAF)**: Cloudflare's WAF can help protect your backend service from common web application attacks such as SQL injection and cross-site scripting (XSS).

3. **SSL/TLS Encryption**: Cloudflare can provide SSL/TLS encryption for your backend service, ensuring that data is secure during transmission.

4. **Content Delivery Network (CDN)**: Cloudflare's CDN can cache static content, reducing the load on your backend service and improving user access speed.

5. **Caching and Optimization**: Cloudflare can cache static content and optimize dynamic content, reducing the load on your backend service and improving performance.

6. **Access Control and Firewall**: Cloudflare offers granular access control and firewall rules, which can restrict access to your backend service and enhance security.

7. **Analytics and Monitoring**: Cloudflare provides detailed analytics and monitoring capabilities, helping you understand traffic patterns and detect potential issues.


## Related topics

- [Cloudflare Tunnel](https://github.com/cloudflare/cloudflared)
