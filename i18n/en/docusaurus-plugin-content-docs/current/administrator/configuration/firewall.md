---
sidebar_position: 7
slug: /administrator/firewall
---

# Firewall and Security Group

## About Firewall

In Linux, the firewall exists as a daemon process, the name of the service is firewalld , which can define a set of rules to control the network access of the external incoming system.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/firewalld-gui-websoft9.png)

## Security Group Settings{#security}

However, in order to simplify the security use, the cloud platform achieves the same function as the firewall through a visual management interface-**security group**.

Therefore, when using a cloud server, the firewall will be turned off and replaced with a security group.   

* [Azure Security Group](../azure#securitygroup)
* [AWS Security Group](../aws#securitygroup)
* [Alibaba Cloud Security Group](../alibabacloud#securitygroup)
* [Tencent Cloud Security Group](../tencentcloud#securitygroup)
* [HUAWEI Cloud Security Group](../huaweicloud#securitygroup)

## FAQ

#### How to test the port is enabled?

You can use **nc** or **telnet** to test it:  

* Use `nc` 

    ```
    # Success
    $ nc -zvw10 8.142.3.195 22
    Connection to 8.142.3.195 22 port [tcp/*] succeeded!

    # Failed
    $ nc -zvw10 8.142.3.195 9091
    nc: connect to 8.142.3.195 port 9093 (tcp) failed: Connection refused

    ```


* Use `telnet` 

    ```
    # Success
    $ telnet 8.142.3.195 22
    Trying 8.142.3.195...
    Connected to 8.142.3.195.
    Escape character is '^]'.

    # Failed
    $ telnet 8.142.3.195 9091
    Trying 8.142.3.195...
    telnet: Unable to connect to remote host: Connection refused
    ```
