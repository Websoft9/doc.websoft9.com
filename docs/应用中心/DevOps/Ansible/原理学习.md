---
sidebar_position: 3
slug: /ansible/study
tags:
  - Ansible
  - DevOps
---

# 原理学习


本章尽量全面的介绍 Ansible 的原理，将常用的知识点汇聚在一起，以帮助用户在实践中能够充分准确的用好 Ansible。

## 概述

[Ansible](https://github.com/ansible/ansible) 诞生于 2012 年，目前是 RedHat 旗下的产品，是 Github 上受欢迎的自动化运维工具。

从事过运维相关工作的小伙伴，对 Shell 应该是“有爱有恨”的。一方面我们爱它的无所不能，另外一方面我们恨它的语法晦涩难懂，且难以模块化利用。  

Ansible 的作者兼创始人Michael DeHaan 曾经供职于Puppet Labs、RedHat、Michael，在配置管理和架构设计方面有丰富的经验。其在RedHat任职期间主要开发了Cobble，经历了各种系统简化、自动化基础架构操作的失败和痛苦，在尝试了Puppet、Chef、Cfengine、Capistrano、Fabric、Function、Plain SSH等各式工具后，决定自己打造一款能结合众多工具优点的自动化工具，Ansible由此诞生。

Ansible 为何如此火爆？首先是当前云计算的大规模应用所驱动，然后就是它的核心特点决定的：

* 无需代理也可以控制多台受控机并行管理
* 采用描述性的语言来使用，非常易读、易编写
* 兼容 Python 的语法
* 安装过程简单，学习曲线很平坦


一种解释排版型语言，易读性极强：  

```
- block:
  - name: Create credentials Folder
    file:
      path: /credentials
      state: directory

  - name: Write Databases Password
    template:
      src: password.txt.jinja2
      dest: /credentials/password.txt
      mode: 644
```

一句话总结：简单易用，功能强大，用途广泛。

## 应用领域

Ansible 究竟有什么用呢？

我们从运维工程师或开发人员日常工作中最常见的部署来说：为了部署一个应用，我们需要提前安装 Web 服务、应用程序服务、消息队列、缓存系统、数据库、负载均衡等基础软件，与此同时我们还需要通过手工配置，将各个组件连接起来，让它们发挥功效。甚至，站在软件维护的角度，还需要部署日志系统、监控系统、数据库分析系统、数据库审计等维护工具。如果使用手工来完成这些任务，从购买一台云服务器，再到 SSH 登录直至完成所有任务，需要数百个步骤，而且每一个步骤不能出错。  

如果有一个自动化程序能够完成上述任务，那一定会收到用户的热烈欢迎。幸运的，Ansible 就是这样的工具，它比 Shell 简单，它可以轻轻松松处理：

### 配置管理

配置管理即部署部署应用程序环境，包括对 Linux 和 Windows 上进行各种程序安装，系统操作，Web服务管理、应用服务管理、数据库配置等

### 管理云资源

Ansible 提供包括 AWS,Azure等数十个云资源的创建、操作。即无需用户了解每个云平台的 API，也可以轻松管理云资源。

### 监控告警

Ansible 支持对 Grafana、Nagios、Zabbix、Datalog 等系统监控软件进行直接操作。

### 消息发送

Ansible 提供了大量的 [Notification modules](https://docs.ansible.com/ansible/2.9/modules/list_of_notification_modules.html) 用于帮助应用程序发送消息，支持：邮件、Mattermost、RabbitMQ、syslogger等常见的应用。

### 硬件管理

Ansible 可以对网络设备、存储设备进行直接操作，所支持网络品牌包括 Cisco、Aruba、Check Point等多达几十个，支持的存储品牌包括：IBM、Netapp、EMC等

一句话总结：Ansible 可以完成 DevOps 全过程所需的自动化配置工作：  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/ansible/ansible-fordevops-websoft9.png)


## 架构

### 技术架构

**Ansible 技术架构**
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/ansible/ansible-structure2-websoft9.png)

我们知道，让合适的程序以合适的方式在合适的主机上高效率的运行，是技术架构的出发点。  

Ansible 的技术架构同样遵循这个原理，下面我们从如下三个方面阐述 Ansible 的技术架构：

* **主机**：运行 Ansible 程序的服务器，分为**主控端和受控端**两种类型的主机，主机的在架构中的表现形式为 Host Inventory（主机清单）
* **程序**：官方内置的软件包被成为为模块和插件，用户自己编写的程序被称之为 Playbook （多个 Playbook 以某种形式组合在一起被成为 roles）
* **连接**：主控端和受控端之间的连接与控制，一般采用 SSH 连接，支持认证

为什么主机分为主控端（Control Node）受控端（Managed Node）？  

主要是 Ansible 的用途决定的，由于 Ansible 需要考虑同一个程序在同一个时间部署到多个主机上，故在设计上引入的主控端这种角色，用于以集中式的方式向多个受控主机发布配置任务。 

如果不考虑这种场景，Ansible 也支持在本机上运行程序，即主控模式并不是必须的。


**Ansible 工作原理**
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/ansible/ansible-structure-websoft9.png)

用户登录到 Ansible 所在的服务器，便可以使用命令行运行 Ansible 程序。

这里需注意的是前面多次提到过的 Inventory 的概念，Ansible 程序在运行的时候，一定提前准备 Inventory 文件，如果缺少这个文件，Ansible 就只能在本机上运行。

下面就是一个在本机运行 ping 模块的程序，`localhost` 参数告之 Ansible 目标主机是本机

```
$ansible localhost -m ping

localhost | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

如果没有准备好 Inventory，而选用所有主机 （`all` 参数），系统就会报错
```
$ansible all -m ping
43.128.22.14 | UNREACHABLE! => {
    "changed": false,
    "msg": "Failed to connect to the host via ssh: Permission denied (publickey,gssapi-keyex,gssapi-with-mic,password).",
    "unreachable": true
}

```

**Ansible 代码执行过程**


### 生态架构

Ansible 是一个卓越的技术产品，也是一个成功的商业软件，它的成功与其商业生态布局有密切关系。  

生态架构的技术基础：

* 模块
* 插件
* Python 语法语法兼容性
* Roles

生态商业整合：

* Ansible Galaxy：开发者共享的代码库（role库）
  ![Ansible Galaxy](https://libs.websoft9.com/Websoft9/DocsPicture/zh/ansible/Ansible-Galaxy-Blog-Post.png)

* Ansible Collection：开发者共享的应用程序库（完整的 Ansible 应用程序）
  ![Ansible Galaxy](https://libs.websoft9.com/Websoft9/DocsPicture/zh/ansible/ansible-collection-websoft9.png)

* Ansible Tower：企业级可视化 Ansible 管理工具，支持 API。
  ![Ansible Tower](https://libs.websoft9.com/Websoft9/DocsPicture/en/awx/awxui-websoft9.png)

* Ansible Automation Platform：由 RedHat 托管的 Ansible 项目，包含 Ansible Tower 以及自动化资源、自动化分析等企业级功能。
  ![Ansible Automation Platform](https://libs.websoft9.com/Websoft9/DocsPicture/zh/ansible/redhat-automation-platform_content-collections.png)


## 安装

### 主控端

安装之前，需了解是否具备安装条件：

**操作系统要求**：Red Hat, Debian, CentOS, macOS, any of the BSDs等，不支持Windows
**Python要求**：Python 2 (version 2.7) or Python 3 (versions 3.5 and higher) installed

条件具备之后，只需要一条命令即可安装：

```
pip install ansible
或
yum install ansible
或
apt install ansible
```

### 受控端

* 采用 SSH（默认为SFTP）与 Control Node 通信，如果SSH不可用，通过修改 ansible.cfg 更改通信协议
* Python支持：Python 2 (version 2.6 or later) or Python 3 (version 3.5 or later).

## 配置

Ansible 作为一个自动化解决方案包，与其他成熟的软件系统一样，支持自定义各种环境参数。

### 配置文件

Ansible 支持多个位置存放 ansible.cfg 配置文件，包括：

* ./ansible.cfg 当前工作目录下的 ansible.cfg
* ~/.ansible.cfg 当前用户家目录下的 .ansible.cfg
* /etc/ansible/ansible.cfg 安装自动产生的 ansible.cfg
* ANSIBLE_CONFIG 配置文件环境路径的环境变量

如果有多个配置文件怎么办？

Ansible 有优先级原则：环境变量 > 当前工作目录 > 用户家目录 > etc

### 配置项

#### 所有配置项

运行 `cat /etc/ansible/ansible.cfg` 文件，便可以查看几乎所有的配置项。

```
# config file for ansible -- https://ansible.com/
# ===============================================

# nearly all parameters can be overridden in ansible-playbook
# or with command line flags. ansible will read ANSIBLE_CONFIG,
# ansible.cfg in the current working directory, .ansible.cfg in
# the home directory or /etc/ansible/ansible.cfg, whichever it
# finds first

[defaults]

# some basic default values...

#inventory      = /etc/ansible/hosts
#library        = /usr/share/my_modules/
#module_utils   = /usr/share/my_module_utils/
#remote_tmp     = ~/.ansible/tmp
#local_tmp      = ~/.ansible/tmp
#plugin_filters_cfg = /etc/ansible/plugin_filters.yml
#forks          = 5
#poll_interval  = 15
#sudo_user      = root
#ask_sudo_pass = True
#ask_pass      = True
#transport      = smart
#remote_port    = 22
#module_lang    = C
#module_set_locale = False

