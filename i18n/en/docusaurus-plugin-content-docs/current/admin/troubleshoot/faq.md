---
sidebar_position: 1
slug: /faq
---

# FAQs

Please refer to the FAQ below to resolve your issue, if you cannot find the solution, please contact [Websoft9 support](./helpdesk). 

## Websoft9 Console

#### 500 Internal Server Error?

**Description**: When checking the logs of websoft9-apphub container, 500 Internal Server Error appears.  

**Reason**: The websoft9-apphub container is working abnormally or it can not connect other websoft9 containers  

**Solution**: Run the following commands to check the cause of the error   

    ```
    docker exec -it websoft9-apphub cat /websoft9/apphub/logs/apphub_error.log
    ```

#### Can not open App Store or My Apps?

**Description**: I can login Websoft9 Console, but can not open "App Store" or "My Apps" interface   

**Reason**: websoft9 containers working abnormally or **80** port not enabled

**Solution**: Run the following commands to check the cause of the error   

    ```
    docker logs websoft9-proxy
    docker exec -it websoft9-apphub cat /websoft9/apphub/logs/apphub_error.log
    ```

#### Login Websoft9 failed{#login}

Using multiple reasons can cause login failure:

* Security Group port **9000** not enabled
* Websoft9 installation failed
* Network access failed for your instance
* Local browser's cookie or session
* Your Linux not allowed password login

#### websoft9.service starting failed?

1. Troubleshooting compute resource limit
    ```shell
    # View processes
    ps aux

    # Check disk space
    df -lh

    # View memory usage
    free -lh
    ```

2. Check the error logs
    ```shell
    # View the Websoft9 service container logs
    docker logs websoft9-apphub
    docker logs websoft9-git
    docker logs websoft9-proxy
    docker logs websoft9-deployment

    # View Websoft9 service status and logs
    systemctl status websoft9
    journalctl -u websoft9
    ``

#### Websoft9 can not running at 9000 port?{#portconflict}

Running `netstat -tunlp` to check which process is using port 9000, then free the port with `kill -9 PID`.

#### Docker starting failed?{#dockernotstart}

Running `systemctl status docker` and `journalctl -xe` to check error logs


## Applications

#### Access application 502 error{#nginx502}

502 错误全称为 “Nginx 502 Bad Gateway”。错误不在 Nginx 网关本身，而是 Nginx 转发的后端服务运行异常。  

后端服务异常包括：  

* 计算资源不够
* 后端服务停止运行
* 后端服务端口错误

#### 修改了数据库密码，应用不能访问？

修改了数据库密码，如果应用不能访问。需要通过 **应用编排** 功能中修改应用的 .env 或 docker-compose.yml 中数据库连接信息。  

重建应用后生效。  

#### 容器应用无法远程访问？{#noremote}

导致这个问题的可能原因有三点：

1. 端口没有正确映射到宿主机
2. 容器内部拒绝远程访问
3. 服务器安全组对应的端口没有开放

#### 如何清空应用的容器日志？

```
# 获取容器日志路径
docker inspect --format='{{.LogPath}}' Container_Name

# 清空日志
echo "" > log_path
```

#### 网站访问很慢？{#siteslow}

网站慢最常见的原因包括如下几个方面：

* 访问量太大
* 带宽不够
* 服务器满负荷运转
* 图片、视频、CSS/JS等静态资源太多

经过实践发现，90% 的情况都是由于[网络带宽不够](./install/requirements#network)导致。  

另外针对静态资源较多的情况，我们建议：

1. 采用CDN
2. 网站图片超过1000张，建议从服务器中分离出去

以上方案简单可靠，降低服务器资源消耗，实现成本较低，效果好。


#### 网站重定向错误导致打不开？{#redirect}

**原因分析**：死循环或重定向目标不存在   
**解决方案**：分析网站根目录下的 `.htaccess` 文件，看看有没有死循环规则  

#### 应用网络超时？{#timeout}

在使用 WordPress, ownCloud 等应用时，可能出现打开后台、访问页面、在线升级等操作由于网络原因导致失败。  

常见网络超时场景：  

* 在线升级
* 应用市场安装插件
* 在应用提供商的平台上注册账号
* 程序中的 reCAPTCHA 验证
* Google 地图
* 程序代码中第三方资源（CSS/JS等）
* Docker pull 镜像
* yum / apt 升级 

这些场景的根本原因都是一样的，即：**应用中的服务无法畅通的访问其上游** 。  

结果会导致用户无法获取对应的服务，最后只能接受系统超时的结果。

如何解决呢？  

既然是网络不通导致，而我们又无法对应用提供商服务器的网络做出任何动作。显然，只有从应用或应用所在的服务器网络情况做出应对，才能探索合适的解决方案：

1. 通过 Websoft9 网关的 sub_filter 指令，替换应用中不畅通的 URL
2. 修改应用中的代码，将网络不通的服务替换。例如：更换 Docker 仓库地址。
3. 临时修改应用自身的网络访问，让应用可以直接与应用提供商服务器连通。例如：在 WordPress 中安装代理插件，临时让 WordPress 访问国外的升级服务器。
4. 临时改变自身服务器的网络，使之与应用提供商服务器连通。例如：应用服务器中安装代理客户端，使应用服务器可以通过代理去访问国外升级服务器。

以上提出的方案基本包括涵盖全部场景，但详细操作需根据具体的应用而定。


## Security

#### Websoft9 存在病毒、木马和安全漏洞吗？

Websoft9 在上架到云市场时，已经过严格的安全测试，绝对不会默认存在病毒或木马、后门。  

但需要澄清的是，仅保证**默认**不存在，无法保证后续没有漏洞。原因见下一个问题。  

#### 云平台为什么不定期提示漏洞？

云平台不定期提醒系统有漏洞或潜在威胁，这是什么原因呢？

软件本身是不断升级迭代发展的，漏洞总是从发现到打补丁的循环中不断成长。镜像中包括：操作系统、中间件、数据库、语言等软件包，没一个软件包都有可能有漏洞。

最新的漏洞就会被发现，云平台就会第一时刻通知到用户，这反而是一件好事。

总而言之，软件的安全是动态系统，软件的本质决定没有人能够在安全上做到“万无一失，疏而不漏”。

另外，从商务角度看，云平台会有监管镜像产品的责任，间接的保障用户的安全：

* 合作选择：保证服务商有丰富的云服务器系统维护和环境配置经验，拥有专业的运维团队；
* 流程控制：要求服务商严格遵循《云平台安全审核标准》，只有通过安全审核的镜像才可以售卖；
* 合规机制：要求服务商须与每一个用户签订《镜像使用许可协议》，对镜像安全向用户作出承诺；

## Related topics

除[应用](./apps)自身的故障问题之外，管理员还需关注支持应用的系统组件的故障：  

| 组         | 组件                                                         |
| ---------- | ------------------------------------------------------------ |
| 基础架构   | [Docker](./docker#troubleshoot), [Linux](./linux#troubleshoot)  |
| 数据库   | [MySQL/MariaDB](./mysql/admin#troubleshoot), [SQLSever](./sqlserver/admin#troubleshoot), [PostgreSQL](./postgresql/admin#troubleshoot), [MongoDB](./mongodb/admin#troubleshoot), [Redis](./redis/admin#troubleshoot) |
