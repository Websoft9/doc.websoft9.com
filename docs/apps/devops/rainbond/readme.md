---
sidebar_position: 100
slug: /rainbond
tags:
  - Web 面板
  - 可视化
  - GUI
---

# 快速入门

Rainbond 是一个云原生应用管理平台，使用简单，不需要懂容器、Kubernetes和底层复杂技术，支持管理多个Kubernetes集群，和管理企业应用全生命周期。主要功能包括应用开发环境、应用市场、微服务架构、应用交付、应用运维、应用级多云管理等。
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rainbond/rainbond-main-websoft9.png)

部署 Websoft9 提供的 Rainbond 之后，请参考下面的步骤快速入门。

## 准备{#prepare}

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80,7070** 端口已经开启
3. 在服务器中查看 Rainbond 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问 Rainbond，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

## Rainbond 初始化向导{#wizard}

### 详细步骤

1. 使用本地电脑浏览器访问网址：*http://域名:7070* 或 *http://服务器公网IP*, 进入初始化页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rainbond/rainbond-login-websoft9.png)

2. 输入用户名和密码登陆到后台(user:admin password:admin123)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rainbond/rainbond-main-websoft9.png)

### 碰到问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

## Rainbond 使用入门{#quickstart}

下面以 **Rainbond 部署JAVA运行环境** 作为一个任务，帮助用户快速入门：

1. 登陆 Rainbond 后台，点击【新增】-> 【从镜像构建】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rainbond/rainbond-createapp-websoft9.png)

2. 点击【新建应用】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rainbond/rainbond-newapp-websoft9.png)

3. 输入应用名称，并创建tomcat组件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rainbond/rainbond-createok-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rainbond/rainbond-tomcat-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rainbond/rainbond-tomcat2-websoft9.png)

4. 选中tomcat组件，并开放对外端口
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rainbond/rainbond-tomcatclick-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rainbond/rainbond-tomcatport-websoft9.png)

5. JAVA运行环境部署成功，可以访问tomcat了
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rainbond/rainbond-complete-websoft9.png)

## Rainbond 常用操作{#guide}


## 参数{#parameter}

Rainbond 应用中包含 Docker, Portainer 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。 

通过运行 `docker ps`，查看 Rainbond 运行时所有的服务组件：   

