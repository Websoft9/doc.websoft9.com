---
sidebar_position: 3
slug: /awx/study
tags:
  - AWX
  - DevOps
---

# 原理学习

awx 是 AWX 和 Red Hat Ansible Tower 的官方命令行客户端。它：

* 使用与AWX HTTP API一致的命名和结构
* 提供一致的输出格式和可选的机器可解析格式
* 在可能的范围内，自动检测AWX和Red Hat Ansible Tower多个版本的API版本，可用的端点和功能支持。

潜在的用途包括：

* 配置和启动作业/剧本
* 检查作业运行的状态和输出
* 管理组织，用户，团队等对象。

更多详情请参考官方文档：[《AWX命令行界面》](https://docs.ansible.com/ansible-tower/latest/html/towercli/index.html)

##  AWX CLI

AWX 官方关于 CLI 是一个通过命令来控制AWX的客户端工具。

#### 安装

```
pip install ansible-tower-cli
```

#### 连接
AWX CLI 需要配置连接信息，方可使用：

```
tower-cli config host http://<new-awx-host.example.com>
tower-cli config username <user>
tower-cli config password <pass>
tower-cli send assets.json
tower-cli user list # 测试是否成功，成功的话显示用户
```

> 更多请参考官方文档： [Ansible Tower AWX CLI ](https://docs.ansible.com/ansible-tower/latest/html/towercli/usage.html#installation)， [ AWX CLI on AWX Github](https://github.com/ansible/awx/tree/devel/awxkit/awxkit/cli/docs)