# plays will gather facts by default, which contain information about
# the remote system.
#
# smart - gather by default, but don't regather if already gathered
# implicit - gather by default, turn off with gather_facts: False
# explicit - do not gather by default, must say gather_facts: True
#gathering = implicit

# This only affects the gathering done by a play's gather_facts directive,
# by default gathering retrieves all facts subsets
# all - gather all subsets
# network - gather min and network facts
# hardware - gather hardware facts (longest facts to retrieve)
# virtual - gather min and virtual facts
# facter - import facts from facter
# ohai - import facts from ohai
# You can combine them using comma (ex: network,virtual)
# You can negate them using ! (ex: !hardware,!facter,!ohai)
# A minimal set of facts is always gathered.
#gather_subset = all

# some hardware related facts are collected
# with a maximum timeout of 10 seconds. This
# option lets you increase or decrease that
# timeout to something more suitable for the
# environment.
# gather_timeout = 10

# Ansible facts are available inside the ansible_facts.* dictionary
# namespace. This setting maintains the behaviour which was the default prior
# to 2.5, duplicating these variables into the main namespace, each with a
# prefix of 'ansible_'.
# This variable is set to True by default for backwards compatibility. It
# will be changed to a default of 'False' in a future release.
# ansible_facts.
# inject_facts_as_vars = True

# additional paths to search for roles in, colon separated
#roles_path    = /etc/ansible/roles

# uncomment this to disable SSH key host checking
#host_key_checking = False

# change the default callback, you can only have one 'stdout' type  enabled at a time.
#stdout_callback = skippy


## Ansible ships with some plugins that require whitelisting,
## this is done to avoid running all of a type by default.
## These setting lists those that you want enabled for your system.
## Custom plugins should not need this unless plugin author specifies it.

# enable callback plugins, they can output to stdout but cannot be 'stdout' type.
#callback_whitelist = timer, mail

# Determine whether includes in tasks and handlers are "static" by
# default. As of 2.0, includes are dynamic by default. Setting these
# values to True will make includes behave more like they did in the
# 1.x versions.
#task_includes_static = False
#handler_includes_static = False

# Controls if a missing handler for a notification event is an error or a warning
#error_on_missing_handler = True

# change this for alternative sudo implementations
#sudo_exe = sudo

# What flags to pass to sudo
# WARNING: leaving out the defaults might create unexpected behaviours
#sudo_flags = -H -S -n

# SSH timeout
#timeout = 10

# default user to use for playbooks if user is not specified
# (/usr/bin/ansible will use current user as default)
#remote_user = root

# logging is off by default unless this path is defined
# if so defined, consider logrotate
#log_path = /var/log/ansible.log

# default module name for /usr/bin/ansible
#module_name = command

# use this shell for commands executed under sudo
# you may need to change this to bin/bash in rare instances
# if sudo is constrained
#executable = /bin/sh

# if inventory variables overlap, does the higher precedence one win
# or are hash values merged together?  The default is 'replace' but
# this can also be set to 'merge'.
#hash_behaviour = replace

# by default, variables from roles will be visible in the global variable
# scope. To prevent this, the following option can be enabled, and only
# tasks and handlers within the role will see the variables there
#private_role_vars = yes

# list any Jinja2 extensions to enable here:
#jinja2_extensions = jinja2.ext.do,jinja2.ext.i18n

# if set, always use this private key file for authentication, same as
# if passing --private-key to ansible or ansible-playbook
#private_key_file = /path/to/file

# If set, configures the path to the Vault password file as an alternative to
# specifying --vault-password-file on the command line.
#vault_password_file = /path/to/vault_password_file

# format of string {{ ansible_managed }} available within Jinja2
# templates indicates to users editing templates files will be replaced.
# replacing {file}, {host} and {uid} and strftime codes with proper values.
#ansible_managed = Ansible managed: {file} modified on %Y-%m-%d %H:%M:%S by {uid} on {host}
# {file}, {host}, {uid}, and the timestamp can all interfere with idempotence
# in some situations so the default is a static string:
#ansible_managed = Ansible managed

# by default, ansible-playbook will display "Skipping [host]" if it determines a task
# should not be run on a host.  Set this to "False" if you don't want to see these "Skipping"
# messages. NOTE: the task header will still be shown regardless of whether or not the
# task is skipped.
#display_skipped_hosts = True

# by default, if a task in a playbook does not include a name: field then
# ansible-playbook will construct a header that includes the task's action but
# not the task's args.  This is a security feature because ansible cannot know
# if the *module* considers an argument to be no_log at the time that the
# header is printed.  If your environment doesn't have a problem securing
# stdout from ansible-playbook (or you have manually specified no_log in your
# playbook on all of the tasks where you have secret information) then you can
# safely set this to True to get more informative messages.
#display_args_to_stdout = False

# by default (as of 1.3), Ansible will raise errors when attempting to dereference
# Jinja2 variables that are not set in templates or action lines. Uncomment this line
# to revert the behavior to pre-1.3.
#error_on_undefined_vars = False

# by default (as of 1.6), Ansible may display warnings based on the configuration of the
# system running ansible itself. This may include warnings about 3rd party packages or
# other conditions that should be resolved if possible.
# to disable these warnings, set the following value to False:
#system_warnings = True

# by default (as of 1.4), Ansible may display deprecation warnings for language
# features that should no longer be used and will be removed in future versions.
# to disable these warnings, set the following value to False:
#deprecation_warnings = True

# (as of 1.8), Ansible can optionally warn when usage of the shell and
# command module appear to be simplified by using a default Ansible module
# instead.  These warnings can be silenced by adjusting the following
# setting or adding warn=yes or warn=no to the end of the command line
# parameter string.  This will for example suggest using the git module
# instead of shelling out to the git command.
# command_warnings = False


# set plugin path directories here, separate with colons
#action_plugins     = /usr/share/ansible/plugins/action
#become_plugins     = /usr/share/ansible/plugins/become
#cache_plugins      = /usr/share/ansible/plugins/cache
#callback_plugins   = /usr/share/ansible/plugins/callback
#connection_plugins = /usr/share/ansible/plugins/connection
#lookup_plugins     = /usr/share/ansible/plugins/lookup
#inventory_plugins  = /usr/share/ansible/plugins/inventory
#vars_plugins       = /usr/share/ansible/plugins/vars
#filter_plugins     = /usr/share/ansible/plugins/filter
#test_plugins       = /usr/share/ansible/plugins/test
#terminal_plugins   = /usr/share/ansible/plugins/terminal
#strategy_plugins   = /usr/share/ansible/plugins/strategy


# by default, ansible will use the 'linear' strategy but you may want to try
# another one
#strategy = free

# by default callbacks are not loaded for /bin/ansible, enable this if you
# want, for example, a notification or logging callback to also apply to
# /bin/ansible runs
#bin_ansible_callbacks = False


# don't like cows?  that's unfortunate.
# set to 1 if you don't want cowsay support or export ANSIBLE_NOCOWS=1
#nocows = 1

# set which cowsay stencil you'd like to use by default. When set to 'random',
# a random stencil will be selected for each task. The selection will be filtered
# against the `cow_whitelist` option below.
#cow_selection = default
#cow_selection = random

# when using the 'random' option for cowsay, stencils will be restricted to this list.
# it should be formatted as a comma-separated list with no spaces between names.
# NOTE: line continuations here are for formatting purposes only, as the INI parser
#       in python does not support them.
#cow_whitelist=bud-frogs,bunny,cheese,daemon,default,dragon,elephant-in-snake,elephant,eyes,\
#              hellokitty,kitty,luke-koala,meow,milk,moofasa,moose,ren,sheep,small,stegosaurus,\
#              stimpy,supermilker,three-eyes,turkey,turtle,tux,udder,vader-koala,vader,www

# don't like colors either?
# set to 1 if you don't want colors, or export ANSIBLE_NOCOLOR=1
#nocolor = 1

# if set to a persistent type (not 'memory', for example 'redis') fact values
# from previous runs in Ansible will be stored.  This may be useful when
# wanting to use, for example, IP information from one group of servers
# without having to talk to them in the same playbook run to get their
# current IP information.
#fact_caching = memory

#This option tells Ansible where to cache facts. The value is plugin dependent.
#For the jsonfile plugin, it should be a path to a local directory.
#For the redis plugin, the value is a host:port:database triplet: fact_caching_connection = localhost:6379:0

#fact_caching_connection=/tmp



# retry files
# When a playbook fails a .retry file can be created that will be placed in ~/
# You can enable this feature by setting retry_files_enabled to True
# and you can change the location of the files by setting retry_files_save_path

#retry_files_enabled = False
#retry_files_save_path = ~/.ansible-retry

# squash actions
# Ansible can optimise actions that call modules with list parameters
# when looping. Instead of calling the module once per with_ item, the
# module is called once with all items at once. Currently this only works
# under limited circumstances, and only with parameters named 'name'.
#squash_actions = apk,apt,dnf,homebrew,pacman,pkgng,yum,zypper

# prevents logging of task data, off by default
#no_log = False

# prevents logging of tasks, but only on the targets, data is still logged on the master/controller
#no_target_syslog = False

# controls whether Ansible will raise an error or warning if a task has no
# choice but to create world readable temporary files to execute a module on
# the remote machine.  This option is False by default for security.  Users may
# turn this on to have behaviour more like Ansible prior to 2.1.x.  See
# https://docs.ansible.com/ansible/become.html#becoming-an-unprivileged-user
# for more secure ways to fix this than enabling this option.
#allow_world_readable_tmpfiles = False

# controls the compression level of variables sent to
# worker processes. At the default of 0, no compression
# is used. This value must be an integer from 0 to 9.
#var_compression_level = 9