```bash
CONTAINER ID        IMAGE                                                                        COMMAND                  CREATED             STATUS              PORTS                    NAMES
48fd6d055987        registry.cn-hangzhou.aliyuncs.com/goodrain/pause:3.2                         "/pause"                 3 hours ago         Up 3 hours                                   k8s_POD_app-2c5561f2-tomcat-6f6c486786-8sbzp_7206225c648043db8a8af3f61bd70ed9_859d87f9-63eb-4446-94df-69a75c9b1d1a_0
a950caf06213        registry.cn-hangzhou.aliyuncs.com/goodrain/rbd-worker                        "/run/entrypoint.sh …"   3 hours ago         Up 3 hours                                   k8s_rbd-worker_rbd-worker-5779b7985b-hnrjl_rbd-system_7ca6da4a-95c3-4970-8109-5d57a30ca0e1_0
e23bc11e7625        registry.cn-hangzhou.aliyuncs.com/goodrain/rbd-eventlog                      "/run/entrypoint.sh …"   3 hours ago         Up 3 hours                                   k8s_rbd-eventlog_rbd-eventlog-0_rbd-system_f55dcd27-eec2-454f-bb95-bc0f2f1e50e6_0
e167393d98a6        registry.cn-hangzhou.aliyuncs.com/goodrain/mysqld-exporter                   "/bin/mysqld_exporter"   3 hours ago         Up 3 hours                                   k8s_rbd-db-exporter_rbd-db-0_rbd-system_5c8af9af-42be-4e89-8f1c-03cb28882ea3_0
ce39424878fa        registry.cn-hangzhou.aliyuncs.com/goodrain/rbd-api                           "/run/entrypoint.sh …"   3 hours ago         Up 3 hours                                   k8s_rbd-api_rbd-api-6f79cff696-2vz5p_rbd-system_1e60e3ff-8c87-4d38-a678-c4fe5960b3e8_0
4d62fc61d231        registry.cn-hangzhou.aliyuncs.com/goodrain/rbd-mq                            "/run/entrypoint.sh …"   3 hours ago         Up 3 hours                                   k8s_rbd-mq_rbd-mq-65975b5cd5-rklwc_rbd-system_65fa516e-3e3f-4b60-b0ae-d19c67df26e4_0
68215ebf91fb        registry.cn-hangzhou.aliyuncs.com/goodrain/rbd-chaos                         "/run/entrypoint.sh …"   3 hours ago         Up 3 hours                                   k8s_rbd-chaos_rbd-chaos-xcdsg_rbd-system_d0be317b-9f0d-4e0a-a721-290b925a22ad_0
63e5a709ade4        registry.cn-hangzhou.aliyuncs.com/goodrain/rbd-monitor                       "/run/entrypoint.sh …"   3 hours ago         Up 3 hours                                   k8s_rbd-monitor_rbd-monitor-0_rbd-system_98a7b6ce-f191-4220-a945-289ec18c1e02_0
ac89e83b70bf        registry.cn-hangzhou.aliyuncs.com/goodrain/pause:3.2                         "/pause"                 3 hours ago         Up 3 hours                                   k8s_POD_rbd-worker-5779b7985b-hnrjl_rbd-system_7ca6da4a-95c3-4970-8109-5d57a30ca0e1_0
ab9c86d001d5        registry.cn-hangzhou.aliyuncs.com/goodrain/pause:3.2                         "/pause"                 3 hours ago         Up 3 hours                                   k8s_POD_rbd-eventlog-0_rbd-system_f55dcd27-eec2-454f-bb95-bc0f2f1e50e6_0
05ac84851c63        registry.cn-hangzhou.aliyuncs.com/goodrain/rbd-db                            "/entrypoint.sh mysq…"   3 hours ago         Up 3 hours                                   k8s_rbd-db_rbd-db-0_rbd-system_5c8af9af-42be-4e89-8f1c-03cb28882ea3_0
ccfec80c899a        registry.cn-hangzhou.aliyuncs.com/goodrain/pause:3.2                         "/pause"                 3 hours ago         Up 3 hours                                   k8s_POD_rbd-api-6f79cff696-2vz5p_rbd-system_1e60e3ff-8c87-4d38-a678-c4fe5960b3e8_0
55ece1cc1952        registry.cn-hangzhou.aliyuncs.com/goodrain/rbd-resource-proxy                "/run/docker-entrypo…"   3 hours ago         Up 3 hours                                   k8s_rbd-resource-proxy_rbd-resource-proxy-cd8f4c484-75rsq_rbd-system_8bf06a88-e68f-4d67-8b23-9342f5488e99_0
7bc5ecbf8742        registry.cn-hangzhou.aliyuncs.com/goodrain/pause:3.2                         "/pause"                 3 hours ago         Up 3 hours                                   k8s_POD_rbd-mq-65975b5cd5-rklwc_rbd-system_65fa516e-3e3f-4b60-b0ae-d19c67df26e4_0
e25a786488af        registry.cn-hangzhou.aliyuncs.com/goodrain/pause:3.2                         "/pause"                 3 hours ago         Up 3 hours                                   k8s_POD_rbd-chaos-xcdsg_rbd-system_d0be317b-9f0d-4e0a-a721-290b925a22ad_0
06792ee9eeb8        registry.cn-hangzhou.aliyuncs.com/goodrain/metrics-scraper                   "/metrics-sidecar"       3 hours ago         Up 3 hours                                   k8s_dashboard-metrics-scraper_dashboard-metrics-scraper-7db45b8bb4-zkgh4_rbd-system_08838266-aebb-45c6-9eba-f4d530a59f6d_0
468937cd6fb3        registry.cn-hangzhou.aliyuncs.com/goodrain/pause:3.2                         "/pause"                 3 hours ago         Up 3 hours                                   k8s_POD_rbd-monitor-0_rbd-system_98a7b6ce-f191-4220-a945-289ec18c1e02_0
486de739a606        registry.cn-hangzhou.aliyuncs.com/goodrain/pause:3.2                         "/pause"                 3 hours ago         Up 3 hours                                   k8s_POD_rbd-db-0_rbd-system_5c8af9af-42be-4e89-8f1c-03cb28882ea3_0
924ddae61a15        registry.cn-hangzhou.aliyuncs.com/goodrain/kubernetes-dashboard              "/dashboard --insecu…"   3 hours ago         Up 3 hours                                   k8s_kubernetes-dashboard_kubernetes-dashboard-fbd4fb949-vlccz_rbd-system_9f07e94c-36e5-4fcb-b4cd-5bce84c817eb_0
de5b17770bae        registry.cn-hangzhou.aliyuncs.com/goodrain/pause:3.2                         "/pause"                 3 hours ago         Up 3 hours                                   k8s_POD_rbd-resource-proxy-cd8f4c484-75rsq_rbd-system_8bf06a88-e68f-4d67-8b23-9342f5488e99_0
aa524853ca30        registry.cn-hangzhou.aliyuncs.com/goodrain/metrics-server                    "/metrics-server --c…"   3 hours ago         Up 3 hours                                   k8s_metrics-server_metrics-server-7f6bc6ff74-hcf4c_rbd-system_e4bbfc56-1699-43ac-8de2-bf9b4e77866c_0
efa594470518        registry.cn-hangzhou.aliyuncs.com/goodrain/pause:3.2                         "/pause"                 3 hours ago         Up 3 hours                                   k8s_POD_dashboard-metrics-scraper-7db45b8bb4-zkgh4_rbd-system_08838266-aebb-45c6-9eba-f4d530a59f6d_0
8725646ac410        registry.cn-hangzhou.aliyuncs.com/goodrain/rbd-webcli                        "/entrypoint.sh --ho…"   3 hours ago         Up 3 hours                                   k8s_rbd-webcli_rbd-webcli-5b9584565f-n6x4t_rbd-system_1b2b2f8c-ffe8-4a28-9e07-1474c0002cb6_0
efd85a26d37d        registry.cn-hangzhou.aliyuncs.com/goodrain/pause:3.2                         "/pause"                 3 hours ago         Up 3 hours                                   k8s_POD_kubernetes-dashboard-fbd4fb949-vlccz_rbd-system_9f07e94c-36e5-4fcb-b4cd-5bce84c817eb_0
0e7933f29861        registry.cn-hangzhou.aliyuncs.com/goodrain/pause:3.2                         "/pause"                 3 hours ago         Up 3 hours                                   k8s_POD_metrics-server-7f6bc6ff74-hcf4c_rbd-system_e4bbfc56-1699-43ac-8de2-bf9b4e77866c_0
163c1cbbefca        registry.cn-hangzhou.aliyuncs.com/goodrain/pause:3.2                         "/pause"                 3 hours ago         Up 3 hours                                   k8s_POD_rbd-webcli-5b9584565f-n6x4t_rbd-system_1b2b2f8c-ffe8-4a28-9e07-1474c0002cb6_0
8a9245a00890        registry.cn-hangzhou.aliyuncs.com/goodrain/rbd-gateway                       "/run/entrypoint.sh …"   3 hours ago         Up 3 hours                                   k8s_rbd-gateway_rbd-gateway-8b9fl_rbd-system_f3f1be30-fce8-433a-9146-e524aea5cfbe_0
339c7a524c63        registry.cn-hangzhou.aliyuncs.com/goodrain/pause:3.2                         "/pause"                 3 hours ago         Up 3 hours                                   k8s_POD_rbd-gateway-8b9fl_rbd-system_f3f1be30-fce8-433a-9146-e524aea5cfbe_0
90afad0248df        registry.cn-hangzhou.aliyuncs.com/goodrain/etcd                              "/usr/local/bin/etcd…"   3 hours ago         Up 3 hours                                   k8s_rbd-etcd_rbd-etcd-0_rbd-system_5601a306-812f-477d-aa2f-2c3669ff17e8_0
d80214b6b32e        registry.cn-hangzhou.aliyuncs.com/goodrain/registry                          "/entrypoint.sh /etc…"   3 hours ago         Up 3 hours                                   k8s_rbd-hub_rbd-hub-64777d89d8-c79lq_rbd-system_22e6478e-6f4a-4e31-9dcc-5e2109b9debc_0
c5c272847bac        registry.cn-hangzhou.aliyuncs.com/goodrain/pause:3.2                         "/pause"                 3 hours ago         Up 3 hours                                   k8s_POD_rbd-etcd-0_rbd-system_5601a306-812f-477d-aa2f-2c3669ff17e8_0
8bfd7d136670        registry.cn-hangzhou.aliyuncs.com/goodrain/rbd-node                          "/run/entrypoint.sh …"   3 hours ago         Up 3 hours                                   k8s_rbd-node_rbd-node-qdxt9_rbd-system_59ba2fa2-17bc-4489-829f-5c9f0465a807_0
64e07177d9fd        registry.cn-hangzhou.aliyuncs.com/goodrain/pause:3.2                         "/pause"                 3 hours ago         Up 3 hours                                   k8s_POD_rbd-hub-64777d89d8-c79lq_rbd-system_22e6478e-6f4a-4e31-9dcc-5e2109b9debc_0
321554bdb38c        registry.cn-hangzhou.aliyuncs.com/goodrain/pause:3.2                         "/pause"                 3 hours ago         Up 3 hours                                   k8s_POD_rbd-node-qdxt9_rbd-system_59ba2fa2-17bc-4489-829f-5c9f0465a807_0
7b7217ece47e        registry.cn-hangzhou.aliyuncs.com/goodrain/nfs-provisioner                   "/nfs-provisioner -p…"   3 hours ago         Up 3 hours                                   k8s_nfs-provisioner_nfs-provisioner-0_rbd-system_28de5f5b-24d2-4f5c-bafe-efabb0282bd9_0
9fec21f63353        registry.cn-hangzhou.aliyuncs.com/goodrain/pause:3.2                         "/pause"                 3 hours ago         Up 3 hours                                   k8s_POD_nfs-provisioner-0_rbd-system_28de5f5b-24d2-4f5c-bafe-efabb0282bd9_0
c7310734e822        registry.cn-hangzhou.aliyuncs.com/goodrain/rainbond-operator                 "/manager --leader-e…"   3 hours ago         Up 3 hours                                   k8s_rainbond-operator_rainbond-operator-6bd98956b7-mq9bn_rbd-system_55244d30-b341-4253-8cb2-7935ec8478f7_0
e5c62dcf2df5        registry.cn-hangzhou.aliyuncs.com/goodrain/pause:3.2                         "/pause"                 3 hours ago         Up 3 hours                                   k8s_POD_rainbond-operator-6bd98956b7-mq9bn_rbd-system_55244d30-b341-4253-8cb2-7935ec8478f7_0
ee5568058ed3        registry.cn-hangzhou.aliyuncs.com/goodrain/cluster-proportional-autoscaler   "/cluster-proportion…"   3 hours ago         Up 3 hours                                   k8s_autoscaler_coredns-autoscaler-74cd6f74d9-97prw_kube-system_8c08dd66-26a6-4ed2-8a6e-61631f7e639f_0
04a23680c4c0        registry.cn-hangzhou.aliyuncs.com/goodrain/coredns-coredns                   "/coredns -conf /etc…"   3 hours ago         Up 3 hours                                   k8s_coredns_coredns-8644d6bd8c-kpxrj_kube-system_3df75cc6-e6c3-49a4-9e15-20641911d5f9_0
8e8898062bbd        registry.cn-hangzhou.aliyuncs.com/goodrain/pause:3.2                         "/pause"                 3 hours ago         Up 3 hours                                   k8s_POD_coredns-autoscaler-74cd6f74d9-97prw_kube-system_8c08dd66-26a6-4ed2-8a6e-61631f7e639f_0
4a19f0a9b4ee        registry.cn-hangzhou.aliyuncs.com/goodrain/pause:3.2                         "/pause"                 3 hours ago         Up 3 hours                                   k8s_POD_coredns-8644d6bd8c-kpxrj_kube-system_3df75cc6-e6c3-49a4-9e15-20641911d5f9_0
c204e90a9b64        registry.cn-hangzhou.aliyuncs.com/goodrain/flannel-cni                       "/install-cni.sh"        3 hours ago         Up 3 hours                                   k8s_install-cni_kube-flannel-mbbcx_kube-system_022e0962-b5db-4371-bcf1-52ae14902a4a_0
198f59f46f87        registry.cn-hangzhou.aliyuncs.com/goodrain/coreos-flannel                    "/opt/bin/flanneld -…"   3 hours ago         Up 3 hours                                   k8s_kube-flannel_kube-flannel-mbbcx_kube-system_022e0962-b5db-4371-bcf1-52ae14902a4a_0
b79050709912        registry.cn-hangzhou.aliyuncs.com/goodrain/pause:3.2                         "/pause"                 3 hours ago         Up 3 hours                                   k8s_POD_kube-flannel-mbbcx_kube-system_022e0962-b5db-4371-bcf1-52ae14902a4a_0
a7e53e6618b4        registry.cn-hangzhou.aliyuncs.com/goodrain/hyperkube:v1.19.6-rke             "/opt/rke-tools/entr…"   3 hours ago         Up 3 hours                                   kube-proxy
6f45fc6aea6c        registry.cn-hangzhou.aliyuncs.com/goodrain/hyperkube:v1.19.6-rke             "/opt/rke-tools/entr…"   3 hours ago         Up 3 hours                                   kubelet
0fc2f86248f7        registry.cn-hangzhou.aliyuncs.com/goodrain/hyperkube:v1.19.6-rke             "/opt/rke-tools/entr…"   3 hours ago         Up 3 hours                                   kube-scheduler
637ce0faba4c        registry.cn-hangzhou.aliyuncs.com/goodrain/hyperkube:v1.19.6-rke             "/opt/rke-tools/entr…"   3 hours ago         Up 3 hours                                   kube-controller-manager
7b16c78f383c        registry.cn-hangzhou.aliyuncs.com/goodrain/hyperkube:v1.19.6-rke             "/opt/rke-tools/entr…"   3 hours ago         Up 3 hours                                   kube-apiserver
82f808597057        registry.cn-hangzhou.aliyuncs.com/goodrain/rke-tools:v0.1.68                 "/docker-entrypoint.…"   3 hours ago         Up 3 hours                                   etcd-rolling-snapshots
56002591730f        registry.cn-hangzhou.aliyuncs.com/goodrain/coreos-etcd:v3.4.13-rke           "/usr/local/bin/etcd…"   3 hours ago         Up 3 hours                                   etcd
b9b62ea4a549        registry.cn-beijing.aliyuncs.com/quyc/rainbond-allinone:v1.2                 "/usr/bin/supervisord"   3 hours ago         Up 3 hours          0.0.0.0:7070->7070/tcp   rainbond-allinone

```

### 路径{#path}

Rainbond 数据目录： */root/rainbonddata*    

### 端口{#port}

除 80, 443 等常见端口需开启之外，以下端口可能会用到：  

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 7070   | Rainbond 控制台端口 | 必选   |

### 版本{#version}

控制台查看

### 服务{#service}

```shell
sudo docker start | stop | restart | stats rainbond-allinone
```

### 命令行{#cli}

[Rainbond Cli](https://www.rainbond.com/docs/ops-guide/tools/grctl)

### API{#api}

Rainbond API(https://www.rainbond.com/docs/ops-guide/component/rbd-api/) 服务，提供底层服务接口。