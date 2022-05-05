---
sidebar_position: 19
---

# Linux Commands

This is the Websoft9 Support Team’s collection of information regarding Linux, that they sometimes use while troubleshooting. It is listed here for transparency, and it may be useful for users with experience with Linux.

## Version

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

## System

```
# Restart
reboot 

# Memory
free

# Disk
df -hl 

# Docker containers list
sudo docker ps -a

# Network port
netstat -tunlp

# List all environment
env
```

## File management

```
# create a new directory and all subdirectories
mkdir -p dir/dir2/dir3

# Send a command's output to file.txt, no STDOUT
ls > file.txt

# Send a command's output to file.txt AND see it in STDOUT
ls | tee /tmp/file.txt

# Search and Replace within a file
sed -i 's/original-text/new-text/g' <filename>

# Download from URL
wget url  

# Unzip to pwd path
unzip xx.zip

# Go to directory
cd /data/wwwroot

# Modify the owner of user and group for directory
chown -R nginx.nginx /data/wwwroot

# Modify the Read, Write and Excuse for directory
find /data/wwwroot/default -type f -exec chmod 640 {} \
find /data/wwwroot/default -type d -exec chmod 750 {} \

# 修改文件权限
chmod u+x <file>
```

## Search

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

## Maintenance

```
# Restart Systemd Service, e.g nginx, php-fpm, apache
systemctl restart nginx
systemctl restart php-fpm 
systemctl restart apache

# Update and Upgrade
yum update -y
yum upgrade -y

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

## 资源

```
# disk space info. The '-h' gives the data in human-readable values
df -h

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
# Debian/Ubuntu

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

# CentOS/RedHat

# Install a package
yum install <package>
dnf install <package> # RHEL/CentOS 8+

rpm -ivh <package_name>.rpm

# Find an installed package
rpm -qa | grep <package>
```

