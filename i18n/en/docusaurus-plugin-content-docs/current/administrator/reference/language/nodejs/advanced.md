---
slug: /nodejs/advanced
---

# Advanced

## Install Node

### Ansible install

You can use Websoft9 Ansible role to install multiply version very easy.  

```
git clone https://github.com/websoft9/role_nodejs
ansible-playbook role_nodejs/tests/test.yml
```

### Upgrade

```
# upgrade NPM
sudo npm install npm -g
```

## Concepts

### NPM

[NPM](https://www.npmjs.com/) is the tool used by over 11,000,000 JavaScript developers around the world. Your developers already use it. Your company depends on it. Create an Org and get more out of the tools your team already knows and loves. 

NPM consists of three distinct components:  

- the website
- the Command Line Interface (CLI)
- the registry

Use the [website](https://npmjs.com/) to discover packages, set up profiles, and manage other aspects of your npm experience. For example, you can set up [Orgs](https://www.npmjs.com/features) (organizations) to manage access to public or private packages.

The [CLI](https://docs.npmjs.com/cli/npm) runs from a terminal, and is how most developers interact with npm.

The [registry](https://docs.npmjs.com/misc/registry) is a large public database of JavaScript software and the meta-information surrounding it

### PM2

[PM2](https://github.com/Unitech/pm2) is a production process manager for Node.js applications with a built-in load balancer..PM2 is constantly assailed by [more than 1800 tests](https://travis-ci.org/Unitech/pm2).

You can install pm2 by NPM  

```
npm install -g pm2
```

Then, enter to your application directory`cd /data/wwwroot/project` and manage node.js application by PM2

```
# Start An Application
pm2 start bin/www or pm2 start app.js

# 重命名进程/应用  
pm2 start app.js --name wb123

# 添加进程/应用 
watch  pm2 start bin/www --watch

# 结束进程/应用  
pm2 stop www

# 结束所有进程/应用  
pm2 stop all

# 删除进程/应用  
pm2 delete www

# 删除所有进程/应用  
pm2 delete all

# To list all running applications  
pm2 list

# 查看某个进程/应用具体情况  
pm2 describe www

# 查看进程/应用的资源消耗情况  
pm2 monit

# Log Management  
pm2 logs

pm2 logs APP-NAME       # Display APP-NAME logs
pm2 logs --json         # JSON output
pm2 logs --format       # Formated output
pm2 flush               # Flush all logs
pm2 reloadLogs          # Reload all logs

# 若要查看某个进程/应用的日志,使用  
pm2 logs www

# 重新启动进程/应用  
pm2 restart www

# 重新启动所有进程/应用  
pm2 restart all
```

### NVM

[NVM](https://github.com/creationix/nvm), Node Version Manager - Simple bash script to manage multiple active node.js versions

```
# Install NVM
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash

# Install Node latest version by NVM
nvm install node

# Install a special Node version by NVM
nvm install 6.14.4

# List all versions that can be installed
nvm ls-remote

# Use the installed version 
nvm run node --version

# Use the Node at subshell
nvm exec 4.2 node --version

# Get the path of Node
nvm which 5.0
```

### TypeScript

TypeScript 是 JavaScript 的超集，简单说 TypeScript 具有更丰富的语法特征。 

## FAQ

#### NPM is included on Node by default?

Yes

#### YARN vs NPM？

| npm | yarn |
| ---: | :--- |
| npm install | yarn |
| npm install react --save | yarn add react |
| npm uninstall react --save | yarn remove react |
| npm install react --save-dev | yarn add react --dev |
| npm update --save | yarn upgrade |

#### How can manage multiply Node?

Use [NVM](https://github.com/creationix/nvm)