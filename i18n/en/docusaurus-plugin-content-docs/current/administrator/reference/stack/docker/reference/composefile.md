---
slug: /docker/composefile
---

# Compose 文件

[Docker Compose](https://docs.docker.com/compose/) 是官方提供的编排工具，功能强大，简单易用。  

Compose 最重要的莫过于编写编排文件。Docker-compose 文件的编写依赖于丰富的[指令](https://github.com/compose-spec/compose-spec/blob/master/spec.md)，所以理解各个指令的含义是首要的学习目标。 
Docker Compose 文件用于创建互相关联的容器服务，下面是一个典型的 Compose 文件范例。  


```
services:
  frontend:
    image: awesome/webapp
    ports:
      - "443:8043"
    networks:
      - front-tier
      - back-tier
    configs:
      - httpd-config
    secrets:
      - server-certificate

  backend:
    image: awesome/database
    volumes:
      - db-data:/etc/data
    networks:
      - back-tier
    profiles:
      - test

volumes:
  db-data:
    driver: flocker
    driver_opts:
      size: "10GiB"

configs:
  httpd-config:
    external: true

secrets:
  server-certificate:
    external: true

networks:
  # The presence of these objects is sufficient to define them
  front-tier: {}
  back-tier: {}
```

下面我们将对 Compose 文件中所用到的指令进行说明。

## version

version 参数表示使用哪个版本的 compose 语法，一般是向下兼容。  

* version: '2' 表示兼容 2 版本的语法
* version: '3.8' 表示兼容 3.8 版本的语法


## Services

### command

command 指令会覆盖 Dockerfile 中定义的 CMD 变量对应的值。  

例如： command: bundle exec thin -p 3000

除了支持上述单一指令之外，也支持多指令的编写。  

**多指令**

```
version: '3.1'
services:
  db:
    image: postgres
  web:
    build: .
    command:
      - /bin/bash
      - -c
      - |
        python manage.py migrate
        python manage.py runserver 0.0.0.0:8000

    volumes:
      - .:/code
    ports:
      - "8000:8000"
    links:
      - db
```

以上编排中的 command 相当于 docker run 下的：`command: bash -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"`   

如果多指令涉及变量，也可以写成：  

```
    command:
      - /bin/bash
      - -c
      - |
        var=$$(echo 'foo')
        echo $$var # prints foo
```

### entrypoint

entrypoint 用法与 command 类似，也支持多命令。  


### deploy

包含对容器的生命周期、资源约束等的配置项。包括：

* endpoint_mode
* labels
* mode
* placement
* replicas
* resources
* restart_policy
* rollback_config
* update_config

> 更多详情参考官网文档 [deploy](https://github.com/compose-spec/compose-spec/blob/master/deploy.md)

### blkio_config

对块 IO 进行设置的参数项

### cpu

一类对 CPU 资源进行约束设置的参数项，包括：

* cpu_count
* cpu_percent
* cpu_shares
* cpu_period
* cpu_quota
* cpu_rt_runtime
* cpt_rt_period
* cpus
* cpuset

### build

[build](https://github.com/compose-spec/compose-spec/blob/master/build.md) 是基于 Dockerfile 构建镜像后再启动容器服务的一组配置参考。  

build 与 image 可以同时使用，当无法在镜像仓库中找到所需镜像之时，系统便开始构建镜像，且镜像会保持到仓库

```
services:
  frontend:
    image: awesome/webapp
    build: ./webapp

  backend:
    image: awesome/database
    build:
        context: backend
        dockerfile: ../backend.Dockerfile

  custom:
    build: ~/custom
```

与 docker build 命令类似，还有 labels, args 等更多的参数。  

### cap

cap 包含 cap_add, cap_drop 两个参数。它是对 [capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html) 的一种按需设置。在运行容器的时候可以通过指定 --privileded 参数来开启容器的所有CAP，可以通过--cap-add 和 --cap-drop 这两个参数来调整.

> Capabilities 是 Linux 中对 root 用户的特殊权限的一种划分。

```
cap_add
  - ALL
```

等同于

```
--privileded: true
```

### cgroup_parent

Control groups 通常称为 cgroups，是一个 Linux 内核功能，允许将进程组织成可以使用各种类型资源的分层组然后受到限制和监控。内核的 cgroup 接口是通过名为 cgroupfs 的伪文件系统提供。分组在核心 cgroup 内核代码中实现，而资源跟踪和限制在一组每个资源类型中实现子系统（内存、CPU 等）。

> cgroup是对进程分组的一种管理机制，一个cgroup包含一组进程。

故 **cgroup_parent**  即指定容器的父 cgroup 组，继承改组的资源限制。  

### command

这个是一个非常重要的参数。它用于覆盖 Dockerfile 中默认的值，所以使用它之前必须参考 Dockerfile

### configs



### container_name

指定容器名称。否则将会使用默认名称：项目名称_服务名称_序号。项目名称一般为文件夹名称。  

> 一旦指定容器名称后，该服务将由于同名导致无法自动扩展（例如：一次创建3个容器）

### credential_spec

### device_cgroup_rules

### devices

### dns

包括：dns, dns_opt, dns_search, domainname 等几个参数

### entrypoint

这个是一个非常重要的参数。它用于覆盖 Dockerfile 中默认的值，所以使用它之前必须参考 Dockerfile

### environment

环境变量，来源有三种：

* 操作系统环境变量
* Dockerfile 中定义的环境变量
* entrypoint 脚本中所定义或使用的环境变量（不易发现）


支持两种写法：  

```
environment:
  RACK_ENV: development
  SHOW: "true"
  USER_INPUT:


environment:
  - RACK_ENV=development
  - SHOW=true
  - USER_INPUT
```

> environment 中所设定的环境变量的值优先级高于 env_file

### env_file

容器默认启动时，会使用同名目录下的 .env 文件，也支持通过 env_file 参数设置

```
env_file:
  - ./a.env
  - ./b.env
```

值得注意的是，env 文件的格式有严格的要求：

1. 必须采用 var=val 这种写法
2. 字符串标引号和不标引号是不同的字符串

```
# Set Rails/Rack environment
RACK_ENV=development
VAR="quoted"
```

上述 VAR 变量会把引号也传递到容器中，可能会导致容器运行异常。  

### expose

定义容器向外公开的端口，这些端口可以被局域网中其他容器访问。但 expose 不应该绑定到宿主机上。  

```
expose:
  - "3000"
  - "3000"
```

### extends

基于一个相对比较简单的模板进行扩展。例如，我们有下面的一个 common.yml 模板：

```
# common.yml
webapp:
  build: ./webapp
  environment:
    - DEBUG=false
    - SEND_EMAIL=false
```

再编写一个 develop.yml 模板，其中第一个容器集成了上面的模板

```
# develop.yml
develop:
  extends:
    file: common.yml
    service: webapp
  ports:
    - "8000:8000"
  environment:
    - DEBUG=true

db:
  image: postgres
```

### external_links

连接到 docker-compose.yml 文件外部的容器

### extra_hosts

给容器的 /etc/hosts 增加更多的 mappings。格式为 **HOSTNAME:IP**
```
extra_hosts:
  - "somehost: 162.242.195.82"
  - "otherhost: 142.242.195.82"
```

### group_add

### healthcheck

覆盖 Dockerfile 中定义的值。  

### hostname

定义容器主机名

### image

定义镜像，格式为： **仓库URL/镜像:tag**

### init

### ipc

### isolation

### labels

### links

### logging

### networks

### network_mode

### mac_address

### mem

### oom

### pid

### platform

platform 使用 os[/arch[/variant]] 语法定义了此服务将运行的目标平台容器。 Compose 实现在声明时必须使用此属性来确定将拉取哪个版本的图像和/或将在哪个平台上执行服务的构建。

```
platform: osx
platform: windows/amd64
platform: linux/arm64/v8
```

### port

容器与宿主机的端口映射配置，非常重要的参数。  

```
ports:
  - "3000"
  - "3000-3005"
  - "8000:8000"
  - "9090-9091:8080-8081"
  - "49100:22"
  - "127.0.0.1:8001:8001"
  - "127.0.0.1:5000-5010:5000-5010"
  - "6060:6060/udp"
```

长语法模式：  
```
ports:
  - target: 80
    host_ip: 127.0.0.1
    published: 8080
    protocol: tcp
    mode: host
```

### privileged

提供容器用户的特权。如果采用了 user 参数，privileged 便提升 user 对应用户的特权。  

### profiles

类似容器标签，定义的标签的容器默认不会别启动，必须采用 --profile 参数方可运行。  

```
# frontend 默认运行，backend 不会运行
docker-compose up

# frontend 默认运行，backend 也会运行
docker-compose --profile test
```


### pull_policy

拉取镜像的策略，包括：always, never, missing, build 等值

### read_only

### restart 

定义容器的重启策略，支持：no, always, on-failure, unless-stopped 等参数

### runtime

### secrets

### security_opt

### shm_size

### stdin_open

### stop_grace_period

### stop_signal

### storage_opt

### sysctls

定义容器的内核参数

### tmpfs

绑定临时文件

### tty

### ulimits

ulimit是一个内建命令,用于控制由shell启动的进程的可用资源。

### userns_mode  

### volumes

### volumes_from

### working_dir

## Networks

## Volumes

volume 指令是很场景的应用变量，最常见的是基于下面的格式创建一个卷。volumes 设置中的前面部分是宿主机的目录，后面是容器的目录，宿主机的目录无需提前创建


```
volumes: 
  graylog
```

此时，创建的卷存储在 /var/lib/volumes 下。  

如果希望自定义一个卷的路径怎么做？docker-compose 文件中定义如下的 volume，基于它再创建容器：  

```
volumes: 
  graylog:
    driver_opts:
      type: none
      device: /data/graylog
      o: bind
```

发现非常有趣：

1. 显示 Creating volume "docker-graylog_graylog" with default driver，即在 /var/lib/volumes 下创建了卷
2. 自定义的 /data/graylog 也产生了数据 

## Configs


## Secret

## 其他

### YAML anchors
