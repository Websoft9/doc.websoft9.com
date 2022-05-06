---
sidebar_position: 1
slug: /java
---

# 指南

## 场景

### Maven 使用{#maven}

下面是一个 Maven  构建的范例：

```
mvn archetype:generate -DgroupId=com.companyname.automobile -DartifactId=trucks -DarchetypeArtifactId=maven-archetype-webapp  -DinteractiveMode=false
```

### Web 框架{#framework}

### JDK 版本变更{#changeversion}

## 故障排除{#troubleshooting}

## 参数

### 路径{#path}

Java 安装目录： */data/java*  
Java 日志目录： */data/logs/java*  
Tomcat 安装目录： */usr/local/tomcat*    
Tomcat 配置文件： */usr/local/tomcat/conf/server.xml*     
Tomcat 建议网站目录： */data/wwwroot/*    
Tomcat 日志目录： */var/log/tomcat*  

### 命令行{#cmd}

下面列出常见的 Java 命令行工具，更多参考[官方文档](https://docs.oracle.com/javase/10/tools/tools-and-command-reference.htm)

* javac：读取 Java 类和接口定义并将它们编译成字节码和类文件。
* javap：反汇编一个或多个类文件。
* javadoc：从 Java 源文件生成 API 文档的 HTML 页面。
* java：启动 Java 应用程序。
* appletviewer：启动 AppletViewer 并在 Web 浏览器之外运行小程序。
* jar：为类和资源创建存档，并从存档中操作或恢复单个类或资源。
* jlink：将一组模块及其依赖项组装和优化为自定义运行时映像。
* jmod：创建 JMOD 文件并列出现有 JMOD 文件的内容。
* jdeps：启动 Java 类依赖关系分析器。
* jdeprscan：静态分析工具，用于扫描 jar 文件（或其他一些类文件的集合）以查找已弃用的 API 元素的使用情况。


### 服务{#service}

```
# Docker
sudo docker start jdk
sudo docker stop jdk
sudo docker restart jdk
sudo docker stats jdk
```

### Tomcat 配置模板{#tomcattp}

针对 Tomcat 下的 server.xml 文件中的 host 配置段，需要修改的参数说明如下：  

|  host 项  |  作用说明  |  必要性 |
| --- | --- | --- |
|  name  |  域名   |  必须填写 |
|  appBase |  war 包解压路径，例如：在 */data/wwwroot* 下解压 mysite2.war，系统就会自动产生 */data/wwwroot/mysite2* 网站目录  | 务必准确无误 |
|  docBase |  网站存放目录，如果是war包，需带上后缀名，例如:`/data/wwwroot/mysite.war`  | 务必准确无误 |
|  path |  访问路径，一般请保持默认为空  | 建议保持默认 |
