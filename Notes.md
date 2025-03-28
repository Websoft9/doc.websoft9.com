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


#### Action app_from_contentful.yml 自动生成文档需要排除哪些应用？

这个 action 会根据所有 contenful 的产品数据自动在 apps 生成中英文文档。但是由于非docker应用例如：BT，明道已经从当前版本中剔除；环境类应用例如: Python，Ruby 没有放在 apps 目录下，  
需要排除。排除列表请参照: template/meta/skip_file.json

#### build_doc.yml 由于产生 `broken links` 执行失败？

   ```
     Exhaustive list of all broken links found:
    - Broken link on source page path = /docs/apps:
     -> linking to ./phpfpmapache (resolved as: /docs/phpfpmapache)
     -> linking to ./phpfpmnginx (resolved as: /docs/phpfpmnginx)
   ```

由于某些特殊的 app 没有对应的路由，需要排除这些应用。排除列表请参照: template/meta/skip_applink.json


#### Action json2md.yml（Generate Apps list for docs）执行失败？

1. 下载最新的制品 media_latest.zip并解压
2. 查找product_zh.json中【"title": "产品"】，并找出它的appname
3. 需要保证这个app的父catalog不是一级目录
4. 重新更新media制品后action即可正常执行

