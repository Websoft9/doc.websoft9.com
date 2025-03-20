---
sidebar_position: 2.1
slug: /linux-commands
---

# 常用命令

管理 Websoft9 时，可能需要用到的 Linux 命令

## 版本

```
# Debian/Ubuntu
uname -a
lsb_release -a

# CentOS/RedHat
cat /etc/centos-release
cat /etc/redhat-release

# This will provide a lot more information
cat /etc/os-release
```

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

# 查看所有环境变量
env

# 设置时间
sudo timedatectl set-time '2024-04-22 15:30:00'

# 查询时间
timedatectl status

# 系统升级
yum update -y //升级所有包同时也升级软件和系统内核,-y当安装过程提示选择全部为"yes"
yum upgrade -y //只升级所有包，不升级软件和系统内核,-y当安装过程提示选择全部为"yes"
```

## 文件系统

```
# create a new directory and all subdirectories
mkdir -p dir/dir2/dir3

# Send a command's output to file.txt, no STDOUT
ls > file.txt

# Send a command's output to file.txt AND see it in STDOUT
ls | tee /tmp/file.txt

# Search and Replace within a file
sed -i 's/original-text/new-text/g' <filename>

# 下载url对应的文件
wget url  

# 解压xx.zip文件到当前目录
unzip xx.zip

# 进入指定目录
cd /data/wwwroot

# 修改wwwroot文件夹所属的用户和用户组为nginx
chown -R nginx.nginx /data/wwwroot

# 分别修改文件和文件夹的读、写、执行权限
chmod -R 0750 /data/apps
find /data/wwwroot/default -type f -exec chmod 640 {} \;
find /data/wwwroot/default -type d -exec chmod 750 {} \;

# 修改文件权限
chmod u+x <file>

# Add groupnamehere to an exist directory /base/path/
sudo setfacl -Rm g:groupnamehere:rwx /base/path/

# Add groupnamehere to an exist directory /base/path/
sudo setfacl -Rm g:groupnamehere:rwx /base/path/

# Add groupnamehere to an new directory /base/path/
sudo setfacl -Rdm g:groupnamehere:rwx /base/path/

# 查看字体
fc-list

# 查看字符编码 
locale 
```

## 搜索

```
# search for a file in a filesystem
find . -name 'filename.rb' -print

# locate a file
locate <filename>

# see command history
history

# search CLI history
<ctrl>-R

# -B/A = show 2 lines before/after search_term
grep -B 2 -A 2 search_term <filename>

# -<number> shows both before and after
grep -2 search_term <filename>

# Search on all files in directory (recursively)
grep -r search_term <directory>

# search through *.gz files is the same except with zgrep
zgrep search_term <filename>

# Fast grep printing lines containing a string pattern
fgrep -R string_pattern <filename or directory>

# View command history
history

# Run last command that started with 'his' (3 letters min)
!his

# Search through command history
<ctrl>-R

# Execute last command with sudo
sudo !!
```

## 服务与进程

```
# 管理服务
systemctl start | stop | status |restart <your_service>

# 重启所有容器
docker restart $(docker ps -a | awk '{ print $1}' | tail -n +2)

# 显示 tcp，udp 的端口和进程等相关情况。
netstat -tunlp
netstat -tunlp | grep 端口号

# 查看服务器 22 端口的占用情况
lsof -i:22

# kill 端口对应的进程
kill -9 PID

# Print last lines in log file where 'n'
# is the number of lines to print
tail -n /path/to/log/file
```

## 磁盘与外设

```
# 查看外设和磁盘分区
lsblk

# 查看分区容量
fdisk -l

# disk space info. The '-h' gives the data in human-readable values
df -h
df -T

# size of each file/dir and its contents in the current dir
du -hd 1

# or alternative
du -h --max-depth=1

# find files greater than certain size(k, M, G) and list them in order
# get rid of the + for exact, - for less than
find / -type f -size +100M -print0 | xargs -0 du -hs | sort -h

# Find free memory on a system
free -m

# Find what processes are using memory/CPU and organize by it
# Load average is 1/CPU for 1, 5, and 15 minutes
top -o %MEM
top -o %CPU

# strace a process
strace -tt -T -f -y -yy -s 1024 -p <pid>

# run strace on all puma processes
ps auwx | grep puma | awk '{ print " -p " $2}' | xargs strace -tt -T -f -y -yy -s 1024 -o /tmp/puma.txt
```

## 网络

```
# Find the programs that are listening on ports
netstat -plnt
ss -plnt
lsof -i -P | grep <port>


# Show domain IP address
dig +short example.com
nslookup example.com

# Check DNS using specific nameserver
# 8.8.8.8 = google, 1.1.1.1 = cloudflare, 208.67.222.222 = opendns
dig @8.8.8.8 example.com
nslookup example.com 1.1.1.1

# Find host provider
whois <ip_address> | grep -i "orgname\|netname"

# Curl headers with redirect
curl --head --location "https://example.com"

# Test if a host is reachable on the network. `ping6` works on IPv6 networks.
ping example.com

# Show the route taken to a host. `traceroute6` works on IPv6 networks.
traceroute example.com
mtr example.com

# List details of network interfaces
ip address

# Check local DNS settings
cat /etc/hosts
cat /etc/resolv.conf
systemd-resolve --status

# Capture traffic to/from a host
sudo tcpdump host www.example.com
```

## 包管理

```
##-------- Debian/Ubuntu

# List packages
dpkg -l
apt list --installed

# Find an installed package
dpkg -l | grep <package>
apt list --installed | grep <package>

# Install a package
dpkg -i <package_name>.deb
apt-get install <package>
apt install <package>

##-------- CentOS/RedHat

# Install a package
yum install <package>
dnf install <package> # RHEL/CentOS 8+

rpm -ivh <package_name>.rpm

# Find an installed package
rpm -qa | grep <package>
```

## 日志{#logs}

```
# 指定服务日志
systemctl status service_name
journalctl -u service_name

# 查看 systemd 的错误日志，-p 支持 emerg alert err crit warning notice info debug 等值
journalctl -p err

# 查看内核日志
journalctl -k

# 查看脚本的日志
journalctl /usr/bin/bash

# 查看指定用户的日志
journalctl UID=33 --since today

# Docker 容器日志查看方法
docker logs appname
```

## 用户

```
# 用于创建 Linux 系统账号，创建过程中会提示：用户名/密码，同时会创建用户家目录
adduser 

# 仅创建无法登陆 Linux 系统的应用账号
useradd 
```