# controls what compression method is used for new-style ansible modules when
# they are sent to the remote system.  The compression types depend on having
# support compiled into both the controller's python and the client's python.
# The names should match with the python Zipfile compression types:
# * ZIP_STORED (no compression. available everywhere)
# * ZIP_DEFLATED (uses zlib, the default)
# These values may be set per host via the ansible_module_compression inventory
# variable
#module_compression = 'ZIP_DEFLATED'

# This controls the cutoff point (in bytes) on --diff for files
# set to 0 for unlimited (RAM may suffer!).
#max_diff_size = 1048576

# This controls how ansible handles multiple --tags and --skip-tags arguments
# on the CLI.  If this is True then multiple arguments are merged together.  If
# it is False, then the last specified argument is used and the others are ignored.
# This option will be removed in 2.8.
#merge_multiple_cli_flags = True

# Controls showing custom stats at the end, off by default
#show_custom_stats = True

# Controls which files to ignore when using a directory as inventory with
# possibly multiple sources (both static and dynamic)
#inventory_ignore_extensions = ~, .orig, .bak, .ini, .cfg, .retry, .pyc, .pyo

# This family of modules use an alternative execution path optimized for network appliances
# only update this setting if you know how this works, otherwise it can break module execution
#network_group_modules=eos, nxos, ios, iosxr, junos, vyos

# When enabled, this option allows lookups (via variables like {{lookup('foo')}} or when used as
# a loop with `with_foo`) to return data that is not marked "unsafe". This means the data may contain
# jinja2 templating language which will be run through the templating engine.
# ENABLING THIS COULD BE A SECURITY RISK
#allow_unsafe_lookups = False

# set default errors for all plays
#any_errors_fatal = False

[inventory]
# enable inventory plugins, default: 'host_list', 'script', 'auto', 'yaml', 'ini', 'toml'
#enable_plugins = host_list, virtualbox, yaml, constructed

# ignore these extensions when parsing a directory as inventory source
#ignore_extensions = .pyc, .pyo, .swp, .bak, ~, .rpm, .md, .txt, ~, .orig, .ini, .cfg, .retry

# ignore files matching these patterns when parsing a directory as inventory source
#ignore_patterns=

# If 'true' unparsed inventory sources become fatal errors, they are warnings otherwise.
#unparsed_is_failed=False

[privilege_escalation]
#become=True
#become_method=sudo
#become_user=root
#become_ask_pass=False

[paramiko_connection]

# uncomment this line to cause the paramiko connection plugin to not record new host
# keys encountered.  Increases performance on new host additions.  Setting works independently of the
# host key checking setting above.
#record_host_keys=False

# by default, Ansible requests a pseudo-terminal for commands executed under sudo. Uncomment this
# line to disable this behaviour.
#pty=False

# paramiko will default to looking for SSH keys initially when trying to
# authenticate to remote devices.  This is a problem for some network devices
# that close the connection after a key failure.  Uncomment this line to
# disable the Paramiko look for keys function
#look_for_keys = False

# When using persistent connections with Paramiko, the connection runs in a
# background process.  If the host doesn't already have a valid SSH key, by
# default Ansible will prompt to add the host key.  This will cause connections
# running in background processes to fail.  Uncomment this line to have
# Paramiko automatically add host keys.
#host_key_auto_add = True

[ssh_connection]

# ssh arguments to use
# Leaving off ControlPersist will result in poor performance, so use
# paramiko on older platforms rather than removing it, -C controls compression use
#ssh_args = -C -o ControlMaster=auto -o ControlPersist=60s

# The base directory for the ControlPath sockets.
# This is the "%(directory)s" in the control_path option
#
# Example:
# control_path_dir = /tmp/.ansible/cp
#control_path_dir = ~/.ansible/cp

# The path to use for the ControlPath sockets. This defaults to a hashed string of the hostname,
# port and username (empty string in the config). The hash mitigates a common problem users
# found with long hostnames and the conventional %(directory)s/ansible-ssh-%%h-%%p-%%r format.
# In those cases, a "too long for Unix domain socket" ssh error would occur.
#
# Example:
# control_path = %(directory)s/%%h-%%r
#control_path =

# Enabling pipelining reduces the number of SSH operations required to
# execute a module on the remote server. This can result in a significant
# performance improvement when enabled, however when using "sudo:" you must
# first disable 'requiretty' in /etc/sudoers
#
# By default, this option is disabled to preserve compatibility with
# sudoers configurations that have requiretty (the default on many distros).
#
#pipelining = False

# Control the mechanism for transferring files (old)
#   * smart = try sftp and then try scp [default]
#   * True = use scp only
#   * False = use sftp only
#scp_if_ssh = smart

# Control the mechanism for transferring files (new)
# If set, this will override the scp_if_ssh option
#   * sftp  = use sftp to transfer files
#   * scp   = use scp to transfer files
#   * piped = use 'dd' over SSH to transfer files
#   * smart = try sftp, scp, and piped, in that order [default]
#transfer_method = smart

# if False, sftp will not use batch mode to transfer files. This may cause some
# types of file transfer failures impossible to catch however, and should
# only be disabled if your sftp version has problems with batch mode
#sftp_batch_mode = False

# The -tt argument is passed to ssh when pipelining is not enabled because sudo
# requires a tty by default.
#usetty = True

# Number of times to retry an SSH connection to a host, in case of UNREACHABLE.
# For each retry attempt, there is an exponential backoff,
# so after the first attempt there is 1s wait, then 2s, 4s etc. up to 30s (max).
#retries = 3

[persistent_connection]

# Configures the persistent connection timeout value in seconds.  This value is
# how long the persistent connection will remain idle before it is destroyed.
# If the connection doesn't receive a request before the timeout value
# expires, the connection is shutdown. The default value is 30 seconds.
#connect_timeout = 30

# The command timeout value defines the amount of time to wait for a command
# or RPC call before timing out. The value for the command timeout must
# be less than the value of the persistent connection idle timeout (connect_timeout)
# The default value is 30 second.
#command_timeout = 30

[accelerate]
#accelerate_port = 5099
#accelerate_timeout = 30
#accelerate_connect_timeout = 5.0

# The daemon timeout is measured in minutes. This time is measured
# from the last activity to the accelerate daemon.
#accelerate_daemon_timeout = 30

# If set to yes, accelerate_multi_key will allow multiple
# private keys to be uploaded to it, though each user must
# have access to the system via SSH to add a new key. The default
# is "no".
#accelerate_multi_key = yes

[selinux]
# file systems that require special treatment when dealing with security context
# the default behaviour that copies the existing context or uses the user default
# needs to be changed to use the file system dependent context.
#special_context_filesystems=nfs,vboxsf,fuse,ramfs,9p,vfat

# Set this to yes to allow libvirt_lxc connections to work without SELinux.
#libvirt_lxc_noseclabel = yes

[colors]
#highlight = white
#verbose = blue
#warn = bright purple
#error = red
#debug = dark gray
#deprecate = purple
#skip = cyan
#unreachable = red
#ok = green
#changed = yellow
#diff_add = green
#diff_remove = red
#diff_lines = cyan


[diff]
# Always print diff when running ( same as always running with -D/--diff )
# always = no

# Set how many context lines to show in diff
# context = 3
```

配置项不仅可通过 ansible.cfg 文件进行定义，大多数参数也可通过 ANSIBLE_ 开头的环境变量进行配置：  

```
export ANSIBLE_SUDO_USER=root
```

#### 常用配置

| 项                | 说明                                                         | 示例                            |
| ----------------- | ------------------------------------------------------------ | ------------------------------- |
| log_path          | 日志文件地址，Ansible 默认不记录日志，需自定义             | log_path = /var/log/ansible.log |
| inventory         | 资源清单（主机列表）文件位置                                 | inventory = /etc/ansible/hosts  |
| library           | 模块目录，有默认值                                           | library = /usr/share/ansible    |
| forks             | 工作进程最大值，默认值为 5                                   | forks = 10                      |
| sudo_user         | 设置运行 Ansible 程序的默认用户                              | sudo_user = root                |
| remote_port       | 远程主机的端口，用于连接被管理主机，默认值为 22              | remote_port = 22                |
| host_key_checking | 是否检查 SSH 主机的秘钥，默认为 True。适用于同一台被管理主机秘钥发生变化的错误提示，如果不希望出现这种提示，可以设置本项为 False | host_key_checking = False       |
| timeout           | 设置连接远程主机的 SSH 超时时间                              | timeout = 60                    |


## 主机清单

Ansible 经常用于管理大量的服务器，如果企业有数千台服务器，那么一定需要对这些服务器进行分门别类。与此同时，服务器的用户账号信息等也各不相同。  

[Ansible Inventory](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#intro-inventory) （主机清单） 就是为了灵活的管理主机信息的技术标准。  

### 格式

静态文件是相对于动态文件来说，Ansible 的静态主机文件是指提前准备好并有完整内容的主机清单

默认的文件是：/etc/ansible/hosts

下面先展示一个包含丰富信息的 hosts 文件示例：

```
[webservers]
86.21.14.177
web1.websoft9.com
we2.websoft9.com
192.165.2.50

[database]
86.21.14.172
host1.websoft9.com
host2.websoft9.com
192.165.2.51

[monitor]
86.21.14.173 ansible_user=root ansible_ssh_pass=123456 proxy=proxy.websoft9.com
86.21.14.174 ansible_user=root ansible_ssh_private_key_file=/root/mykey
host1.websoft9.com
www[01:50].example.com

