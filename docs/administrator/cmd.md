---
sidebar_position: 19
---

# 常用命令

可能需要用到的 Linux 命令

## 系统

```
# 重启服务器
reboot 

# 查看内存使用
free

# 查看硬盘使用
df -hl 

# 查看 Docker 容器
sudo docker ps -a

# 查看端口
netstat -tunlp
```

## 文件管理

```
# 下载url对应的文件
wget url  

# 解压xx.zip文件到当前目录
unzip xx.zip

# 进入指定目录
cd /data/wwwroot

# 修改wwwroot文件夹所属的用户和用户组为nginx
chown -R nginx.nginx /data/wwwroot

# 分别修改文件和文件夹的读、写、执行权限
find /data/wwwroot/default -type f -exec chmod 640 {} \;
find /data/wwwroot/default -type d -exec chmod 750 {} \;
```

## 运维命令

```
# 重启Nginx服务，重启php-fpm
systemctl restart nginx
systemctl restart php-fpm 

# 重启Apache服务
systemctl restart apache

# 系统升级
yum update -y //升级所有包同时也升级软件和系统内核,-y当安装过程提示选择全部为"yes"
yum upgrade -y //只升级所有包，不升级软件和系统内核,-y当安装过程提示选择全部为"yes"

# 重启所有容器
docker restart $(docker ps -a | awk '{ print $1}' | tail -n +2)

# 显示 tcp，udp 的端口和进程等相关情况。
netstat -tunlp
netstat -tunlp | grep 端口号

# 查看服务器 22 端口的占用情况
lsof -i:22

# kill 端口对应的进程
kill -9 PID
```