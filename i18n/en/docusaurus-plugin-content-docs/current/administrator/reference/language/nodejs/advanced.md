---
slug: /nodejs/advanced
---
# 进阶

[Node.js](https://nodejs.org/) 是一个基于 Chrome JavaScript 的运行时平台， 用于方便地搭建响应速度快、易于扩展的网络应用。Node.js 使用事件驱动， 非阻塞I/O 模型而得以轻量和高效，非常适合在分布式设备上运行数据密集型的实时应用。  

## 安装

### 自动安装

使用 Ansible 可以很方便安装由 Websoft9 提供的多版本 Node 安装：  

```
git clone https://github.com/websoft9/role_nodejs
ansible-playbook role_nodejs/tests/test.yml
```

> 项目基于 nvm 安装，支持多版本

### 升级

```
# 升级 NPM
sudo npm install npm -g
```

## 概念与原理

### NPM

NPM 是随同 Node.js 一起安装的包管理工具，能解决 NodeJS 代码部署上的很多问题，常见的使用场景有以下几种：

* 允许用户从NPM服务器下载别人编写的第三方包到本地使用。
* 允许用户从NPM服务器下载并安装别人编写的命令行程序到本地使用。
* 允许用户将自己编写的包或命令行程序上传到NPM服务器供别人使用。

### PM2

PM2是一个用于管理Node.js的进程管理工具。本部署方案默认已经安装了PM2，如果你的服务器没有安装PM2，请参加下面的命令全局安装它：
```
npm install -g pm2
```

进入到项目的根目录，例如：`cd /data/wwwroot/project`， 开始使用pm2管理你的Node.js应用

```
# 启动进程/应用  
pm2 start bin/www 或 pm2 start app.js

# 重命名进程/应用  
pm2 start app.js --name wb123

# 添加进程/应用 
watch  pm2 start bin/www --watch

# 结束进程/应用  
pm2 stop www

# 结束所有进程/应用  
pm2 stop all

# 删除进程/应用  
pm2 delete www

# 删除所有进程/应用  
pm2 delete all

# 列出所有进程/应用  
pm2 list

# 查看某个进程/应用具体情况  
pm2 describe www

# 查看进程/应用的资源消耗情况  
pm2 monit

# 查看pm2的日志  
pm2 logs

# 若要查看某个进程/应用的日志,使用  
pm2 logs www

# 重新启动进程/应用  
pm2 restart www

# 重新启动所有进程/应用  
pm2 restart all
```

### NVM

[nvm](https://github.com/nvm-sh/nvm) 是  Node 的多版本安装与管理工具。

```
# 安装 NVM
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash

# 安装 Node 的最新版本
nvm install node

# 安装 Node 的指定版本
nvm install 6.14.4

# 查询可被安装的版本
nvm ls-remote

# 使用刚安装的版本
nvm run node --version

# 在 subshell 使用指定版本
nvm exec 4.2 node --version

# 查询指定 Node  版本的路径
nvm which 5.0
```

### TypeScript

TypeScript 是 JavaScript 的超集，简单说 TypeScript 具有更丰富的语法特征。 

## 问题解答

#### 如何找到 Node.js 资源？

* [Awesome Node](https://github.com/sindresorhus/awesome-nodejs)
* [Node 中文网](http://nodejs.cn/)

#### NPM 需额外单独安装吗？

不需要，它是 Node 的标配

#### Node.js 环境是否支持部署多个网站？

支持。每增加一个网站，需在**虚拟主机配置文件**中增加配置项。

#### YARN vs NPM？

[Yarn](https://yarnpkg.com/en/) 是在NPM之后推出的一个包管理解决方案

| npm | yarn |
| ---: | :--- |
| npm install | yarn |
| npm install react --save | yarn add react |
| npm uninstall react --save | yarn remove react |
| npm install react --save-dev | yarn add react --dev |
| npm update --save | yarn upgrade |

#### NPM Prevent Permissions Errors？

参考：[Fix NPM permissions](https://www.npmjs.com.cn/getting-started/fixing-npm-permissions/)

#### NPM broken？

尝试运行 `npm cache clean` 命令，若仍然没有解决问题，需更新或重装 NPM

#### 如何安装和管理多个 Node 版本？

使用 [NVM](https://github.com/creationix/nvm) 。 它可以避免权限错误，并解决更新 Node.js 和 npm 的复杂性。