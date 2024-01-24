---
sidebar_position: 2
slug: /backup/websoft9
---

# Websoft9 自身备份

目前 Websoft9 没有提供可视化的自身备份与恢复功能，建议先运行下面的脚步进行备份
```
#!/bin/bash

# 定义备份的目标目录
backup_dir="/path/to/your/backup/directory"

# 创建备份目录，如果它不存在的话
mkdir -p "$backup_dir"

# 列出所有以 websoft9_ 开头的volumes
volumes=$(docker volume ls --format "{{.Name}}" | grep "^websoft9_")

# 遍历找到的volumes
for volume in $volumes; do
    # 创建一个包含日期的备份文件名
    backup_file="$backup_dir/${volume}_backup_$(date +%F).tar.gz"
    
    # 使用docker run创建一个容器，它将挂载volume
    # 并将其内容tar并压缩到指定的备份文件中
    docker run --rm -v "${volume}":/volume -v "${backup_dir}":/backup busybox \
    tar czf /backup/"${backup_file##*/}" -C /volume ./
    
    echo "Volume ${volume} has been backed up to ${backup_file}"
done

echo "All backups have been completed."
```