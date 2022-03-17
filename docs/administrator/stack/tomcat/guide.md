# Tomcat

## 参数

### 路径{#path}

JVM 目录：*/usr/lib/jvm*  
Tomcat 安装目录： */usr/local/tomcat*    
Tomcat 配置文件： */usr/local/tomcat/conf/server.xml*     
Tomcat 建议网站目录： */data/wwwroot/*    
Tomcat 日志目录： */var/log/tomcat*  

### host 模板

针对 Tomcat 下的 server.xml 文件中的 host 配置段，需要修改的参数说明如下：  

|  host 项  |  作用说明  |  必要性 |
| --- | --- | --- |
|  name  |  域名   |  必须填写 |
|  appBase |  war 包解压路径，例如：在 */data/wwwroot* 下解压 mysite2.war，系统就会自动产生 */data/wwwroot/mysite2* 网站目录  | 务必准确无误 |
|  docBase |  网站存放目录，如果是war包，需带上后缀名，例如:`/data/wwwroot/mysite.war`  | 务必准确无误 |
|  path |  访问路径，一般请保持默认为空  | 建议保持默认 |