[monitor:vars]
proxy=proxy.websoft9.com
```

从以上文件可得知 Inventory 的特点：

* 可分组（分组还可以嵌套）
* 可存放用户账号和密码
* 可以为主机和分组指定变量
* 同一个主机可以归属多个组
* 主机名称支持范表达式 www[01:50] 表示：www01,www02...


另外，Ansible 还支持多个 inventory 文件。只需在 ansible.cfg 文件中让 inventory 配置项指向一个目录即可。不过，多个 inventory 文件与单个并没有区别，毕竟可以单个文件由于支持分组，已经完全可以满足各种分类场景了。

### 参数

| ansible_ssh_host             | 远程主机                             |
| ---------------------------- | ------------------------------------ |
| ansible_ssh_port             | 指定原创主机ssh端口                  |
| ansible_ssh_root             | ssh连接远程主机的用户                |
| ansible_ssh_pass             | ssh连接远程主机的密码                |
| ansible_sudo_pass            | sudo密码                             |
| ansible_connection           | 指定连接类型：local、ssh、paramiko   |
| ansible_ssh_private_key_file | ssh连接使用的私钥                    |
| ansible_shell_type           | 指定连接端的shell类型，sh、csh、fish |
| ansible_python_interpreter   | 指定远程主机使用的python路径         |

### 变量

Ansible 支持向 inventory 文件中添加变量，变量适用范围可以是单个主机，也可以是分组。

### 清单插件

[参考](https://docs.ansible.com/ansible/latest/plugins/inventory.html#inventory-plugins)

### 常见问题

#### Ansible 是否支持动态主机清单？

支持。由于在实际生产场景中，如果清单采用手动维护这些列表将是一个非常繁琐的任务。  

Ansible 支持动态生产主机清单，即 ansible.cfg 指向一个生产主机清单的程序，再由程序产生符合格式的清单列表。

#### Ansible 有没有默认分组？

有。默认有包含文件所有主机的 all 组，同时还有没有归属的 ungrouped 组。

## 命令行

以下是 Ansible 命令行的完整列表。每个页面均包含对该实用程序的描述以及所支持参数的列表。

- [ansible](https://docs.ansible.com/ansible/latest/cli/ansible.html)：主命令
- [ansible-config](https://docs.ansible.com/ansible/latest/cli/ansible-config.html)：配置文件和配置项修改
- [ansible-console](https://docs.ansible.com/ansible/latest/cli/ansible-console.html)：交互式运行 ansible 命令
- [ansible-doc](https://docs.ansible.com/ansible/latest/cli/ansible-doc.html)：查询文档
- [ansible-galaxy](https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html)：galaxy 项目库发布与下载
- [ansible-inventory](https://docs.ansible.com/ansible/latest/cli/ansible-inventory.html)：主机清单管理
- [ansible-playbook](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html)：运行 playbook 程序
- [ansible-pull](https://docs.ansible.com/ansible/latest/cli/ansible-pull.html)：拉取并运行 playbook 程序
- [ansible-vault](https://docs.ansible.com/ansible/latest/cli/ansible-vault.html)：加密处理

ansible-playbook 是最常见的命令，也是运行程序的主要入口。  

实际上，Ansible 也支持在一条命令中运行使用模块，实现我们的部署目标。  

官方称这种命令的运行方式为 [Ad-doc](https://docs.ansible.com/ansible/2.9/user_guide/intro_adhoc.html)

示例  

```
# 打印本机磁盘信息
ansible localhost -m command -a 'df -h'

# 获取 facts 信息
ansible localhost -m setup

# 连通性测试
ansible all -m ping

# 本机上安装 docker-composer
ansible localhost -m get_url -a "url=https://getcomposer.org/composer-stable.phar dest=/usr/bin/composer mode=0750"
```

命令解释：

* localhost/all：主机名/IP/分组
* -m：指定模块（默认是command，所以可以把-m command这个去掉）
* command/setup/ping：模块名称
* -a：模块参数
* 'df -h'：参数值

## Playbook

本章我们讲解 Ansible 最核心的组件 playbook。  


### 概述

**playbook 是什么？**

如果把 Ansible 比作开发语言，那么 playbook 就是一个程序文件。程序代码在程序文件中按顺序执行，最终完成所需处理的任务。

**为什么称之 playbook 而不是程序文件呢？**

playbook 翻译过来就是剧本的意思。如果你是文艺爱好者，可能阅读过电影/舞台剧的剧本（下图）

![电影剧本](https://libs.websoft9.com/Websoft9/DocsPicture/zh/ansible/film-playbook.png)

剧本是个导演组织演员、道具、拍摄等资源一种编排叙述性的文字说明。

Ansible 的程序代码与电影具备具有类似性，故被作者命名为 playbook

### 格式

playbook 有着规范化的格式，下面就是一个典型的可以被直接运行的 playbook 范例：

```
- hosts: localhost
  remote_user:root
  vars:
    https_port: 443
  tasks:
    - name: Create file1
      ansible.builtin.file:
        state: touch
        path: /tmp/file1

    - name: Create file2
      ansible.builtin.file:
        state: touch
        path: /tmp/file2

    - name: Create file3
      ansible.builtin.file:
        state: touch
        path: /tmp/file3
```

playbook 包含几个关键字，每个关键字的含义如下：

* hosts: 主机IP 或 主机组名 或 all
* remote_user: 以某个用户身份运行，通常设置为 root
* vars: 变量

![Ansible playbook 关系图](https://libs.websoft9.com/Websoft9/DocsPicture/zh/ansible/ansible-palybookvsplay-websoft9.png)  
**图：playbook, paly, task 三者关系**

### 模块

模块 Ansible 官方已经编写好了的软件包，是 Ansible 的功能核心。  

正是由于 Ansible 提供了大量的模块，才大大简化运维工作，可以让运维人员只需要少量的 Shell 知识便可以完成复杂的运维任务。  

有两种使用模块的方式：  

在 Playbook 中使用模块：  

```
- name: restart webserver
  service:
    name: httpd
    state: restarted

```

在 命令行中使用模块：

```
ansible localhost -m service -a "name=httpd state=started"
```

查看所有[模块](https://docs.ansible.com/ansible/2.9/modules/modules_by_category.html)

### 插件

插件是对模块功能的一种补充。


### 变量

### 循环

### 条件

Ansible 中使用 `when` 作为条件判断的关键词，条件判断注意事项：

* 变量名不需要双大括号“{{}}”
* 运算符兼容 jinja2 格式：==, !=, >, >=
* 支持逻辑运算符：and, or, not
* 支持变量的定义判断：defined, undefined, none

详情参考：[Ansible条件判断详解](https://www.ityoudao.cn/posts/ansible-conditionals/)

### 过滤

### 模板

### 查询

### 交互

- name: Create file1
  ansible.builtin.file:
    state: touch
    path: /tmp/file1

## Role

Ansible role 是用于规范化管理 playbook 程序文件以及附带的其他文件的一种软件包组织机制。  

### 结构

运行 `ansible-galaxy init myrole` 可以创建名称为 myrole 的 role。

使用 `tree` 命令查看包的结构：  

```
$ tree myrole
myrole
|-- defaults
|   `-- main.yml
|-- files
|-- handlers
|   `-- main.yml
|-- meta
|   `-- main.yml
|-- README.md
|-- tasks
|   `-- main.yml
|-- templates
|-- tests
|   |-- inventory
|   `-- test.yml
`-- vars
    `-- main.yml

8 directories, 8 files

```

* tasks/main.yml 存放项目的主文件
* templates 存放 jinjia2 模板文件
* files 存放程序所需的文件
* defaults/vars 存放变量文件，vars 下的变量优先级更高
* tests 存放本 role 入口 playbook
* handlers 存放 task 的 handler
* meta 存放 role 的元数据，包括系统兼容性、role 依赖等

### 运行

以上创建的 role 模板也可以使用 ansible-playbook 运行。  

```
ansible-playbook myrole/tests/test.yml
```

> 这种运行方式是很多初学者可能会忽视的

### Ansible Galaxy

