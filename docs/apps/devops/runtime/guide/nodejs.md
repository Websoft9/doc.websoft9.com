---
sidebar_position: 3
slug: /runtime/nodejs
tags:
  - Node.js
  - Node
  - 运行环境
---

# Node.js 应用

## 安装 Node.js 应用

在 Node.js 环境上安装一个网站（应用），也就是我们常说的增加一个虚拟主机。

全局上看，只需三个步骤：**上传网站代码** + **运行NPM命令** + [**虚拟机主机配置文件**](../runtime#path) **中增加 server{} 配置段**

> server{} 又称之为虚拟主机配置段，每个网站必定在 default.conf 中对应唯一的 server{}。

### 删除示例

本部署方案默认已经安装并启动了[Express框架](https://www.expressjs.com.cn/)，我们先删除它：

1. 运行 `npm list` 查询正在运行的Node.js程序
   ```
   ┌────┬────────────────────┬──────────┬──────┬───────────┬──────────┬──────────┐
   │ id │ name               │ mode     │ ↺    │ status    │ cpu      │ memory   │
   ├────┼────────────────────┼──────────┼──────┼───────────┼──────────┼──────────┤
   │ 0  │ www                │ fork     │ 0    │ online    │ 0.1%     │ 48.7mb   │
   ```
2. 运行 `pm2 delete 0` 删除程序
3. 运行 `pm2 save`
4. 删除项目文件夹 `rm -rf /data/wwwroot/express.example.com`
5. 删除初始化
   ```
   //delete the PM2 init script
   pm2 unstartup systemd

   //delete the have been saved PM2 file of process
   rm -rf /root/.pm2
   ```


### 安装 Express

下面我们还原Express的安装过程：

1. 创建目录
   ```
   mkdir myapp
   cd myapp
   ```
2. 创建Express应用骨架
   ···
   npx express-generator
   ···
3. 安装依赖包
   ```
   npm install
   ```
4. 启动应用程序，通过：*http://服务器公网IP:3000* 访问应用
   ```
   DEBUG=myapp:* npm start
   ```

> 你也可以使用pm2管理应用程序

## 维护 Node.js 环境

参考本文档：[《Node.js 指南》](../nodejs) 和 [《Node.js 进阶》](../nodejs/advanced) 



