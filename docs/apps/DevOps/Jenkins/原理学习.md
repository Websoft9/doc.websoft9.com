---
sidebar_position: 3
slug: /jenkins/study
tags:
  - Jenkins
  - DevOps
---

# 原理学习

## API

Jenkins 提供可供远程访问的 [类似 REST API](https://www.jenkins.io/doc/book/using/remote-access-api/) 以便更好的实现自动化。

同时，也提供了 Java, Python, Ruby 等语言的 API SDK 开发包。  

## CLI

Jenkins有一个内置的命令行界面，允许用户和管理员从脚本或shell环境中访问Jenkins。这可以方便的编写日常任务, 批量更新, 故障排除等等。  

可以通过SSH 或 Jenkins CLI客户端访问命令行界面, Jenkins分布式的的`.jar` 文件。  

将 *jenkins-cli.jar* 文件下载到 */data/wwwroot* 目录，便可使用：
```
wget -O /data/wwwroot/jenkins/jenkins-cli.jar http://localhost/jnlpJars/jenkins-cli.jar
cd /data/wwwroot
java -jar jenkins-cli.jar -ssh

...................
Neither -s nor the JENKINS_URL env var is specified.
Jenkins CLI
Usage: java -jar jenkins-cli.jar [-s URL] command [opts...] args...
Options:
 -s URL              : the server URL (defaults to the JENKINS_URL env var)
 -http               : use a plain CLI protocol over HTTP(S) (the default; mutually exclusive with -ssh)
 -webSocket          : like -http but using WebSocket (works better with most reverse proxies)
 -ssh                : use SSH protocol (requires -user; SSH port must be open on server, and user must have registered a public key)
 -i KEY              : SSH private key file used for authentication (for use with -ssh)
 -noCertificateCheck : bypass HTTPS certificate check entirely. Use with caution
 -noKeyAuth          : don't try to load the SSH authentication private key. Conflicts with -i
 -user               : specify user (for use with -ssh)
 -strictHostKey      : request strict host key checking (for use with -ssh)
 -logger FINE        : enable detailed logging from the client
 -auth [ USER:SECRET | @FILE ] : specify username and either password or API token (or load from them both from a file);
                                 for use with -http.
                                 Passing credentials by file is recommended.
                                 See https://jenkins.io/redirect/cli-http-connection-mode for more info and options.
```

更多CLI的使用请参考官方文档：[Jenkins CLI ](https://www.jenkins.io/zh/doc/book/managing/cli/)



