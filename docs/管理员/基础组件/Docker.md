---
sidebar_position: 1
---

# Docker

## 常见问题

#### 如何查看容器中的所有服务状态？

虽然容器无法使用 systemctl 命令，但是可以使用 service 命令管理服务

```
# 查看所有服务状态
service --status-all

# 管理服务
service apache2 start | status | stop | restart
```

