---
slug: /docker/dockerfile
---

# Dockerfile

Dockerfile 是一个用来构建镜像的文本文件，文本内容包含了一条条构建镜像所需的[指令](https://github.com/docker/cli/blob/master/docs/reference/builder.md)和说明。  

> 理解每个指令的用法是掌握 Docker 技术的关键

具体使用请直接阅读[官方文档](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)。

关于 Dockerfile，下面我们再传递几个重要的观点：

* Dockerfile 是 Docker 运维开发工作的关键
* Dockerfile 文件主要用于编写应用的安装过程
* 应用的初始化过程可以在 Dockerfile 中引入，然后在独立的脚本中编写
* Dockerfile 必须构建成镜像后再供用户使用，直接基于 Dockerfile 运行容器可能会由于网络问题导致无法达成预期目的

指令不仅仅用于设计 Docker 镜像，还有一部分指令与容器运行时密切相关，包括：

* CMD
* ENTRYPOINT
* WORKDIR
* ENV
* USER
* VOLUME


### CMD 和 ENTRYPOINT

它们都是容器启动时运行的指令。

有如下几个关键技术点需要掌握：  

1. CMD 与 ENTRYPOINT 的区别：CMD 直接运行单条命令，ENTRYPOINT 用于运行一个脚本
2. 指令的 Shell 和 Exec 语法模式

  ```
  # Shell 模式
  CMD ping localhost

  # Exec 模式
  CMD ["/bin/ping","localhost"] 
  ```

  可见它们从写法上一种是命令行模式，一种是数组模式。  

  但它们不仅仅写法上不同，更重要的是运行方式不同。  
  
  * CMD 模式相当于调用 Shell 后再运行指令，例如上面的例子实际上相当于： /bin/sh -c "ping localhost"
  * ENTRYPOINT 模式相当于直接运行指令，例如上面的例子实际上相当于： /bin/ping localhost

3. CMD 与 ENTRYPOINT 组合使用：组合使用的时候 CMD 作为 ENTRYPOINT 的一个参数

组合使用 ENTRYPOINT 和 CMD 命令式, 确保你一定用的是 Exec 表示法. 如果用其中一个用的是Shell表示法, 或者一个是Shell表示法, 另一个是Exec表示法, 你永远得不到你预期的效果.

下表列出了如果把Shell表示法和Exec表示法混合, 最终得到的命令行, 可以看到如果有Shell表示法存在, 很难得到正确的效果:

  ```
  Dockerfile    Command

  ENTRYPOINT /bin/ping -c 3
  CMD localhost               /bin/sh -c '/bin/ping -c 3' /bin/sh -c localhost


  ENTRYPOINT ["/bin/ping","-c","3"]
  CMD localhost               /bin/ping -c 3 /bin/sh -c localhost

  ENTRYPOINT /bin/ping -c 3
  CMD ["localhost"]"          /bin/sh -c '/bin/ping -c 3' localhost

  ENTRYPOINT ["/bin/ping","-c","3"]
  CMD ["localhost"]            /bin/ping -c 3 localhost
  ```

从上面看出, 只有ENTRYPOINT 和 CMD 都用 Exec 表示法, 才能得到预期的效果。


### WORKDIR

### ENV

### USER

先看官方的定义：  

The USER instruction sets the user name (or UID) and optionally the user group (or GID) to use when running the image and for any RUN, CMD and ENTRYPOINT instructions that follow it in the Dockerfile.

有几个关键信息：  

* 适用于 RUN, CMD and ENTRYPOINT 三个指令

### VOLUME

对于 VOLUME 申明的目录，容器运行后会自动在 /var/lib/docker/volumes 下创建如下的匿名卷。  

```
/var/lib/docker/volumes/b58ec6901901202b215315db8d958848d910d51dc37c781e29c133064ed5842d
```

当我们运行 `docker-compose down` 删除容器时，匿名卷不会被删除，只有运行 `docker-compose down -v` 才会删除这个卷。
