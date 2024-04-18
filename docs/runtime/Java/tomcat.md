---
title: Tomcat
slug: /tomcat
tags:
  - Java web 服务器
  - JSP
  - Tomcat
---

import Meta from '../../apps/_include/tomcat.md';

<Meta name="meta" />

## 部署应用{#guide}

### 部署 Tomcat 应用{#deploy}

以 Tomcat 官方示例包来展示部署过程：

1. 进入 Tomcat 容器

2. 进入 web 应用目录并下载示例 war 包
    ```
    cd /usr/local/tomcat/webapps && wget https://tomcat.apache.org/tomcat-10.0-doc/appdev/sample/sample.war
    ```

3. Tomcat会自动解压包，Websoft9 控制台可访问 URL


## 配置选项{#configs}

## 管理维护{#administrator}

## 故障

### Tomcat 配置模板{#tomcattp}

针对 Tomcat 下的 server.xml 文件中的 host 配置段，需要修改的参数说明如下：  

|  host 项  |  作用说明  |  必要性 |
| --- | --- | --- |
|  name  |  域名   |  必须填写 |
|  appBase |  war 包解压路径，例如：在 */data/wwwroot* 下解压 mysite2.war，系统就会自动产生 */data/wwwroot/mysite2* 网站目录  | 务必准确无误 |
|  docBase |  网站存放目录，如果是war包，需带上后缀名，例如:`/data/wwwroot/mysite.war`  | 务必准确无误 |
|  path |  访问路径，一般请保持默认为空  | 建议保持默认 |
