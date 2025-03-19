---
sidebar_position: 1
slug: /automation-it
---

# 运行服务器计划任务

执行自动化任务是服务器管理中的常规操作，它包括但不限于数据备份、日志清理、时间同步以及安全扫描等任务。这些自动化流程有助于确保服务器的稳定性和安全性，同时提升了管理效率。

## 条件

- n8n 控制台，**Credentials** 页面中新增目标服务器的 SSH 连接账号
- 向目标服务器上传命令脚本（非必须）

## 创建服务器工作流{#server}

1. 登录到 n8n 控制台，新建一个 Workflow

2. 在 **Add first step** 时，选择 **On a schedule** 作为任务的时间周期设置

3. 接下来选择 **ssh** 作为工作流任务模板
   ![](./assets/websoft9-n8n-addssh.png)

4. Action 处选择 **Execute a command**

5. 接下来选择模板服务器的 **credential**

6. 设置所需运行的命令，例如：`ls`

7. 点击 **Test workflow** 验证任务

## 创建容器工作流{#container}

创建容器工作流与[创建服务器工作流](#server)是一致的，只需要设置命令时，使用 `docker exec` 运行容器的任务
