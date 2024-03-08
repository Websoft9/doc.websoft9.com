# 创作指南

## 文档10个原则

* 可维护是文档进化第一任务，也就是说允许使用上的“不直观”出现
* 向编程序一样设计文档的：组件、接口
* 文档满足三层技术体系
* 通用方案参考+特殊要素清单=特殊解决方案。例如：特殊 Nginx 配置只需列出配置文件模板，而不用再次阐述步骤
* 路由不超过两层结构

## 常见问题

#### 多层链接有哪些？

```
./../administrator/firewall#security
../
./
```

#### 异常有哪些参数类型？

Type: 'ignore' | 'log' | 'warn' | 'throw'

#### Action json2md.yml（Generate Apps list for docs）执行失败？

1. 下载最新的制品 media_latest.zip并解压
2. 查找product_zh.json中【"title": "产品"】，并找出它的appname
3. 需要保证这个app的父catalog不是一级目录
4. 重新更新media制品后action即可正常执行

