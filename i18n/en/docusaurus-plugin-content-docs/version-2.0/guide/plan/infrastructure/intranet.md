---
sidebar_position: 1.3
slug: /intranet
---

# Design your network

When managing multiple applications on the Websoft9, constructing a manageable and efficient virtual LAN is essential. Here are key technologies:

1. **Virtual Private Cloud (VPC)**: VPC provides a logically isolated network environment. It allows full control over network configurations, including IP address ranges, subnets, routing tables, and gateways. VPC ensures your applications run in an isolated environment, enhancing security and preventing external network interference.

2. **Virtual Private Network (VPN)**: VPN securely extends your local network to the cloud, creating an encrypted connection between your local network and VPC. This is useful for secure remote access to cloud resources, such as for remote workers or data sharing between branch offices.

3. **Private DNS**: Private DNS is a DNS service visible only within your VPC or specific network environment. Unlike public DNS, it provides domain name resolution for internal network resources without exposing them to the internet. This allows custom domain names for internal resources, unresolvable on the public internet.

4. **Service Discovery**: In microservice architectures, service discovery is crucial. It enables application components to dynamically locate each other at startup. Services can auto-register, and others can query this registry to discover and communicate. Service discovery can be DNS-based or use specialized systems like Consul or Etcd.

Combining these technologies, you can create a secure, flexible multi-application deployment environment. This ensures safe and efficient inter-application connections and data transfers. It helps protect sensitive data and enhances overall system stability and scalability.