---
sidebar_position: 3
slug: /huaweicloud/advanced
---

# 进阶

## 核心原理

### API/CLI

华为云提供了[原生 API/CLI](https://support.huaweicloud.com/productdesc-hcli/hcli_01.html) 和 OpenStack API/CLI 两种方式。

* [机房编号](https://developer.huaweicloud.com/endpoint)

#### 配置

华为云 CLI 默认的超时和重试设置不太合理，出错不重试，5s就超时。所以运行之前需要修改这些值：  
必要参数：readTimeout, connectionTimeout, retryCount
 
```
{
	"crypter": "3XQfrO2Krn4OeZeA4ZdITnFgIM6q+/+w",
	"nonce": "cvLMpf1hTaCtMadKQI",
	"language": "cn",
	"current": "default",
	"profiles": [
		{
			"name": "default",
			"mode": "AKSK",
			"accessKeyId": "4QUDu1ucWvatP8ZHl4u3a0+8xy",
			"secretAccessKey": "/CkDi1uzeAwMN2Q=",
			"securityToken": "",
			"xAuthToken": "",
			"expiresAt": "",
			"region": "",
			"projectId": "",
			"domainId": "",
			"readTimeout": 20,
			"connectTimeout": 10,
			"retryCount": 5
		}
	]
}
```

另外，需要注意的是，配置文件中的 region、projectId 不要预先设置到配置文件中，以避免CLI无法操作多区域。

* region 在运行CLI命令的时候通过参数带入
* project_id 在运行CLI命令的时候会自动获取

#### 常用命令 

通过 [apiexplorer](https://apiexplorer.developer.huaweicloud.com/) 可以查询常见的命令

```
# 查询公共镜像
hcloud IMS ListImages --cli-region="ap-southeast-1" --__imagetype="gold"

# 创建服务器
hcloud ECS CreatePostPaidServers --cli-region="ap-southeast-1" --server.key_name="websoft9_auto" --server.security_groups.1.id="14e9ce31-0378-4785-8e03-a43ec78f12b9" --server.availability_zone="ap-southeast-1b" --server.vpcid="943bc887-3340-4219-bf9d-8265d8cef1d2" --server.name="test-cdl" --server.nics.1.subnet_id="4105cc19-20dd-4be5-b03c-50734cdf9248" --server.root_volume.volumetype="SSD" --server.flavorRef="c3.large.2" --server.publicip.eip.bandwidth.size=300 --server.publicip.eip.bandwidth.sharetype="PER" --server.publicip.eip.iptype="5_bgp" --server.imageRef="5be19e6d-80ef-4e9d-96a2-ec1b8438065d"

# 查询创建服务器Job状态
hcloud ECS ShowJob --cli-region="ap-southeast-1"  --job_id="ff80808176f756f30177d725bde10842"

# 查询磁盘信息
hcloud ECS ListServerVolumeAttachments --cli-region="ap-southeast-1"  --server_id="24749da9-f15a-4245-8c9f-9a291c7f90f2"

# 查询服务器详情（包含公网IP信息）
hcloud ECS ShowServer --cli-region="ap-southeast-1" --server_id="24749da9-f15a-4245-8c9f-9a291c7f90f2"

# 关闭服务器
hcloud ECS NovaStopServer --cli-region="ap-southeast-1" --server_id="24749da9-f15a-4245-8c9f-9a291c7f90f2" --os-stop.type="SOFT"

# 制作系统盘镜像
 hcloud IMS CreateImage --cli-region="ap-southeast-1" --instance_id="24749da9-f15a-4245-8c9f-9a291c7f90f2" --name="image-name"
 
# 查询镜像信息
hcloud IMS ListImages --cli-region="ap-southeast-1" --__imagetype="private" --name="image-name"

# 跨区域复制镜像
hcloud IMS CopyImageCrossRegion --cli-region="ap-southeast-1" --image_id="2fdf21a6-cf32-4787-9524-18565da42e46" --agency_name="Copy" --name="image-name" --description="Copy from HK" --project_name="cn-north-4" --region="cn-north-4"

# 删除服务器
hcloud ECS DeleteServers --cli-region="ap-southeast-1" --delete_volume=true --servers.1.id="7d178f9b-ecf1-4844-aea2-e41d642afd65" --delete_publicip=true

```


## 问题解答

#### 如何启用Linux系统的root账号？

华为云默认已经开启root账号

#### 如何列出Websoft9在华为云云市场上的所有产品？

通过 [Websoft9华为云店铺](https://marketplace.huaweicloud.com/seller/e57458aa054b430fb2f82a066105f986) 查看我们在华为云上的所有镜像，也可以通过搜索关键字“websoft9”列出

#### 如何通过华为云控制台获取镜像文档？

登录华为云控制台，依次打开：云市场->已购买的服务，列出所有服务以及文档链接
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-getdocfromorder-websoft9.png)

#### 华为云磁盘支持扩容吗？

系统盘和数据盘均支持扩容。当前EVS只支持扩大容量，不支持缩小容量。

#### 如何在无需付出高成本的情况下享受服务器的高带宽（>100M）?

只要服务器的带宽付费方式为**按流量计费**即可享受最大300M的带宽，付费方式是后付费

#### 云硬盘备份与快照的区别？
云硬盘备份以及快照为存储在云硬盘中的数据提供冗余备份，确保高可靠性，两者的主要区别[参考](https://support.huaweicloud.com/productdesc-evs/evs_01_0048.html)

#### 切换操作系统有什么要注意的？

切换操作系统提供以用户选择的镜像进行重装系统的功能。

- 切换操作系统会清除系统盘数据，包括系统盘上的系统分区和所有其它分区，请做好数据备份。
- 切换操作系统成功后云服务器会自动开机。
- 部分操作系统不支持挂载SCSI磁盘，切换操作系统后，可能会导致原弹性云服务器上挂载的SCSI磁盘不可用。查看支持列表。
- 如果云服务器一键式重置密码功能未生效，建议安装密码重置插件开启一键重置密码功能。如何安装。
- 切换操作系统后，当前操作系统内的个性化设置（如DNS、主机名等）将被重置，需重新配置。

#### 如何试用Websoft9的镜像？

部分镜像的商品详情页面提供了官方的演示地址。如果没有演示地址，请按需购买（按小时付费）试用，只需付出几毛钱/小时的成本。

#### 鲲鹏是什么类型的服务器？

鲲鹏原指华为在2019年1月初发布的一款兼容ARM指令集的服务器芯片鲲鹏920，性能强悍，配备了64个物理核心，单核实力从CPU算力benchmark的角度对比，大约持平于同期X86的主流服务器芯片，整体多核多线程算力较同期的X86芯片更强大。 当前鲲鹏的含义已经有所延伸，鲲鹏不再仅仅局限于鲲鹏系列服务芯片，更是包含了服务器软件在新的计算架构平台上的完整软硬件生态和云服务生态。

#### CooCLI 与 OpenStackCLI 有什么区别？

华为云由于使用的是OpenStack架构，原来一直使用 OpenStackCLI，但由于其快速发展，OpenStackCLi 已经无法满足用户的需求，所有华为云自行开发了 KooCLI

#### CLI 创建的秘钥对为什么找不到？

CLI 用户使用的秘钥对必须是CLI用户登录到控制台后创建，其他用户创建的无法使用
