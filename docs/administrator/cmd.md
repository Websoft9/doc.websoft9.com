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
```