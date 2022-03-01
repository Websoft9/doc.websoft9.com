---
sidebar_position: 3
slug: /rabbitmq/study
tags:
  - RabbitMQ 
  - IT 架构
  - 中间件
---

# 原理学习

## CLI

RabbitMQ 提供了强大的的命令行工具 `rabbitmqctl`  

Erlang 语言提供了便捷的开发调试命令行工具 `erl`  

## SSL\TLS通信

RabbitMQ对外提供服务时，为保证通信的安全性，通常使用SSL/TLS加密通信。
对于生成证书，RabbitMQ官网推荐的tls-gen工具，该工具可在MacOS和Linux系统中使用，要求系统中装有openssl和Python 3.5以上版本。
使用tls-gen生成证书：
git clone https://github.com/michaelklishin/tls-gen tls-gen
cd tls-gen/basic

123456是自定义的私钥密码
make PASSWORD=123456
make verify
make info

证书生成完毕后，会在basic目录下生成result、testca、server和client四个文件夹。
通常使用单向认证的方式进行SSL\TLS通信，所需的文件为：
（1）CA的证书文件testca/cacert.cer，C#客户端需要信任签名的CA；
（2）CA证书文件result/ca_certificate.pem，用于服务端配置；
（3）服务端证书文件result/server_certificate.pem，用于服务端配置；
（4）服务端私钥文件result/server_key.pem，用于服务端配置；
（5）客户端证书文件result/client_key.p12，用于客户端。

vi etc/rabbitmq/rabbitmq.conf

限定非SSL\TLS的通信仅可在服务端本地连接
listeners.tcp.default = 127.0.0.1:5672
SSL\TLS通信的端口
listeners.ssl.default = 5671
服务端私钥和证书文件配置
ssl_options.cacertfile = /root/tls-gen/basic/result/ca_certificate.pem
ssl_options.certfile = /root/tls-gen/basic/result/server_certificate.pem
ssl_options.keyfile = /root/tls-gen/basic/result/server_key.pem
有verify_none和verify_peer两个选项，verify_none表示完全忽略验证证书的结果，verify_peer表示要求验证对方证书
ssl_options.verify = verify_peer
若为true，服务端会向客户端索要证书，若客户端无证书则中止SSL握手；若为false，则客户端没有证书时依然可完成SSL握手
ssl_options.fail_if_no_peer_cert = true

根据语言，选择不同的验证方式：
使用Java提供的keytool工具，将服务端证书server_certificate.pem转换为keystore证书文件
使用C#将testca/cacert.cer文件导入受信任的根证书颁发机构