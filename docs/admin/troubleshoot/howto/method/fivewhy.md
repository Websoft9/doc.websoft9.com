---
sidebar_position: 2
slug: /troubleshoot/5why 
---

# 5WHY 分析法

所谓 5why 分析法，又称“5问法”，也就是对一个问题点连续以5个“为什么”来自问，以追究其根本原因。   

## 是什么？

**5why法的关键所在**：鼓励解决问题的人要努力避开主观或自负的假设和逻辑陷阱，从结果着手，沿着因果关系链条，顺藤摸瓜，直至找出原有问题的根本原因。  

**经典案例**  

丰田汽车公司前副社长大野耐一，如何通过运用5WHY法来找到工厂设备停机的根本原因。有一次，他在生产线上发现机器总是停转，虽然修过多次，但仍不见好转。于是他询问工人机器停机的原因。

于是出现了下面的问答对话：

```
问题1：为什么机器停了？

答案1：因为机器超载，保险丝烧断了。

问题2：为什么机器会超载？

答案2：因为轴承的润滑不足。

问题3：为什么轴承会润滑不足？

答案3：因为润滑泵失灵了。

问题4：为什么润滑泵会失灵？

答案4：因为它的轮轴耗损了。

问题5：为什么润滑泵的轮轴会耗损？

答案5：因为杂质跑到里面去了。
```

## 怎么用？

#### pip install 在容器中运行异常？

```
1. 无法使用的表现是什么？

从Docker日志来看，是访问 py.org 超时

2. 为什么访问 py.org 超时？

容器到 py.org 的网络不稳定

3. 为什么容器到 py.org 的网络不稳定？

py.org 的仓库在国外，不稳定是合理的

4. 宿主机访问 py.org 的网络稳定？

不稳定，但宿主机 pip install 正常。  

5. 宿主机连接的 python 仓库与容器连接的 Python 仓库有什么不一样？

不一样。宿主机并不是访问 py.org 的仓库。  

原来宿主机 pip.conf 中设置了国内的源，此时问题已有答案。

```

#### ONLYOFFICE 运行超时? 

```
1. 什么导致超时？

ERROR: for onlyoffice-community-server  UnixHTTPConnectionPool(host='localhost', port=None): Read timed out. (read timeout=60)

2. 镜像拉取下来了吗？

拉取了，即说明有某种原因导致在 60s 无法启动 或 ONLYOFFICE 启动本身超过 60s。先排除资源瓶颈

3. 内存够用吗？

还剩余2G，即内存不是原因。那么更偏向于ONLYOFFICE 启动本身超过 60s

4. Docker compose 可以修改超时时间吗？

可以。通过 export DOCKER_CLIENT_TIMEOUT=500 和 export COMPOSE_HTTP_TIMEOUT=500 修改它

5. 修改到 500s 解决问题了？

解决了
```








