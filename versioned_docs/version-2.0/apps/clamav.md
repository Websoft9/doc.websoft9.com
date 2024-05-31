---
title: ClamAV
slug: /clamav
tags:
  - 杀毒
  - 安全防护
  - clamav
---

import Meta from './_include/clamav.md';

<Meta name="meta" />

## 入门指南{#guide}

### 启动扫描

1. 通过控制台 Exec 进入容器

2. 运行下面的扫描命令（sudo 非必须）
   ```
   apk add sudo
   sudo clamscan -ri /scandir --log=myscan.log
   ```
   > myscan.log 为扫描结果，如果包含 Infected files 信息，表明系统有病毒。

## 配置选项{#configs}

- 设置扫描路径：应用编排 .env 文件中的 **W9_SCAN_PATH_SET**
- 扫描命令：clamscan（深度扫描） 与 clamdscan

## 管理维护{#administrator}

## 故障

#### clamscan 没有扫描文件的权限？

需安装 sudo 后，使用 `sudo clamscan` 扫描
