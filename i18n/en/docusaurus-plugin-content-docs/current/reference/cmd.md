---
sidebar_position: 2.1
slug: /linux-commands
---

# Commands

Linux commands that you may need to use when use Websoft9

## Distribution

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
# Restart Linux
reboot 

# Check memory
free

# Check disk
df -hl 

# Check container
sudo docker ps -a

# Check port
netstat -tunlp

# Check environment
env

# Time settings
sudo timedatectl set-time '2024-04-22 15:30:00'

# Query time
timedatectl status

# Upgrade
yum upgrade
apt upgrade

# Check fonts
fc-list

# View character encoding 
locale 
```

## Filesystem

```
# create a new directory and all subdirectories
mkdir -p dir/dir2/dir3

# Send a command's output to file.txt, no STDOUT
ls > file.txt

# Send a command's output to file.txt AND see it in STDOUT
ls | tee /tmp/file.txt

# Search and Replace within a file
sed -i 's/original-text/new-text/g' <filename>

# Downlod file to your target path
wget -P /path/to/directory URL

# Unzip
unzip xx.zip
unzip xx.zip -d /path/to/directory


# Modify directory owner and group
chown -R user:gourp /path/to/directory


# Modify read, write, and execute permissions for all
chmod -R 0750 /path/to/directory

# Modify read, write, and execute permissions for files
find /path/to/directory -type f -exec chmod 640 {} \;

# Modify read, write, and execute permissions for directory
find /path/to/directory -type d -exec chmod 750 {} \;

# Modify read, write, and execute permissions for file
chmod u+x <file>

# Add groupnamehere to an exist directory
sudo setfacl -Rm g:groupnamehere:rwx /path/to/directory

# Add groupnamehere to an exist directory
sudo setfacl -Rm g:groupnamehere:rwx /path/to/directory

# Add groupnamehere to an new directory
sudo setfacl -Rdm g:groupnamehere:rwx /path/to/directory
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

## Service and Process

```
# Manage Systemd service
systemctl start | stop | status |restart <your_service>

# Manage docker service
docker restart $(docker ps -a | awk '{ print $1}' | tail -n +2)

# Displays tcp and udp ports, processes, and other related information.
netstat -tunlp
netstat -tunlp | grep 端口号

# View server port 22 occupancy
lsof -i:22

# kill process
kill -9 PID

# Print last lines in log file where 'n'
# is the number of lines to print
tail -n /path/to/log/file
```

## Disk

```
# Viewing peripherals and disk partitions
lsblk

# View Partition Capacity
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

## Network

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

## Packages

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

## Logs{#logs}

```
# View service logs
systemctl status service_name
journalctl -u service_name

# View service error logs
journalctl -p err

# Viewing the kernel log
journalctl -k

# Viewing the log of a script
journalctl /usr/bin/bash

# View logs for a target user
journalctl UID=33 --since today

# View Docker logs
docker logs <container>
```

## User

```
# Create a Linux system account, the creation process will prompt for: username/password, and will create the user's home directory
adduser 

# Only create accounts for applications that cannot log in to Linux.
useradd 
```