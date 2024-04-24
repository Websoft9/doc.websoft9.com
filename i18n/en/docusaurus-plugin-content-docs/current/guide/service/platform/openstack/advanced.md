---
sidebar_position: 3
slug: /openstack/advanced
---

# 进阶 

## 核心原理

### API/CLI

[OpenStack CLI](https://docs.openstack.org/python-openstackclient/latest/)是比较通用的云设施命令行工具。    

#### 安装

以Python3环境为例，通过PIP安装 [OpenStack CLI](https://pypi.org/project/python-openstackclient/)

```
pip3 install python-openstackclient
openstack --help
openstack help server create

#更新
pip3 install --upgrade  python-openstackclient

#强制更新
pip3 install --upgrade --force-reinstall python-openstackclient
```


#### 常见命令
```
#先通过 source /root/.huawei/config_zh 引入环境变量，然后再操作下列命令：

#查询服务器型号
openstack flavor list

#列出当前所有服务器
openstack server list

#列出所有区域
openstack region list
+----------------+---------------+-------------+
| Region         | Parent Region | Description |
+----------------+---------------+-------------+
| af-south-1     | None          |             |
| ap-southeast-1 | None          |             |
| ap-southeast-2 | None          |             |
| ap-southeast-3 | None          |             |
| cn-east-2      | None          |             |
| cn-east-201    | None          |             |
| cn-east-3      | None          |             |
| cn-north-1     | None          |             |
| cn-north-4     | None          |             |
| cn-north-9     | None          |             |
| cn-northeast-1 | None          |             |
| cn-south-1     | None          |             |
| cn-southwest-2 | None          |             |
| la-south-2     | None          |             |
| na-mexico-1    | None          |             |
| sa-brazil-1    | None          |             |
+----------------+---------------+-------------+

#以json格式输出所有镜像
openstack image list -f json

#列出所有公共镜像
openstack image list --public

#使华为云CLI环境变量文件生效
        'vm_createVM_template':'source /root/.huawei/config_zh; \
             openstack server create {Template_VMNAME} --flavor {Template_CONFIGURE} \
             --availability-zone ap-southeast-1b --image {Template_IMAGEID} \
             --security-group open-all \
             --key-name websoft9_auto \
             -f value --wait | sed -n \'20p\'',
        
        #为了稳妥起见，等待60s。实践证明等待时间太短，导致后续预装依赖步骤连不上服务器
        'vm_waitforVM_template':'sleep 60s',
        
        'vm_gitIP_template':'source /root/.huawei/config_zh; \
            ipstr=$(openstack floating ip create 0a2228f2-7f8a-45f1-8e09-9039e1d09975 -f value \
            | sed -n \'6p\'); \
            openstack server add floating ip {Template_VMID} $ipstr; \
            echo $ipstr',
        
        'vm_buildImage_template':'source /root/.huawei/config_zh; \
            openstack server image create {Template_VMID} -f json --wait',
        
        #华为云暂无合适的运行命令模块，因此使用fab
        'vm_remotecmd_template':'fab -t 30 runcommand {Template_IP} {Template_USERNAME}',
        
        'vm_deleteVM_template':'source /root/.huawei/config_zh; \
            openstack server delete {Template_VMID} --wait; \
            openstack floating ip delete {Template_IP}',
```


## 常见问题

#### nova 与 openstack 命令有什么区别？

OpenStackClient 项目设有统一命令行客户端（Unified CLI），即 `openstack`  
同时，每一项服务也有一个独立的命令行客户端（Individual CLI）。例如，Compute 服务 `nova`  

#### OpenStack CLI中的port是什么？

port就是虚拟网卡，包括：ID号，MAC地址，内网IP、公网IP等信息。