[Ansible Galaxy](https://galaxy.ansible.com/) 是官方提供的帮助用户分享 role 的网站平台。

同时官方也提供了一套 cli 命令：  

```
$ ansible-galaxy role -h
usage: ansible-galaxy role [-h] ROLE_ACTION ...

positional arguments:
  ROLE_ACTION
    init       Initialize new role with the base structure of a role.
    remove     Delete roles from roles_path.
    delete     Removes the role from Galaxy. It does not remove or alter the
               actual GitHub repository.
    list       Show the name and version of each role installed in the
               roles_path.
    search     Search the Galaxy database by tags, platforms, author and
               multiple keywords.
    import     Import a role
    setup      Manage the integration between Galaxy and the given source.
    info       View more details about a specific role.
    install    Install role(s) from file(s), URL(s) or Ansible Galaxy

optional arguments:
  -h, --help   show this help message and exit
```

### Websoft9 role

Websoft9 提供了包括 Apache,Nginx, MySQL 等数十个常见应用的自动化 [Ansible role](https://github.com/search?q=org%3AWebsoft9+role)， 100%开源，非常便于用户使用。

## Collection

[Ansible Collection](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) 是完整的 Ansible 应用，它包含了 role 以及各种其他所需的配置，可以 role 编排后处理更为复杂的任务。

Websoft9 提供了包括 WordPress, GitLab, Odoo, LAMP 等数十个常见应用的开源自动化 [Ansible Collection](https://github.com/search?q=org%3AWebsoft9+ansible)，可免费使用。

## Ansible Facts

Ansible Facts 是用于收集设备新的的一个功能，运行 `ansible localhost -m setup` 可查看本机所有的 facts 信息，并以 JSON 格式返回。  

facts 可以当做 playbook 的变量进行引用，故下面列出以供编写程序的时候做参考：

```
localhost | SUCCESS => {
    "ansible_facts": {
        "ansible_all_ipv4_addresses": [
            "172.23.0.1",
            "172.27.0.1",
            "172.22.0.1",
            "172.18.0.1",
            "172.28.0.1",
            "172.17.0.1",
            "172.19.0.11"
        ],
        "ansible_all_ipv6_addresses": [
            "fe80::42:9fff:fe11:a0f3",
            "fe80::42:b5ff:feb0:13b3",
            "fe80::42:1fff:fe68:d58b",
            "fe80::8874:21ff:fe2a:cada",
            "fe80::42:2cff:fefd:f576",
            "fe80::688a:7ff:fea2:9a76",
            "fe80::42:bdff:fe4e:d3ab",
            "fe80::42:edff:fef4:5bd3",
            "fe80::5054:ff:fe4a:8b63",
            "fe80::14d0:b6ff:fecb:a383",
            "fe80::2cae:e1ff:fee1:aa10"
        ],
        "ansible_apparmor": {
            "status": "disabled"
        },
        "ansible_architecture": "x86_64",
        "ansible_bios_date": "04/01/2014",
        "ansible_bios_version": "seabios-1.9.1-qemu-project.org",
        "ansible_br_2f206deb7914": {
            "active": false,
            "device": "br-2f206deb7914",
            "features": {
                "busy_poll": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "on",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "netns_local": "on [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "off [fixed]",
                "rx_fcs": "off [fixed]",
                "rx_gro_hw": "off [fixed]",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "off [fixed]",
                "rx_vlan_offload": "off [fixed]",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "off [fixed]",
                "tx_checksumming": "on",
                "tx_fcoe_segmentation": "on",
                "tx_gre_csum_segmentation": "on",
                "tx_gre_segmentation": "on",
                "tx_gso_partial": "on",
                "tx_gso_robust": "on",
                "tx_ipip_segmentation": "on",
                "tx_lockless": "on [fixed]",
                "tx_nocache_copy": "off",
                "tx_scatter_gather": "on",
                "tx_scatter_gather_fraglist": "on",
                "tx_sctp_segmentation": "on",
                "tx_sit_segmentation": "on",
                "tx_tcp6_segmentation": "on",
                "tx_tcp_ecn_segmentation": "on",
                "tx_tcp_mangleid_segmentation": "on",
                "tx_tcp_segmentation": "on",
                "tx_udp_tnl_csum_segmentation": "on",
                "tx_udp_tnl_segmentation": "on",
                "tx_vlan_offload": "on",
                "tx_vlan_stag_hw_insert": "on",
                "udp_fragmentation_offload": "on",
                "vlan_challenged": "off [fixed]"
            },
            "hw_timestamp_filters": [],
            "id": "8000.02421f68d58b",
            "interfaces": [],
            "ipv4": {
                "address": "172.22.0.1",
                "broadcast": "172.22.255.255",
                "netmask": "255.255.0.0",
                "network": "172.22.0.0"
            },
            "ipv6": [
                {
                    "address": "fe80::42:1fff:fe68:d58b",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "02:42:1f:68:d5:8b",
            "mtu": 1500,
            "promisc": false,
            "stp": false,
            "timestamping": [
                "rx_software",
                "software"
            ],
            "type": "bridge"
        },
        "ansible_br_9651f99a5578": {
            "active": true,
            "device": "br-9651f99a5578",
            "features": {
                "busy_poll": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "on",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "netns_local": "on [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "off [fixed]",
                "rx_fcs": "off [fixed]",
                "rx_gro_hw": "off [fixed]",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "off [fixed]",
                "rx_vlan_offload": "off [fixed]",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "off [fixed]",
                "tx_checksumming": "on",
                "tx_fcoe_segmentation": "off [requested on]",
                "tx_gre_csum_segmentation": "on",
                "tx_gre_segmentation": "on",
                "tx_gso_partial": "on",
                "tx_gso_robust": "off [requested on]",
                "tx_ipip_segmentation": "on",
                "tx_lockless": "on [fixed]",
                "tx_nocache_copy": "off",
                "tx_scatter_gather": "on",
                "tx_scatter_gather_fraglist": "on",
                "tx_sctp_segmentation": "on",
                "tx_sit_segmentation": "on",
                "tx_tcp6_segmentation": "on",
                "tx_tcp_ecn_segmentation": "on",
                "tx_tcp_mangleid_segmentation": "on",
                "tx_tcp_segmentation": "on",
                "tx_udp_tnl_csum_segmentation": "on",
                "tx_udp_tnl_segmentation": "on",
                "tx_vlan_offload": "on",
                "tx_vlan_stag_hw_insert": "on",
                "udp_fragmentation_offload": "on",
                "vlan_challenged": "off [fixed]"
            },
            "hw_timestamp_filters": [],
            "id": "8000.0242bd4ed3ab",
            "interfaces": [
                "veth477c3d2"
            ],
            "ipv4": {
                "address": "172.28.0.1",
                "broadcast": "172.28.255.255",
                "netmask": "255.255.0.0",
                "network": "172.28.0.0"
            },
            "ipv6": [
                {
                    "address": "fe80::42:bdff:fe4e:d3ab",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "02:42:bd:4e:d3:ab",
            "mtu": 1500,
            "promisc": false,
            "stp": false,
            "timestamping": [
                "rx_software",
                "software"
            ],
            "type": "bridge"
        },
        "ansible_br_9a4737a41426": {
            "active": true,
            "device": "br-9a4737a41426",
            "features": {
                "busy_poll": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "on",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "netns_local": "on [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "off [fixed]",
                "rx_fcs": "off [fixed]",
                "rx_gro_hw": "off [fixed]",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "off [fixed]",
                "rx_vlan_offload": "off [fixed]",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "off [fixed]",
                "tx_checksumming": "on",
                "tx_fcoe_segmentation": "off [requested on]",
                "tx_gre_csum_segmentation": "on",
                "tx_gre_segmentation": "on",
                "tx_gso_partial": "on",
                "tx_gso_robust": "off [requested on]",
                "tx_ipip_segmentation": "on",
                "tx_lockless": "on [fixed]",
                "tx_nocache_copy": "off",
                "tx_scatter_gather": "on",
                "tx_scatter_gather_fraglist": "on",
                "tx_sctp_segmentation": "on",
                "tx_sit_segmentation": "on",
                "tx_tcp6_segmentation": "on",
                "tx_tcp_ecn_segmentation": "on",
                "tx_tcp_mangleid_segmentation": "on",
                "tx_tcp_segmentation": "on",
                "tx_udp_tnl_csum_segmentation": "on",
                "tx_udp_tnl_segmentation": "on",
                "tx_vlan_offload": "on",
                "tx_vlan_stag_hw_insert": "on",
                "udp_fragmentation_offload": "on",
                "vlan_challenged": "off [fixed]"
            },
            "hw_timestamp_filters": [],
            "id": "8000.02429f11a0f3",
            "interfaces": [
                "veth2d333ca",
                "vethcbd8671"
            ],
            "ipv4": {
                "address": "172.23.0.1",
                "broadcast": "172.23.255.255",
                "netmask": "255.255.0.0",
                "network": "172.23.0.0"
            },
            "ipv6": [
                {
                    "address": "fe80::42:9fff:fe11:a0f3",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "02:42:9f:11:a0:f3",
            "mtu": 1500,
            "promisc": false,
            "stp": false,
            "timestamping": [
                "rx_software",
                "software"
            ],
            "type": "bridge"
        },
        "ansible_br_be93c3b27dc7": {
            "active": true,
            "device": "br-be93c3b27dc7",
            "features": {
                "busy_poll": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "on",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "netns_local": "on [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "off [fixed]",
                "rx_fcs": "off [fixed]",
                "rx_gro_hw": "off [fixed]",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "off [fixed]",
                "rx_vlan_offload": "off [fixed]",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "off [fixed]",
                "tx_checksumming": "on",
                "tx_fcoe_segmentation": "off [requested on]",
                "tx_gre_csum_segmentation": "on",
                "tx_gre_segmentation": "on",
                "tx_gso_partial": "on",
                "tx_gso_robust": "off [requested on]",
                "tx_ipip_segmentation": "on",
                "tx_lockless": "on [fixed]",
                "tx_nocache_copy": "off",
                "tx_scatter_gather": "on",
                "tx_scatter_gather_fraglist": "on",
                "tx_sctp_segmentation": "on",
                "tx_sit_segmentation": "on",
                "tx_tcp6_segmentation": "on",
                "tx_tcp_ecn_segmentation": "on",
                "tx_tcp_mangleid_segmentation": "on",
                "tx_tcp_segmentation": "on",
                "tx_udp_tnl_csum_segmentation": "on",
                "tx_udp_tnl_segmentation": "on",
                "tx_vlan_offload": "on",
                "tx_vlan_stag_hw_insert": "on",
                "udp_fragmentation_offload": "on",
                "vlan_challenged": "off [fixed]"
            },
            "hw_timestamp_filters": [],
            "id": "8000.02422cfdf576",
            "interfaces": [
                "veth0cf6c64"
            ],
            "ipv4": {
                "address": "172.18.0.1",
                "broadcast": "172.18.255.255",
                "netmask": "255.255.0.0",
                "network": "172.18.0.0"
            },
            "ipv6": [
                {
                    "address": "fe80::42:2cff:fefd:f576",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "02:42:2c:fd:f5:76",
            "mtu": 1500,
            "promisc": false,
            "stp": false,
            "timestamping": [
                "rx_software",
                "software"
            ],
            "type": "bridge"
        },
        "ansible_br_f4e97043f974": {
            "active": false,
            "device": "br-f4e97043f974",
            "features": {
                "busy_poll": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "on",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "netns_local": "on [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "off [fixed]",
                "rx_fcs": "off [fixed]",
                "rx_gro_hw": "off [fixed]",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "off [fixed]",
                "rx_vlan_offload": "off [fixed]",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "off [fixed]",
                "tx_checksumming": "on",
                "tx_fcoe_segmentation": "on",
                "tx_gre_csum_segmentation": "on",
                "tx_gre_segmentation": "on",
                "tx_gso_partial": "on",
                "tx_gso_robust": "on",
                "tx_ipip_segmentation": "on",
                "tx_lockless": "on [fixed]",
                "tx_nocache_copy": "off",
                "tx_scatter_gather": "on",
                "tx_scatter_gather_fraglist": "on",
                "tx_sctp_segmentation": "on",
                "tx_sit_segmentation": "on",
                "tx_tcp6_segmentation": "on",
                "tx_tcp_ecn_segmentation": "on",
                "tx_tcp_mangleid_segmentation": "on",
                "tx_tcp_segmentation": "on",
                "tx_udp_tnl_csum_segmentation": "on",
                "tx_udp_tnl_segmentation": "on",
                "tx_vlan_offload": "on",
                "tx_vlan_stag_hw_insert": "on",
                "udp_fragmentation_offload": "on",
                "vlan_challenged": "off [fixed]"
            },
            "hw_timestamp_filters": [],
            "id": "8000.0242b5b013b3",
            "interfaces": [],
            "ipv4": {
                "address": "172.27.0.1",
                "broadcast": "172.27.255.255",
                "netmask": "255.255.0.0",
                "network": "172.27.0.0"
            },
            "ipv6": [
                {
                    "address": "fe80::42:b5ff:feb0:13b3",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "02:42:b5:b0:13:b3",
            "mtu": 1500,
            "promisc": false,
            "stp": false,
            "timestamping": [
                "rx_software",
                "software"
            ],
            "type": "bridge"
        },
        "ansible_cmdline": {
            "BOOT_IMAGE": "/boot/vmlinuz-3.10.0-1127.13.1.el7.x86_64",
            "LANG": "en_US.UTF-8",
            "biosdevname": "0",
            "console": "tty0",
            "crashkernel": "auto",
            "intel_idle.max_cstate": "1",
            "intel_pstate": "disable",
            "net.ifnames": "0",
            "panic": "5",
            "ro": true,
            "root": "UUID=4b499d76-769a-40a0-93dc-4a31a59add28"
        },
        "ansible_date_time": {
            "date": "2021-03-29",
            "day": "29",
            "epoch": "1616989366",
            "hour": "11",
            "iso8601": "2021-03-29T03:42:46Z",
            "iso8601_basic": "20210329T114246426643",
            "iso8601_basic_short": "20210329T114246",
            "iso8601_micro": "2021-03-29T03:42:46.426643Z",
            "minute": "42",
            "month": "03",
            "second": "46",
            "time": "11:42:46",
            "tz": "CST",
            "tz_offset": "+0800",
            "weekday": "Monday",
            "weekday_number": "1",
            "weeknumber": "13",
            "year": "2021"
        },
        "ansible_default_ipv4": {
            "address": "172.19.0.11",
            "alias": "eth0",
            "broadcast": "172.19.15.255",
            "gateway": "172.19.0.1",
            "interface": "eth0",
            "macaddress": "52:54:00:4a:8b:63",
            "mtu": 1500,
            "netmask": "255.255.240.0",
            "network": "172.19.0.0",
            "type": "ether"
        },
        "ansible_default_ipv6": {
            "address": "fe80::5054:ff:fe4a:8b63",
            "interface": "eth0",
            "macaddress": "52:54:00:4a:8b:63",
            "mtu": 1500,
            "prefix": "64",
            "scope": "link",
            "type": "ether"
        },
        "ansible_device_links": {
            "ids": {
                "sr0": [
                    "ata-QEMU_DVD-ROM_QM00002"
                ]
            },
            "labels": {
                "sr0": [
                    "config-2"
                ]
            },
            "masters": {},
            "uuids": {
                "sr0": [
                    "2021-03-18-14-18-09-00"
                ],
                "vda1": [
                    "4b499d76-769a-40a0-93dc-4a31a59add28"
                ]
            }
        },
        "ansible_devices": {
            "loop0": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "0",
                "sectorsize": "512",
                "size": "0.00 Bytes",
                "support_discard": "0",
                "vendor": null,
                "virtual": 1
            },
            "sr0": {
                "holders": [],
                "host": "IDE interface: Intel Corporation 82371SB PIIX3 IDE [Natoma/Triton II]",
                "links": {
                    "ids": [
                        "ata-QEMU_DVD-ROM_QM00002"
                    ],
                    "labels": [
                        "config-2"
                    ],
                    "masters": [],
                    "uuids": [
                        "2021-03-18-14-18-09-00"
                    ]
                },
                "model": "QEMU DVD-ROM",
                "partitions": {},
                "removable": "1",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "deadline",
                "sectors": "242864",
                "sectorsize": "2048",
                "size": "118.59 MB",
                "support_discard": "0",
                "vendor": "QEMU",
                "virtual": 1
            },
            "vda": {
                "holders": [],
                "host": "SCSI storage controller: Red Hat, Inc. Virtio block device",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {
                    "vda1": {
                        "holders": [],
                        "links": {
                            "ids": [],
                            "labels": [],
                            "masters": [],
                            "uuids": [
                                "4b499d76-769a-40a0-93dc-4a31a59add28"
                            ]
                        },
                        "sectors": "104855519",
                        "sectorsize": 512,
                        "size": "50.00 GB",
                        "start": "2048",
                        "uuid": "4b499d76-769a-40a0-93dc-4a31a59add28"
                    }
                },
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "104857600",
                "sectorsize": "512",
                "size": "50.00 GB",
                "support_discard": "0",
                "vendor": "0x1af4",
                "virtual": 1
            }
        },
        "ansible_distribution": "CentOS",
        "ansible_distribution_file_parsed": true,
        "ansible_distribution_file_path": "/etc/redhat-release",
        "ansible_distribution_file_variety": "RedHat",
        "ansible_distribution_major_version": "7",
        "ansible_distribution_release": "Core",
        "ansible_distribution_version": "7.8",
        "ansible_dns": {
            "nameservers": [
                "183.60.82.98",
                "183.60.83.19"
            ]
        },
        "ansible_docker0": {
            "active": false,
            "device": "docker0",
            "features": {
                "busy_poll": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "on",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "netns_local": "on [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "off [fixed]",
                "rx_fcs": "off [fixed]",
                "rx_gro_hw": "off [fixed]",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "off [fixed]",
                "rx_vlan_offload": "off [fixed]",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "off [fixed]",
                "tx_checksumming": "on",
                "tx_fcoe_segmentation": "on",
                "tx_gre_csum_segmentation": "on",
                "tx_gre_segmentation": "on",
                "tx_gso_partial": "on",
                "tx_gso_robust": "on",
                "tx_ipip_segmentation": "on",
                "tx_lockless": "on [fixed]",
                "tx_nocache_copy": "off",
                "tx_scatter_gather": "on",
                "tx_scatter_gather_fraglist": "on",
                "tx_sctp_segmentation": "on",
                "tx_sit_segmentation": "on",
                "tx_tcp6_segmentation": "on",
                "tx_tcp_ecn_segmentation": "on",
                "tx_tcp_mangleid_segmentation": "on",
                "tx_tcp_segmentation": "on",
                "tx_udp_tnl_csum_segmentation": "on",
                "tx_udp_tnl_segmentation": "on",
                "tx_vlan_offload": "on",
                "tx_vlan_stag_hw_insert": "on",
                "udp_fragmentation_offload": "on",
                "vlan_challenged": "off [fixed]"
            },
            "hw_timestamp_filters": [],
            "id": "8000.0242edf45bd3",
            "interfaces": [],
            "ipv4": {
                "address": "172.17.0.1",
                "broadcast": "172.17.255.255",
                "netmask": "255.255.0.0",
                "network": "172.17.0.0"
            },
            "ipv6": [
                {
                    "address": "fe80::42:edff:fef4:5bd3",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "02:42:ed:f4:5b:d3",
            "mtu": 1500,
            "promisc": false,
            "stp": false,
            "timestamping": [
                "rx_software",
                "software"
            ],
            "type": "bridge"
        },
        "ansible_domain": "",
        "ansible_effective_group_id": 0,
        "ansible_effective_user_id": 0,
        "ansible_env": {
            "HISTSIZE": "3000",
            "HISTTIMEFORMAT": "%F %T ",
            "HOME": "/root",
            "HOSTNAME": "VM-0-11-centos",
            "LANG": "en_US.utf8",
            "LESSOPEN": "||/usr/bin/lesspipe.sh %s",
            "LOGNAME": "root",
            "LS_COLORS": "rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=01;05;37;41:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.axv=01;35:*.anx=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=01;36:*.au=01;36:*.flac=01;36:*.mid=01;36:*.midi=01;36:*.mka=01;36:*.mp3=01;36:*.mpc=01;36:*.ogg=01;36:*.ra=01;36:*.wav=01;36:*.axa=01;36:*.oga=01;36:*.spx=01;36:*.xspf=01;36:",
            "MAIL": "/var/spool/mail/root",
            "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin",
            "PROMPT_COMMAND": "history -a; printf \"\\033]0;%s@%s:%s\\007\" \"${USER}\" \"${HOSTNAME%%.*}\" \"${PWD/#$HOME/~}\"",
            "PWD": "/root",
            "SHELL": "/bin/bash",
            "SHLVL": "3",
            "SSH_CLIENT": "175.9.29.126 5889 22",
            "SSH_CONNECTION": "175.9.29.126 5889 172.19.0.11 22",
            "SSH_TTY": "/dev/pts/0",
            "TERM": "xterm",
            "USER": "root",
            "XDG_RUNTIME_DIR": "/run/user/0",
            "XDG_SESSION_ID": "19552",
            "_": "/usr/bin/python2"
        },
        "ansible_eth0": {
            "active": true,
            "device": "eth0",
            "features": {
                "busy_poll": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "off [requested on]",
                "highdma": "on [fixed]",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "netns_local": "off [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "on [fixed]",
                "rx_fcs": "off [fixed]",
                "rx_gro_hw": "off [fixed]",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "on [fixed]",
                "rx_vlan_offload": "off [fixed]",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "off",
                "tcp_segmentation_offload": "off",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "off [fixed]",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "off [fixed]",
                "tx_checksumming": "off",
                "tx_fcoe_segmentation": "off [fixed]",
                "tx_gre_csum_segmentation": "off [fixed]",
                "tx_gre_segmentation": "off [fixed]",
                "tx_gso_partial": "off [fixed]",
                "tx_gso_robust": "off [fixed]",
                "tx_ipip_segmentation": "off [fixed]",
                "tx_lockless": "off [fixed]",
                "tx_nocache_copy": "off",
                "tx_scatter_gather": "off [fixed]",
                "tx_scatter_gather_fraglist": "off [fixed]",
                "tx_sctp_segmentation": "off [fixed]",
                "tx_sit_segmentation": "off [fixed]",
                "tx_tcp6_segmentation": "off [fixed]",
                "tx_tcp_ecn_segmentation": "off [fixed]",
                "tx_tcp_mangleid_segmentation": "off [fixed]",
                "tx_tcp_segmentation": "off [fixed]",
                "tx_udp_tnl_csum_segmentation": "off [fixed]",
                "tx_udp_tnl_segmentation": "off [fixed]",
                "tx_vlan_offload": "off [fixed]",
                "tx_vlan_stag_hw_insert": "off [fixed]",
                "udp_fragmentation_offload": "off [fixed]",
                "vlan_challenged": "off [fixed]"
            },
            "hw_timestamp_filters": [],
            "ipv4": {
                "address": "172.19.0.11",
                "broadcast": "172.19.15.255",
                "netmask": "255.255.240.0",
                "network": "172.19.0.0"
            },
            "ipv6": [
                {
                    "address": "fe80::5054:ff:fe4a:8b63",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "52:54:00:4a:8b:63",
            "module": "virtio_net",
            "mtu": 1500,
            "pciid": "virtio0",
            "promisc": false,
            "timestamping": [
                "rx_software",
                "software"
            ],
            "type": "ether"
        },
        "ansible_fibre_channel_wwn": [],
        "ansible_fips": false,
        "ansible_form_factor": "Other",
        "ansible_fqdn": "VM-0-11-centos",
        "ansible_hostname": "VM-0-11-centos",
        "ansible_hostnqn": "",
        "ansible_interfaces": [
            "br-2f206deb7914",
            "docker0",
            "vethcbd8671",
            "br-be93c3b27dc7",
            "lo",
            "br-f4e97043f974",
            "veth2d333ca",
            "veth477c3d2",
            "br-9a4737a41426",
            "br-9651f99a5578",
            "veth0cf6c64",
            "eth0"
        ],
        "ansible_is_chroot": false,
        "ansible_iscsi_iqn": "iqn.1994-05.com.redhat:b83e0e28a2",
        "ansible_kernel": "3.10.0-1127.13.1.el7.x86_64",
        "ansible_kernel_version": "#1 SMP Tue Jun 23 15:46:38 UTC 2020",
        "ansible_lo": {
            "active": true,
            "device": "lo",
            "features": {
                "busy_poll": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "on [fixed]",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "on [fixed]",
                "netns_local": "on [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "on [fixed]",
                "rx_fcs": "off [fixed]",
                "rx_gro_hw": "off [fixed]",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "off [fixed]",
                "rx_vlan_offload": "off [fixed]",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on [fixed]",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "on [fixed]",
                "tx_checksumming": "on",
                "tx_fcoe_segmentation": "off [fixed]",
                "tx_gre_csum_segmentation": "off [fixed]",
                "tx_gre_segmentation": "off [fixed]",
                "tx_gso_partial": "off [fixed]",
                "tx_gso_robust": "off [fixed]",
                "tx_ipip_segmentation": "off [fixed]",
                "tx_lockless": "on [fixed]",
                "tx_nocache_copy": "off [fixed]",
                "tx_scatter_gather": "on [fixed]",
                "tx_scatter_gather_fraglist": "on [fixed]",
                "tx_sctp_segmentation": "on",
                "tx_sit_segmentation": "off [fixed]",
                "tx_tcp6_segmentation": "on",
                "tx_tcp_ecn_segmentation": "on",
                "tx_tcp_mangleid_segmentation": "on",
                "tx_tcp_segmentation": "on",
                "tx_udp_tnl_csum_segmentation": "off [fixed]",
                "tx_udp_tnl_segmentation": "off [fixed]",
                "tx_vlan_offload": "off [fixed]",
                "tx_vlan_stag_hw_insert": "off [fixed]",
                "udp_fragmentation_offload": "on",
                "vlan_challenged": "on [fixed]"
            },
            "hw_timestamp_filters": [],
            "ipv4": {
                "address": "127.0.0.1",
                "broadcast": "",
                "netmask": "255.0.0.0",
                "network": "127.0.0.0"
            },
            "ipv6": [
                {
                    "address": "::1",
                    "prefix": "128",
                    "scope": "host"
                }
            ],
            "mtu": 65536,
            "promisc": false,
            "timestamping": [
                "rx_software",
                "software"
            ],
            "type": "loopback"
        },
        "ansible_local": {},
        "ansible_lsb": {},
        "ansible_lvm": {
            "lvs": {},
            "pvs": {},
            "vgs": {}
        },
        "ansible_machine": "x86_64",
        "ansible_machine_id": "9d6bbb8b60264e3eb3d39f9837e85fa5",
        "ansible_memfree_mb": 154,
        "ansible_memory_mb": {
            "nocache": {
                "free": 6175,
                "used": 1646
            },
            "real": {
                "free": 154,
                "total": 7821,
                "used": 7667
            },
            "swap": {
                "cached": 0,
                "free": 2047,
                "total": 2047,
                "used": 0
            }
        },
        "ansible_memtotal_mb": 7821,
        "ansible_mounts": [
            {
                "block_available": 8743479,
                "block_size": 4096,
                "block_total": 12868467,
                "block_used": 4124988,
                "device": "/dev/vda1",
                "fstype": "ext4",
                "inode_available": 2971959,
                "inode_total": 3276800,
                "inode_used": 304841,
                "mount": "/",
                "options": "rw,relatime,data=ordered",
                "size_available": 35813289984,
                "size_total": 52709240832,
                "uuid": "4b499d76-769a-40a0-93dc-4a31a59add28"
            }
        ],
        "ansible_nodename": "VM-0-11-centos",
        "ansible_os_family": "RedHat",
        "ansible_pkg_mgr": "yum",
        "ansible_proc_cmdline": {
            "BOOT_IMAGE": "/boot/vmlinuz-3.10.0-1127.13.1.el7.x86_64",
            "LANG": "en_US.UTF-8",
            "biosdevname": "0",
            "console": [
                "ttyS0",
                "tty0"
            ],
            "crashkernel": "auto",
            "intel_idle.max_cstate": "1",
            "intel_pstate": "disable",
            "net.ifnames": "0",
            "panic": "5",
            "ro": true,
            "root": "UUID=4b499d76-769a-40a0-93dc-4a31a59add28"
        },
        "ansible_processor": [
            "0",
            "GenuineIntel",
            "Intel(R) Xeon(R) Platinum 8255C CPU @ 2.50GHz",
            "1",
            "GenuineIntel",
            "Intel(R) Xeon(R) Platinum 8255C CPU @ 2.50GHz"
        ],
        "ansible_processor_cores": 2,
        "ansible_processor_count": 1,
        "ansible_processor_threads_per_core": 1,
        "ansible_processor_vcpus": 2,
        "ansible_product_name": "CVM",
        "ansible_product_serial": "9d6bbb8b-6026-4e3e-b3d3-9f9837e85fa5",
        "ansible_product_uuid": "9D6BBB8B-6026-4E3E-B3D3-9F9837E85FA5",
        "ansible_product_version": "3.0",
        "ansible_python": {
            "executable": "/usr/bin/python2",
            "has_sslcontext": true,
            "type": "CPython",
            "version": {
                "major": 2,
                "micro": 5,
                "minor": 7,
                "releaselevel": "final",
                "serial": 0
            },
            "version_info": [
                2,
                7,
                5,
                "final",
                0
            ]
        },
        "ansible_python_version": "2.7.5",
        "ansible_real_group_id": 0,
        "ansible_real_user_id": 0,
        "ansible_selinux": {
            "status": "disabled"
        },
        "ansible_selinux_python_present": true,
        "ansible_service_mgr": "systemd",
        "ansible_ssh_host_key_dsa_public": "ddd",
        "ansible_ssh_host_key_ecdsa_public": "ddd",
        "ansible_ssh_host_key_ed25519_public": "ddd",
        "ansible_ssh_host_key_rsa_public": "ddd",
        "ansible_swapfree_mb": 2047,
        "ansible_swaptotal_mb": 2047,
        "ansible_system": "Linux",
        "ansible_system_capabilities": [
            "cap_chown",
            "cap_dac_override",
            "cap_dac_read_search",
            "cap_fowner",
            "cap_fsetid",
            "cap_kill",
            "cap_setgid",
            "cap_setuid",
            "cap_setpcap",
            "cap_linux_immutable",
            "cap_net_bind_service",
            "cap_net_broadcast",
            "cap_net_admin",
            "cap_net_raw",
            "cap_ipc_lock",
            "cap_ipc_owner",
            "cap_sys_module",
            "cap_sys_rawio",
            "cap_sys_chroot",
            "cap_sys_ptrace",
            "cap_sys_pacct",
            "cap_sys_admin",
            "cap_sys_boot",
            "cap_sys_nice",
            "cap_sys_resource",
            "cap_sys_time",
            "cap_sys_tty_config",
            "cap_mknod",
            "cap_lease",
            "cap_audit_write",
            "cap_audit_control",
            "cap_setfcap",
            "cap_mac_override",
            "cap_mac_admin",
            "cap_syslog",
            "35",
            "36+ep"
        ],
        "ansible_system_capabilities_enforced": "True",
        "ansible_system_vendor": "Tencent Cloud",
        "ansible_uptime_seconds": 941063,
        "ansible_user_dir": "/root",
        "ansible_user_gecos": "root",
        "ansible_user_gid": 0,
        "ansible_user_id": "root",
        "ansible_user_shell": "/bin/bash",
        "ansible_user_uid": 0,
        "ansible_userspace_architecture": "x86_64",
        "ansible_userspace_bits": "64",
        "ansible_veth0cf6c64": {
            "active": true,
            "device": "veth0cf6c64",
            "features": {
                "busy_poll": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "on",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "netns_local": "off [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "on",
                "rx_fcs": "off [fixed]",
                "rx_gro_hw": "off [fixed]",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "off [fixed]",
                "rx_vlan_offload": "on",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "on",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "on",
                "tx_checksumming": "on",
                "tx_fcoe_segmentation": "off [fixed]",
                "tx_gre_csum_segmentation": "on",
                "tx_gre_segmentation": "on",
                "tx_gso_partial": "off [fixed]",
                "tx_gso_robust": "off [fixed]",
                "tx_ipip_segmentation": "on",
                "tx_lockless": "on [fixed]",
                "tx_nocache_copy": "off",
                "tx_scatter_gather": "on",
                "tx_scatter_gather_fraglist": "on",
                "tx_sctp_segmentation": "on",
                "tx_sit_segmentation": "on",
                "tx_tcp6_segmentation": "on",
                "tx_tcp_ecn_segmentation": "on",
                "tx_tcp_mangleid_segmentation": "on",
                "tx_tcp_segmentation": "on",
                "tx_udp_tnl_csum_segmentation": "on",
                "tx_udp_tnl_segmentation": "on",
                "tx_vlan_offload": "on",
                "tx_vlan_stag_hw_insert": "on",
                "udp_fragmentation_offload": "on",
                "vlan_challenged": "off [fixed]"
            },
            "hw_timestamp_filters": [],
            "ipv6": [
                {
                    "address": "fe80::14d0:b6ff:fecb:a383",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "16:d0:b6:cb:a3:83",
            "mtu": 1500,
            "promisc": true,
            "speed": 10000,
            "timestamping": [
                "rx_software",
                "software"
            ],
            "type": "ether"
        },
        "ansible_veth2d333ca": {
            "active": true,
            "device": "veth2d333ca",
            "features": {
                "busy_poll": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "on",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "netns_local": "off [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "on",
                "rx_fcs": "off [fixed]",
                "rx_gro_hw": "off [fixed]",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "off [fixed]",
                "rx_vlan_offload": "on",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "on",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "on",
                "tx_checksumming": "on",
                "tx_fcoe_segmentation": "off [fixed]",
                "tx_gre_csum_segmentation": "on",
                "tx_gre_segmentation": "on",
                "tx_gso_partial": "off [fixed]",
                "tx_gso_robust": "off [fixed]",
                "tx_ipip_segmentation": "on",
                "tx_lockless": "on [fixed]",
                "tx_nocache_copy": "off",
                "tx_scatter_gather": "on",
                "tx_scatter_gather_fraglist": "on",
                "tx_sctp_segmentation": "on",
                "tx_sit_segmentation": "on",
                "tx_tcp6_segmentation": "on",
                "tx_tcp_ecn_segmentation": "on",
                "tx_tcp_mangleid_segmentation": "on",
                "tx_tcp_segmentation": "on",
                "tx_udp_tnl_csum_segmentation": "on",
                "tx_udp_tnl_segmentation": "on",
                "tx_vlan_offload": "on",
                "tx_vlan_stag_hw_insert": "on",
                "udp_fragmentation_offload": "on",
                "vlan_challenged": "off [fixed]"
            },
            "hw_timestamp_filters": [],
            "ipv6": [
                {
                    "address": "fe80::8874:21ff:fe2a:cada",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "8a:74:21:2a:ca:da",
            "mtu": 1500,
            "promisc": true,
            "speed": 10000,
            "timestamping": [
                "rx_software",
                "software"
            ],
            "type": "ether"
        },
        "ansible_veth477c3d2": {
            "active": true,
            "device": "veth477c3d2",
            "features": {
                "busy_poll": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "on",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "netns_local": "off [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "on",
                "rx_fcs": "off [fixed]",
                "rx_gro_hw": "off [fixed]",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "off [fixed]",
                "rx_vlan_offload": "on",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "on",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "on",
                "tx_checksumming": "on",
                "tx_fcoe_segmentation": "off [fixed]",
                "tx_gre_csum_segmentation": "on",
                "tx_gre_segmentation": "on",
                "tx_gso_partial": "off [fixed]",
                "tx_gso_robust": "off [fixed]",
                "tx_ipip_segmentation": "on",
                "tx_lockless": "on [fixed]",
                "tx_nocache_copy": "off",
                "tx_scatter_gather": "on",
                "tx_scatter_gather_fraglist": "on",
                "tx_sctp_segmentation": "on",
                "tx_sit_segmentation": "on",
                "tx_tcp6_segmentation": "on",
                "tx_tcp_ecn_segmentation": "on",
                "tx_tcp_mangleid_segmentation": "on",
                "tx_tcp_segmentation": "on",
                "tx_udp_tnl_csum_segmentation": "on",
                "tx_udp_tnl_segmentation": "on",
                "tx_vlan_offload": "on",
                "tx_vlan_stag_hw_insert": "on",
                "udp_fragmentation_offload": "on",
                "vlan_challenged": "off [fixed]"
            },
            "hw_timestamp_filters": [],
            "ipv6": [
                {
                    "address": "fe80::2cae:e1ff:fee1:aa10",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "2e:ae:e1:e1:aa:10",
            "mtu": 1500,
            "promisc": true,
            "speed": 10000,
            "timestamping": [
                "rx_software",
                "software"
            ],
            "type": "ether"
        },
        "ansible_vethcbd8671": {
            "active": true,
            "device": "vethcbd8671",
            "features": {
                "busy_poll": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "on",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "netns_local": "off [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "on",
                "rx_fcs": "off [fixed]",
                "rx_gro_hw": "off [fixed]",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "off [fixed]",
                "rx_vlan_offload": "on",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "on",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "on",
                "tx_checksumming": "on",
                "tx_fcoe_segmentation": "off [fixed]",
                "tx_gre_csum_segmentation": "on",
                "tx_gre_segmentation": "on",
                "tx_gso_partial": "off [fixed]",
                "tx_gso_robust": "off [fixed]",
                "tx_ipip_segmentation": "on",
                "tx_lockless": "on [fixed]",
                "tx_nocache_copy": "off",
                "tx_scatter_gather": "on",
                "tx_scatter_gather_fraglist": "on",
                "tx_sctp_segmentation": "on",
                "tx_sit_segmentation": "on",
                "tx_tcp6_segmentation": "on",
                "tx_tcp_ecn_segmentation": "on",
                "tx_tcp_mangleid_segmentation": "on",
                "tx_tcp_segmentation": "on",
                "tx_udp_tnl_csum_segmentation": "on",
                "tx_udp_tnl_segmentation": "on",
                "tx_vlan_offload": "on",
                "tx_vlan_stag_hw_insert": "on",
                "udp_fragmentation_offload": "on",
                "vlan_challenged": "off [fixed]"
            },
            "hw_timestamp_filters": [],
            "ipv6": [
                {
                    "address": "fe80::688a:7ff:fea2:9a76",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "6a:8a:07:a2:9a:76",
            "mtu": 1500,
            "promisc": true,
            "speed": 10000,
            "timestamping": [
                "rx_software",
                "software"
            ],
            "type": "ether"
        },
        "ansible_virtualization_role": "guest",
        "ansible_virtualization_type": "kvm",
        "gather_subset": [
            "all"
        ],
        "module_setup": true
    },
    "changed": false
}

```
## [Ansible Tower](https://support.websoft9.com/docs/awx/zh)
