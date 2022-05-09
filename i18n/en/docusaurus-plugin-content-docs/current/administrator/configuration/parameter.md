---
sidebar_position: 10
slug: /administrator/parameter
---

# Parameter sheet

The important information such as the installation directory path, configuration file path, port, version, etc. are listed below.

## Path and directory{#path}

A unified **data, log and configuration file** storage directory is agreed by Websoft9:

* */data/wwwroot/appname*: appname directory
* */data/apps*: the same with appname directory
* */data/db*: database directory
* */data/config* : configuration file directory
* */data/logs* logs directory

## Port{#port}

You can run the cmd `netstat -tunlp` to list all used ports, and we list the following most useful ports:     

### Common ports for application

| Number | Use |  Necessity |
| --- | --- | --- |
| 80 | HTTP to access application | Optional |
| 443 | HTTPS to access application | Optional |

### Common ports for Server

| Number | Use |  Necessity |
| --- | --- | --- |
| 21 | Linux FTP | Optional |
| 22 | Linux SSH  | Optional |
| 3389 | Windows RDP  | Optional |

### Common ports for Database

Refer to: [Database GUI](../user/dbgui)


## Service{#service}

These services you must know when you using Websoft9.   

There are two types of services based on Systemd and Docker in Websoft9 applications.  

### Systemd Service

```
sudo systemctl start | top | restart | status docker
sudo systemctl start | top | restart | status apache
sudo systemctl start | top | restart | status nginx
sudo systemctl start | top | restart | status mysql
sudo systemctl start | top | restart | status php-fpm
sudo systemctl start | top | restart | status postgresql
sudo systemctl start | top | restart | status mongod
```

### Docker Service

This section we agreed that container is the same with service, so you list all services by command `sudo docker ps -a` 

Below is some useful service for you:  

```
$ sudo docker start | stop | restart | stats container_name

# e.g Database GUI tools service
sudo docker start | stop | restart | stats phpmyadmin
sudo docker start | stop | restart | stats adminmongo
sudo docker start | stop | restart | stats pgadmin

# e.g Database service
sudo docker start | stop | restart | stats mysql
sudo docker start | stop | restart | stats postgresql
sudo docker start | stop | restart | stats redis
sudo docker start | stop | restart | stats sqlite
sudo docker start | stop | restart | stats memcached
```


## Version{#version}

You can see the version from product page of Marketplace. However, after being deployed to your server, the components will be automatically updated, resulting in a certain change in the version number. Therefore, the exact version number should be viewed by running the command on the server:

##### Common 

```
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# Docker version
docker -v
```

##### Database

```
# MongoDB version
mongo --version

# PostgreSQL version:
psql --version

# MySQL version
mysql -V

# Redis version
redis-server -v

```

##### Web Server

```
# Apache version on Centos
httpd -v

# Apache version on Ubuntu
apache2 -v

# List Installed Apache Modules
apachectl -M

# Nginx version
nginx -v

# List Installed Nginx Modules
nginx -V

```

##### Program languages

```
# Java version
java -v

# PHP Version
php -v

# List Installed PHP Modules
php -m

# Node.js  Version
node -v

# PM2  Version
pm2 -V

# NPM version
npm -v

# yarn version
yarn --version
```
