---
title: Java
sidebar_position: 1.0
slug: /java
---


## 配置选项

- JDK 环境应用路径：*/usr/src/app*
- Jetty 环境应用路径：*var/lib/jetty/webapps*
- Tomcat 环境应用路径：*/usr/local/tomcat*
- Tomee 环境应用路径：*/usr/local/tomee*
- [命令行](https://docs.oracle.com/javase/10/tools/tools-and-command-reference.htm)：java, javac, jar, jdeprscan 等
- Java 百科：[Awesome Java](https://github.com/akullpp/awesome-java)
- 包管理器：maven, gradle

## 部署网站{#deploy}

参考：[Web Runtime 入门指南](./runtime)

## 环境管理{#administrator}

- **包管理工具**：安装 maven, gradle 的[范例参考](https://websoft9.github.io/docker-library/apps/openjdk/src/cmd.sh)


## 问题与故障

#### 如何选择 Java 环境？

Java 的开源社区各种力量角逐，蓬勃发展，有多个 JDK 分支和各种有特色的应用程序服务器和中间件。  

Websoft9 提供的 Java 程序环境都运行了 JDK 或 JRE，考虑 Java 生态的多样性，我们让用户有更多合适的选择。

下面我们推荐根据实际场景做出最合适的选择：

- 如果运行一个包含 Web 服务器的 war 程序包，那么请选择 OpenJDK
- 如果运行一个不包含 Web 服务器的 war 程序包，那么请选择 Jetty，Tomcat，Tomee
- 如果只是构建并打包，请选择 Maven

#### JDK 与 JRE 有什么区别？

JRE 是 JAVA 程序运行时，JDK 是 Java 开发者套件。JDK 包含了 JRE。

#### Java 应用程序启动过慢？

这是由于 [java.security 随机数策略导致](https://cloud.tencent.com/developer/article/2016915)

#### 访问 Tomcat 报404 ？

原因：Tomcat 容器应用路径中没有任何 app   
方案：部署自己的 web 应用即可正常访问

#### Jetty 下 war 没解压解？

Jetty 环境下运行 war 包后，并没有在 war 包的路径下看到解压文件。  

其实，这是正常的，因为 Jetty 会将 war 包解压到另外的路径中（与 Tomcat 不同）

