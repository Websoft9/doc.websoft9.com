---
sidebar_position: 3
slug: /upgrade/os
---

# 操作系统更新

Linux服务器以及组件的更新，只需要运行一条命令即可完成：  

```
# CentOS or Redhat
sudo yum update -y

# Ubuntu & Debian
apt update && apt upgrade -y
```

> 建议用户将更新命令设置成**计划任务**，实现自动升级。  