---
sidebar_position: 1
slug: /docker
---

# 指南

[Docker](https://www.docker.com)  是轻量级虚拟化技术，可以在原生操作系统上虚拟出多个容器（虚拟机）。同时，Docker 配套镜像机制，可以将容器中所有程序和环境打包成“单一”文件，让软件的安装和运行无缝对接，彻底改变原来开发和运维工作的割裂问题。

## 场景

### 镜像仓库加速{#imagespeed}

如果从 Dockerhub 下载镜像镜像非常慢的话，就需要通过如下的方式修改仓库地址：

1. 选择或获取你喜欢的国内镜像仓库（加速地址）
   ```
   #1 Docker 中文社区
   https://registry.docker-cn.com

   #2 网易仓库
   http://hub-mirror.c.163.com

   #3 腾讯仓库
   https://mirror.ccs.tencentyun.com

   #4 阿里云仓库
   https://f53jxx8r.mirror.aliyuncs.com
   ```
   > 上述阿里云仓库加速地址仅供参考，建议登录控制台后，从后台[获取](https://cr.console.aliyun.com/cn-zhangjiakou/instances/mirrors)获取

2. 修改 */etc/docker/daemon.json* 文件（如果没有可以增加），插入下值
    ```
    {
      "registry-mirrors": ["https://f53jxx8r.mirror.aliyuncs.com"]
    }
    ```

3. 重启服务后生效
    ```
    sudo systemctl daemon-reload
    sudo systemctl restart docker
    ```

4. Docker 支持配置多个仓库地址，类似：
    ```
    {
      "registry-mirrors": ["https://registry.docker-cn.com","https://f53jxx8r.mirror.aliyuncs.com","https://docker.mirrors.ustc.edu.cn","http://hub-mirror.c.163.com"]
    }
    ```

### 远程 API 访问设置{enableapi}

Docker 服务提供了丰富的 API 接口，默认只能在本地以 **socket** 通讯方式访问 API。

```
curl --unix-socket /var/run/docker.sock  http://docker/version
```

如果需添加远程访问 [Docker API](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-socket-option)，需修改 [Docker系统服务](#path)，然后在 **ExecStart** 这一行添加 `-H tcp://0.0.0.0:2375`

```
ExecStart=/usr/bin/dockerd -H fd://   --containerd=/run/containerd/containerd.sock -H tcp://0.0.0.0:2375
```



### 查看容器内部服务

虽然容器内无法使用 systemctl 命令，但是可以使用 service 命令查看和管理服务

```
# 查看所有服务状态
service --status-all

# 管理服务
service apache2 start | status | stop | restart
```

### 重置容器{#resetcontainer}


```
cd /data/apps/appname
docker-compose down -v
docker-compose pull
docker-compose up -d
```


### 单容器升级

以正在运行的 MySQL 容器为例，如果没有持久化卷，容器的升级步骤：

```
#更新镜像
docker pull mysql

#停止容器
docker stop my-mysql-container

#删除容器
docker rm my-mysql-container

#重载容器
docker run --name=my-mysql-container --restart=always \
  -e MYSQL_ROOT_PASSWORD=mypwd -v /my/data/dir:/var/lib/mysql -d mysql
```

### 多容器升级

如果使用的是 Docker-Compose 启动的多个容器，升级只需运行如下三条命令：

```
docker-compose down -v
docker-compose pull
docker-compose up -d
```

### Compose 文件附件初始化命令

有三种运行个性化命令的方式：

* command 实现，例如：command: bundle exec thin -p 3000
* entrypoint 实现，例如：entrypoint: /code/entrypoint.sh
* 多容器共享数据卷实现
  ```
    superset-init:
    image: *superset-image
    container_name: superset_init
    command: ["/app/docker/docker-init.sh"]
    env_file: docker/.env-non-dev
    depends_on: *superset-depends-on
    user: "root"
    volumes: *superset-volumes

  superset-worker:
    image: *superset-image
    container_name: superset_worker
    command: ["/app/docker/docker-bootstrap.sh", "worker"]
    env_file: docker/.env-non-dev
    restart: unless-stopped
    depends_on: *superset-depends-on
    user: "root"
    volumes: *superset-volumes
  ```


## 参数

### 路径{#path}

Docker 根目录: */var/lib/docker*  
Docker 镜像目录: */var/lib/docker/image*   
Docker daemon.json 文件：默认没有创建，请到 */etc/docker* 目录下根据需要自行创建   
Portainer 数据卷：*/var/lib/docker/volumes/portainer_data/_data*    
Docker 系统服务： */lib/systemd/system/docker.service*  

### 端口{#port}

### 版本{#version}

```shell
# Docker Version
docker -v
```
### 服务{#service}

使用由 Websoft9 提供的 Docker 部署方案，可能需要用到的服务如下：

#### Docker 系统服务

```shell
sudo systemctl start docker
sudo systemctl restart docker
sudo systemctl stop docker
sudo systemctl status docker
```

#### Docker-Compose 服务

```
#创建容器编排
sudo docker-compose up

#创建容器编排并重建有变化的容器
sudo docker-compose up -d

#启动/重启
sudo docker-compose start
sudo docker-compose stop
sudo docker-compose restart
```

#### Docker 容器服务

> 终止命令 `stop` 会从进程中释放容器的资源，但不会删除容器

```shell
#示例：mysql
sudo docker pause mysql
sudo docker stop mysql

#示例：redis
sudo docker pause redis
sudo docker stop redis
```


### 命令行{#cmd}
#### Docker 命令

下面是使用 Docker 可能需要用到的常见命令
~~~
systemctl start/stop docker     运行/停止 docker 服务
systemctl enable docker         使 docker 开机自启
docker pull                     从镜像库拉取容器镜像
docker ps                       查看正在运行的容器列表（可以看到容器ID，所映射的端口号等等）
docker ps -a                    查看所有的容器（不管是否运行都能看到）
docker start/stop CONTAINER ID  开始/停止容器（CONTAINER ID 是容器的ID）            
docker rm CONTAINER ID          删除容器
docker stop $(docker ps -aq)    停止所有容器
docker rm $(docker ps -aq)      删除所有容器
docker kill CONTAINER ID        直接关闭容器
docker rmi $(docker images -q) -f 删除所有镜像
docker images  # 查询已下载镜像
~~~

更多详细命令
```
Usage:  docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

Run a command in a new container

Options:
      --add-host list                  Add a custom host-to-IP mapping (host:ip)
  -a, --attach list                    Attach to STDIN, STDOUT or STDERR
      --blkio-weight uint16            Block IO (relative weight), between 10 and 1000, or 0 to disable (default 0)
      --blkio-weight-device list       Block IO weight (relative device weight) (default [])
      --cap-add list                   Add Linux capabilities
      --cap-drop list                  Drop Linux capabilities
      --cgroup-parent string           Optional parent cgroup for the container
      --cgroupns string                Cgroup namespace to use (host|private)
                                       'host':    Run the container in the Docker host's cgroup namespace
                                       'private': Run the container in its own private cgroup namespace
                                       '':        Use the cgroup namespace as configured by the
                                                  default-cgroupns-mode option on the daemon (default)
      --cidfile string                 Write the container ID to the file
      --cpu-period int                 Limit CPU CFS (Completely Fair Scheduler) period
      --cpu-quota int                  Limit CPU CFS (Completely Fair Scheduler) quota
      --cpu-rt-period int              Limit CPU real-time period in microseconds
      --cpu-rt-runtime int             Limit CPU real-time runtime in microseconds
  -c, --cpu-shares int                 CPU shares (relative weight)
      --cpus decimal                   Number of CPUs
      --cpuset-cpus string             CPUs in which to allow execution (0-3, 0,1)
      --cpuset-mems string             MEMs in which to allow execution (0-3, 0,1)
  -d, --detach                         Run container in background and print container ID
      --detach-keys string             Override the key sequence for detaching a container
      --device list                    Add a host device to the container
      --device-cgroup-rule list        Add a rule to the cgroup allowed devices list
      --device-read-bps list           Limit read rate (bytes per second) from a device (default [])
      --device-read-iops list          Limit read rate (IO per second) from a device (default [])
      --device-write-bps list          Limit write rate (bytes per second) to a device (default [])
      --device-write-iops list         Limit write rate (IO per second) to a device (default [])
      --disable-content-trust          Skip image verification (default true)
      --dns list                       Set custom DNS servers
      --dns-option list                Set DNS options
      --dns-search list                Set custom DNS search domains
      --domainname string              Container NIS domain name
      --entrypoint string              Overwrite the default ENTRYPOINT of the image
  -e, --env list                       Set environment variables
      --env-file list                  Read in a file of environment variables
      --expose list                    Expose a port or a range of ports
      --gpus gpu-request               GPU devices to add to the container ('all' to pass all GPUs)
      --group-add list                 Add additional groups to join
      --health-cmd string              Command to run to check health
      --health-interval duration       Time between running the check (ms|s|m|h) (default 0s)
      --health-retries int             Consecutive failures needed to report unhealthy
      --health-start-period duration   Start period for the container to initialize before starting health-retries countdown (ms|s|m|h) (default 0s)
      --health-timeout duration        Maximum time to allow one check to run (ms|s|m|h) (default 0s)
      --help                           Print usage
  -h, --hostname string                Container host name
      --init                           Run an init inside the container that forwards signals and reaps processes
  -i, --interactive                    Keep STDIN open even if not attached
      --ip string                      IPv4 address (e.g., 172.30.100.104)
      --ip6 string                     IPv6 address (e.g., 2001:db8::33)
      --ipc string                     IPC mode to use
      --isolation string               Container isolation technology
      --kernel-memory bytes            Kernel memory limit
  -l, --label list                     Set meta data on a container
      --label-file list                Read in a line delimited file of labels
      --link list                      Add link to another container
      --link-local-ip list             Container IPv4/IPv6 link-local addresses
      --log-driver string              Logging driver for the container
      --log-opt list                   Log driver options
      --mac-address string             Container MAC address (e.g., 92:d0:c6:0a:29:33)
  -m, --memory bytes                   Memory limit
      --memory-reservation bytes       Memory soft limit
      --memory-swap bytes              Swap limit equal to memory plus swap: '-1' to enable unlimited swap
      --memory-swappiness int          Tune container memory swappiness (0 to 100) (default -1)
      --mount mount                    Attach a filesystem mount to the container
      --name string                    Assign a name to the container
      --network network                Connect a container to a network
      --network-alias list             Add network-scoped alias for the container
      --no-healthcheck                 Disable any container-specified HEALTHCHECK
      --oom-kill-disable               Disable OOM Killer
      --oom-score-adj int              Tune host's OOM preferences (-1000 to 1000)
      --pid string                     PID namespace to use
      --pids-limit int                 Tune container pids limit (set -1 for unlimited)
      --platform string                Set platform if server is multi-platform capable
      --privileged                     Give extended privileges to this container
  -p, --publish list                   Publish a container's port(s) to the host
  -P, --publish-all                    Publish all exposed ports to random ports
      --pull string                    Pull image before running ("always"|"missing"|"never") (default "missing")
      --read-only                      Mount the container's root filesystem as read only
      --restart string                 Restart policy to apply when a container exits (default "no")
      --rm                             Automatically remove the container when it exits
      --runtime string                 Runtime to use for this container
      --security-opt list              Security Options
      --shm-size bytes                 Size of /dev/shm
      --sig-proxy                      Proxy received signals to the process (default true)
      --stop-signal string             Signal to stop a container (default "SIGTERM")
      --stop-timeout int               Timeout (in seconds) to stop a container
      --storage-opt list               Storage driver options for the container
      --sysctl map                     Sysctl options (default map[])
      --tmpfs list                     Mount a tmpfs directory
  -t, --tty                            Allocate a pseudo-TTY
      --ulimit ulimit                  Ulimit options (default [])
  -u, --user string                    Username or UID (format: <name|uid>[:<group|gid>])
      --userns string                  User namespace to use
      --uts string                     UTS namespace to use
  -v, --volume list                    Bind mount a volume
      --volume-driver string           Optional volume driver for the container
      --volumes-from list              Mount volumes from the specified container(s)
  -w, --workdir string                 Working directory inside the container
```

#### Docker Compose 命令

```
$docker-compose -h

Define and run multi-container applications with Docker.

Usage:
  docker-compose [-f <arg>...] [--profile <name>...] [options] [--] [COMMAND] [ARGS...]
  docker-compose -h|--help

Options:
  -f, --file FILE             Specify an alternate compose file
                              (default: docker-compose.yml)
  -p, --project-name NAME     Specify an alternate project name
                              (default: directory name)
  --profile NAME              Specify a profile to enable
  -c, --context NAME          Specify a context name
  --verbose                   Show more output
  --log-level LEVEL           Set log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
  --ansi (never|always|auto)  Control when to print ANSI control characters
  --no-ansi                   Do not print ANSI control characters (DEPRECATED)
  -v, --version               Print version and exit
  -H, --host HOST             Daemon socket to connect to

  --tls                       Use TLS; implied by --tlsverify
  --tlscacert CA_PATH         Trust certs signed only by this CA
  --tlscert CLIENT_CERT_PATH  Path to TLS certificate file
  --tlskey TLS_KEY_PATH       Path to TLS key file
  --tlsverify                 Use TLS and verify the remote
  --skip-hostname-check       Don't check the daemon's hostname against the
                              name specified in the client certificate
  --project-directory PATH    Specify an alternate working directory
                              (default: the path of the Compose file)
  --compatibility             If set, Compose will attempt to convert keys
                              in v3 files to their non-Swarm equivalent (DEPRECATED)
  --env-file PATH             Specify an alternate environment file

Commands:
  build              Build or rebuild services
  config             Validate and view the Compose file
  create             Create services
  down               Stop and remove resources
  events             Receive real time events from containers
  exec               Execute a command in a running container
  help               Get help on a command
  images             List images
  kill               Kill containers
  logs               View output from containers
  pause              Pause services
  port               Print the public port for a port binding
  ps                 List containers
  pull               Pull service images
  push               Push service images
  restart            Restart services
  rm                 Remove stopped containers
  run                Run a one-off command
  scale              Set number of containers for a service
  start              Start services
  stop               Stop services
  top                Display the running processes
  unpause            Unpause services
  up                 Create and start containers
  version            Show version information and quit
```

### 模板{#template}

#### docker-compose 模板

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
#### dockerfile 模板