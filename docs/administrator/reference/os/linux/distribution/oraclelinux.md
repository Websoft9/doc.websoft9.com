---
sidebar_position: 1
slug: /oraclelinux
---

# Oracle Linux

[Oracle Linux](https://www.oracle.com/linux/) 是一个完全免费、开源并可以自由分发的 Linux 发行版。  

它与 CentOS 或 Ubuntu 等其他免费 Linux 相比，有几个特别之处：

1. 更兼容 Oracle 的其他产品线，例如：[Why Oracle Database Runs Best on Oracle Linux](https://www.oracle.com/a/ocom/docs/linux/oracle-database-runs-best-on-oracle-linux.pdf)

2. 修复补丁后无需重启（零停机）

3. Oracle Linux 官方提供了比较完善的配套支持：
   * [Oracle Linux 认证应用程序](https://apexapps.oracle.com/pls/apex/f?p=10263:17::::::)
   * [Oracle Linux 硬件兼容商](https://linux.oracle.com/ords/f?p=117:1)
   * [Oracle Linux CVE](https://linux.oracle.com/ords/f?p=130:21:)
   * [Oracle Linux 升级包](https://linux.oracle.com/ords/f?p=105:21:117077190823888:pg_R_1213672130548773998:NO&pg_min_row=1&pg_max_rows=50&pg_rows_fetched=50)
   * [Oracle Linux 勘误表](https://oss.oracle.com/mailman/listinfo/el-errata)

4. Oracle 官方提供了可选的[技术支持订阅](https://shop.oracle.com/apex/f?p=dstore:2:0::NO:RIR,RP,2:PROD_HIER_ID:4510272175861805728468)

5. Oracle 在云上提供了一个 Oracle Autonomous Linux 系统，具备自主更新升级的能力（零停机）

## 场景

### 升级

升级是一个很有必要的工作，担心升级系统会导致业务出现问题是典型的保守主义。   

Oracle Linux 在一个维护周期内可能会发布数百个安全漏洞和 Bug 补丁，如果不去升级谁又能保证这些 Bug 不会影响自己的业务呢？  

优先使用 Oracle 官方提供的升级工具[Ksplice](https://ksplice.oracle.com/try/trial)进行升级。  

## 问题解答

#### Oracle Linux 使用的什么内核？

Oracle 使用的其自己维护的 [Unbreakable Enterprise Kernel](https://github.com/oracle/linux-uek)，兼容 RHCK

## 故障排除

#### IO 密集型计算下服务器重启？

问题描述：数据库建索引等 IO 密集型计算负载下或资源耗尽 CPU 100%，服务器出现重启的情况？  
解决方案：Oracle 官方建议及时升级补丁
