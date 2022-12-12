---
sidebar_position: 100
slug: /minio
tags:
  - Web 面板
  - 可视化
  - GUI
---

# 快速入门

MinIO 是全球领先的对象存储先锋，目前在全世界有数百万的用户。 MinIO用作云原生应用程序的主要存储，与传统对象存储相比，云原生应用程序需要更高的吞吐量和更低的延迟。而这些都是MinIO能够达成的性能指标。MinIO利用了Web缩放器的来之不易的知识，为对象存储带来了简单的缩放模型。MinIO 强有力的支持和驱动了很多世界500强的企业。 此外，其部署的多样性和专业性提供了其他软件无法比拟的优势。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/minio/minio-introduct-websoft9.png)

部署 Websoft9 提供的 MinIO 之后，请参考下面的步骤快速入门。

## 准备{#prepare}

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 MinIO 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问 MinIO，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

## MinIO 初始化向导{#wizard}

### 详细步骤

1. 使用本地电脑浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入初始化页面

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/minio/minio-login-websoft9.png)

2. 输入账号密码（不知道账号密码？），进入后台

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/minio/minio-main-websoft9.png)

3. 点击【Create Bucket】，创建新的存储桶

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/minio/minio-bucket-websoft9.png)

4. 上传文件后可以下载和预览
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/minio/minio-upload-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/minio/minio-preview-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/minio/minio-show-websoft9.png)

### 碰到问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。


## MinIO 使用入门{#quickstart}

下面以 **××××** 作为一个任务，帮助用户快速入门：

## MinIO 常用操作{#guide}


## MinIO 参数{#parameter}

MinIO 应用中包含 Docker, Portainer 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。 

通过运行 `docker ps`，查看 MinIO 运行时所有的服务组件：   

```bash
CONTAINER ID   IMAGE                COMMAND                  CREATED         STATUS         PORTS                                                                                  NAMES
685334d0620e   minio/minio:latest   "/usr/bin/docker-ent…"   2 minutes ago   Up 2 minutes   0.0.0.0:9000->9000/tcp, :::9000->9000/tcp, 0.0.0.0:9002->9001/tcp, :::9002->9001/tcp   minio
```

### 路径{#path}

MinIO 安装目录： */data/apps/minio*    

### 端口{#port}

无特殊端口

### 版本{#version}

控制台查看

### 服务{#service}

```shell
sudo docker start | stop | restart | stats minio
```

### 命令行{#cli}

```
$ docker exec -it minio bash
$ curl https://dl.min.io/client/mc/release/linux-amd64/mc \
  --create-dirs \
  -o $HOME/minio-binaries/mc
$ chmod +x $HOME/minio-binaries/mc
$ export PATH=$PATH:$HOME/minio-binaries/

$ mc --help
NAME:                                                                              
  mc - MinIO Client for object storage and filesystems.                            
                                                                                   
USAGE:                                                                             
  mc [FLAGS] COMMAND [COMMAND FLAGS | -h] [ARGUMENTS...]                           
                                                                                   
COMMANDS:                                                                          
  alias      manage server credentials in configuration file                       
  ls         list buckets and objects                                              
  mb         make a bucket                                                         
  rb         remove a bucket                                                       
  cp         copy objects                                                          
  mv         move objects                                                          
  rm         remove object(s)                                                      
  mirror     synchronize object(s) to a remote site                                
  cat        display object contents                                               
  head       display first 'n' lines of an object                                  
  pipe       stream STDIN to an object                                             
  find       search for objects                                                    
  sql        run sql queries on objects                                            
  stat       show object metadata                                                  
  tree       list buckets and objects in a tree format                             
  du         summarize disk usage recursively                                      
  retention  set retention for object(s)                                           
  legalhold  manage legal hold for object(s)                                       
  support    support related commands                                              
  license    license related commands                                              
  share      generate URL for temporary access to an object                        
  version    manage bucket versioning                                              
  ilm        manage bucket lifecycle                                               
  encrypt    manage bucket encryption config                                       
  event      manage object notifications                                           
  watch      listen for object notification events                                 
  undo       undo PUT/DELETE operations                                            
  anonymous  manage anonymous access to buckets and objects                        
  tag        manage tags for bucket and object(s)                                  
  diff       list differences in object name, size, and date between two buckets   
  replicate  configure server side bucket replication                              
  admin      manage MinIO servers                                                  
  update     update mc to latest release                                           
  ready      checks if the cluster is ready or not                                 
  ping       perform liveness check                                                
  od         measure single stream upload and download                             
  batch      manage batch jobs                                                     
                                                                                   
GLOBAL FLAGS:                                                                      
  --autocompletion              install auto-completion for your shell             
  --config-dir value, -C value  path to configuration folder (default: "/root/.mc")
  --quiet, -q                   disable progress bar display                       
  --no-color                    disable color theme                                
  --json                        enable JSON lines formatted output                 
  --debug                       enable debug output                                
  --insecure                    disable SSL certificate verification               
  --help, -h                    show help                                          
  --version, -v                 print the version                                  
                                                                                   
TIP:                                                                               
  Use 'mc --autocompletion' to enable shell autocompletion     
```

### API{#api}
