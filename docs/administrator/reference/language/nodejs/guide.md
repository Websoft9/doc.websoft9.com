---
sidebar_position: 1
slug: /nodejs
---

# 指南

我们知道 JavaScript 可以作为前端直接在浏览器端使用，也是以 [Node](https://nodejs.org/) 作为运行时的后端语言。  
本文档围绕 JavaScript 作为后端的场景进行说明。

## 场景

### 开启外网访问

开启 Node 应用的外网访问，主要通过 --host 实现，--port 可以指定端口

```
npm run start -- --host 0.0.0.0  --port 3002
```

### Node 版本变更{#changeversion}

### 框架{#framework}

#### Express{#express}
#### Vue{#vue}
#### React{#react}
#### AngularJS{#angular}
#### Nuxt{#nuxt}
#### Next{#next}
#### Koa{#koa}
#### Vuepress{#vuepress}
#### Gatsby.js{#gatsby}

## 故障排除{#troubleshooting}

## 参数

### 路径{#path}

与 Node 相关的组件目录如下：

Node.js 模块目录: */usr/lib/node_modules*  
Node.js 应用安装目录: */data/wwwroot*  
Express 示例目录: */data/wwwroot/express.example.com*  
Node.js 日志文件: */root/.pm2/pm2.log*  

### 版本号{#checkversion}

下面的命令用于查看 Python 相关的版本号

```shell
# Node.js  Version
node -v

# PM2  Version
pm2 -V

# NPM version
npm -v

# yarn version
yarn --version
``````

### 服务{#service}

```shell
# PM2
systemctl start pm2-root
systemctl stop pm2-root
systemctl restart pm2-root
systemctl status pm2-root
```

### 命令行{#cmd}

主要包括 node, nvm, npm, yarn, pm2 等命令