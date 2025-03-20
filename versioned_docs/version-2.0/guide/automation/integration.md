---
sidebar_position: 3
slug: /automation-integration
---

# 集成应用之间的数据

自动化极大地简化了应用间的数据和流程集成，确保了无缝的信息同步与业务流程自动化。这不仅提升了操作效率，减少了人为错误，还显著加快了业务响应速度，增强了系统的整体灵活性。

## 条件

- n8n 控制台，**Credentials** 页面中新增集成流程中应用的账号或 API 秘钥
- 理顺所需集成的数据格式和内容

## 创建 Git 工作流{#git}

1. 登录到 n8n 控制台，新建一个 Workflow

2. 在 **Add first step** 时，选择 **On a schedule** 作为任务的时间周期设置

3. 接下来选择 **Github** 或 **GitLab** 等作为工作流任务模板

4. 完成后续设置
   

## 范例参考

以下是来着 n8n 的官方范例：

- [Automate lead management](https://n8n.io/automate-lead-management/)
- [Supercharge your CRM](https://n8n.io/supercharge-your-crm/)
- [SaaS backend prototyping](https://n8n.io/saas/)
