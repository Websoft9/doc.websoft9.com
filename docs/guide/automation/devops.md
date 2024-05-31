---
sidebar_position: 3
slug: /automation-devops
---

# 运行 DevOps 作业

自动化在 DevOps 实践中扮演着核心角色，它涉及到从代码提交到软件部署的整个持续集成和持续部署（CI/CD）流程。自动化任务包括代码的自动审查、编译、测试、打包以及最终的部署，这些流程的自动化不仅加快了开发周期，还提高了软件交付的质量和一致性。通过实现DevOps自动化，团队可以减少手动错误，提升协作效率，从而更快地响应市场变化。  

## 条件

- n8n 控制台，"Credentials" 页面中新增 DevOps 流程中计算节点的账号
- 准备基于 git 仓库的项目

## 创建 Git 工作流{#git}

1. 登录到 n8n 控制台，新建一个 Workflow

2. 在 **Add first step** 时，选择 "On a schedule" 作为任务的时间周期设置

3. 接下来选择 **Github** 或 **GitLab** 等作为工作流任务模板

4. 完成后续设置

## 范例参考

以下是来着 n8n 的官方范例：

- [Save resources](https://n8n.io/engineering-resources/)
- [Low-code workflow automation for SecOps](https://n8n.io/secops/)