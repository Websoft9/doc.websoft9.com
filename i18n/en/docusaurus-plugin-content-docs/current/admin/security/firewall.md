---
sidebar_position: 1
slug: /security-firewall
---

# Firewall and Security Group

A Linux firewall is a network security tool that control and filter incoming and outgoing data packets, protecting the system from unauthorized access and network attacks.  

## Managing firewalls in Linux

On Linux systems, use tools such as [firewalld](https://firewalld.org/), iptables, and nftables to manage firewalls.    

After installing firewalld, it exists as a daemon on the system.  

## Managing Security Group on cloud{#security}

If there no firewall tool in your Linux system, you can enable **Security Group** on your cloud. Security groups on cloud and Firewalld in Linux both serve to control network traffic.    

Major Cloud platform security group settings for your references:  

* [Azure Security Group](./iaas-azure#security-group)
* [AWS Security Group](./iaas-aws#security-group)
* [Alibaba Cloud Security Group](./iaas-alibabacloud#security-group)
* [HUAWEICLOUD Security Group](./iaas-huaweicloud#security-group)
* [Tencent Cloud Security Group](./iaas-tencentcloud#security-group)

## FAQ

#### How to test if a port is reachable?

Use **nc** or **telnet** commands to test the port more efficiently than viewing the cloud console:  

* nc

    ```
    # Success result
    $ nc -zvw10 8.142.3.195 22
    Connection to 8.142.3.195 22 port [tcp/*] succeeded!

    # Failed result
    $ nc -zvw10 8.142.3.195 9091
    nc: connect to 8.142.3.195 port 9093 (tcp) failed: Connection refused

    ```


* telnet

    ```
    # Success result
    $ telnet 8.142.3.195 22
    Trying 8.142.3.195...
    Connected to 8.142.3.195.
    Escape character is '^]'.

    # Failed result
    $ telnet 8.142.3.195 9091
    Trying 8.142.3.195...
    telnet: Unable to connect to remote host: Connection refused
    ```
