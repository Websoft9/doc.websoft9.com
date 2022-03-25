---
sidebar_position: 3
slug: /codeserver/admin
tags:
  - code-server
  - 在线编辑器
---

# 维护参考

## 故障速查

除以下列出的 code-server 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 

#### code-server 创建文件权限不足？

如果上传的文件存在一些文件权限需要修正。运行如下命令即可解决文件权限问题：
```
chown -R docker.docker /data/wwwroot/codeserver/volumes/config/workspace
```

## 问题解答

#### code-server 容器默认预装哪些组件？

code-server 容器默认已经运行 Node, Yarn, Git等工具，可以很方便的配合 code-server 进行 Node 相关程序的开发。 

#### code-server 是 Microsoft 开发的吗？

不是，它是由一家名为[CODER](https://coder.com/)的公司开发的

#### code-server 支持多账号吗？

不支持，但我们在本部署包中提供了[多开发者方案](/zh/solution-more.md#多开发者)

#### code-server 支持扩展安装吗？

支持

#### 如何退出 code-server 界面？

打开控制台左上角菜单，点击【Log out】即可退出

#### 通过命令行修改 code-server 后台密码？

不支持

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R docker.docker /data/wwwroot/codeserver
# 读写执行权限
find /data/wwwroot/codeserver -type d -exec chmod 750 {} \;
find /data/wwwroot/codeserver -type f -exec chmod 640 {} \;
```

#### 本部署方案中 code-server 是如何安装的？

本部署方案中的 code-server 基于 Docker 安装，实现开发环境与宿主机隔离。
