---
sidebar_position: 3
slug: /ansible/example
---

# Tasks samples

下面根据常用的场景列出一些代码的范例和技巧：

### 通用属性

Ansible有些属性属于通用属性，适用于所有模块:

```
- name: Upgrade all packages to the latest version for production
  apt:
    name: "*"
    state: latest
    only_upgrade: yes
  register: result // 注册变量
  until: result.msg.find("Could not get lock /var/lib/dpkg") == -1 // 循环条件判断
  retries: // 重试次数
  delay: 10 // 重试间隔时间单位s
  failed_when: "'FAILED' in result.stdout" // 定义错误的条件，满足该条件终止
  when: common_system_upgrade and (init == '1' or init == 1) // 普通条件判断
```

### 文件管理

#### 管理目录

```
- name: Create knowage directory
  file:
    path: /data/wwwroot/knowage
    state: directory
    owner: knowage
    group: knowage


# 删除目录，下载解压，重命名
# if [ ! d "scratch-gui*") ] 这种写法当不存在需要更名的目录的时候会报错，弃用
- name: Remove extra dir
  shell: rm -rf /data/wwwroot/scratch

- name: Download Scratch
  unarchive:
    src: "{{scratch_download_url}}"
    dest: /data/wwwroot
    remote_src: yes

- name: Rename dir name
  shell: if [ $( ls | grep "scratch-gui") ]; then mv scratch-gui* scratch; fi
  args:
    chdir: /data/wwwroot
```

#### 创建文件

```
- name: Create file
  shell: if [ ! $( ls | grep "scratch-gui") ]; then touch scratch-gui; fi
  args:
    chdir: /data/wwwroot


- name: Create recurse directory
  file: 
    path: /data/xuwei/test
    state: directory
    recurse: yes
```

#### 下载解压

```

- name: Unarchive a file that needs to be downloaded (added in 2.0)
  unarchive:
    src: https://example.com/example.zip
    dest: /usr/local/bin
    remote_src: yes
```

#### 软链接

```
- name: Create a Apache Log symbolic link
  file:
    src: '{{item.src}}'
    dest: '{{item.dest}}'
    state: link
  with_items:
    - {src: /etc/apache2,dest: /etc/httpd}
    - {src: /usr/sbin/apache2,dest: /usr/sbin/apache}
    - {src: /usr/sbin/apache2,dest: /usr/sbin/httpd}
    - {src: /etc/apache2/sites-enabled,dest: /etc/httpd/conf.d}
    - {src: /etc/apache2,dest: /etc/httpd/conf}
    - {src: /etc/apache2/apache2.conf,dest: /etc/httpd/conf/httpd.conf}
    - {src: /etc/apache2/sites-available/000-default.conf,dest: /etc/apache2/sites-enabled/vhost.conf}
    - {src: /var/log/apache2,dest: /var/log/httpd}
    - {src: /var/log/apache2,dest: /data/logs/apache}
    - {src: /var/log/apache2,dest: /etc/apache2/logs}
    - {src: /etc/apache2/sites-enabled,dest: /data/config/apache/sites-enabled}
    - {src: /etc/apache2/mods-enabled,dest: /data/config/apache/mods-enabled}
    - {src: /etc/apache2/sites-enabled,dest: /etc/apache2/vhost}

备注: 有变量嵌套时加入单引号即可; 如下apache_version为变量:
    - {src: '/etc/apache2/apache_version/',dest: /etc/apache2/apache}
      如果目标文件夹不存在，不能创建软链接
    - {src: /etc/apache2,dest: /etc/xuwei/httpd}
```

#### 替换

```
#匹配regexp，如果找到，用line替换；找不到，末尾追加line的内容。
- name: Change postgresql databases directory
  lineinfile:
      dest: /etc/postgresql/{{postgresql_version}}/main/postgresql.conf
      regexp: "data_directory = '/var/lib/postgresql/{{postgresql_version}}/main'"
      line: "data_directory = '/data/pgsql'"
      
 #匹配regexp，如果找到，用line替换；找不到，什么都不做。
- name: Change postgresql databases directory
  lineinfile:
      dest: /etc/postgresql/{{postgresql_version}}/main/postgresql.conf
      regexp: "data_directory = '/var/lib/postgresql/{{postgresql_version}}/main'"
      line: "data_directory = '/data/pgsql'"
      backrefs: yes

#匹配regexp，找到后删除这行；找不到，什么都不做。（这种情况下line的内容无意义）
- name: Change postgresql databases directory
  lineinfile:
      dest: /etc/postgresql/{{postgresql_version}}/main/postgresql.conf
      regexp: "data_directory = '/var/lib/postgresql/{{postgresql_version}}/main'"
      state: absent

#特殊字符的匹配，如"."，需要在前面加上\进行转义，否则无法进行正则匹配(#elasticsearch.hosts 本例为替换所有#elasticsearch.hosts开头的行)
- name: elasticsearch.hosts
  lineinfile:
    path: /etc/kibana/kibana.yml
    regexp: '^#elasticsearch\.hosts'
    line: 'elasticsearch.hosts: ["http://localhost:9200"]'
    state: present
    backrefs: yes

#循环替换，数据结构

mysql_configure_extras:
  - name: innodb_buffer_pool_size
    value: 2G
  - name: innodb_log_file_size
    value: 500M

- name: Create MySQL extra databases 
  mysql_db:
    login_user: root
    login_password: '{{mysql_root_password}}'
    name: "{{ item.name }}"
    encoding: "{{ item.encoding | default('utf8mb4',true) }}"
    state: "{{ item.state | default('present',true) }}"
  with_items: "{{ mysql_databases }}"
  when: (mysql_databases is defined) and (mysql_databases != none)
```

### 用户管理

创建用户建议使用user模块，否则重复安装的时候会因为已有用户而报错

```
#创建非登陆用户
- name: Create Mattermost System User
  user:
      name: mattermost 
      create_home: no 
      shell: /usr/sbin/nologin
      
#创建可登陆用户jetty，并在home下创建用户目录
- name: Create jetty User
  user:
    name: jetty
    shell: /usr/bin/bash
    create_home: yes

- name: Create User for Canvas -- adduser --disabled-password --gecos canvas canvas
  user: 
    name: canvas
    comment: canvas
    password_lock: yes

#git克隆并指定分支
- name: Clone onlyoffice in Websoft9 
  git:
    repo: "{{onlyoffice_url}}"
    dest: "/data/wwwroot/onlyoffice"
    version: main
```

### 条件判断

```
# ansible使用when来进行条件判断

在Ansible中，除了比较运算符，还支持逻辑运算符：
and：逻辑与，当左边和右边两个表达式同时为真，则返回真
or：逻辑或，当左右和右边两个表达式任意一个为真，则返回真
not：逻辑否，对表达式取反
()：当一组表达式组合在一起，形成一个更大的表达式，组合内的所有表达式都是逻辑与的关系

defined ：判断变量是否已经定义，已经定义则返回真
undefind ：判断变量是否已经定义，未定义则返回真
none ：判断变量值是否为空，如果变量已经定义，但是变量值为空，则返回真

success 或 succeeded：通过任务的返回信息判断任务的执行状态，任务执行成功则返回真
failure 或 failed：通过任务的返回信息判断任务的执行状态，任务执行失败则返回真
change 或 changed：通过任务的返回信息判断任务的执行状态，任务执行状态为changed则返回真
skip 或 skipped：通过任务的返回信息判断任务的执行状态，当任务没有满足条件，而被跳过执行时，则返回真

file : 判断路径是否是一个文件，如果路径是一个文件则返回真
directory ：判断路径是否是一个目录，如果路径是一个目录则返回真
link ：判断路径是否是一个软链接，如果路径是一个软链接则返回真
mount：判断路径是否是一个挂载点，如果路径是一个挂载点则返回真
exists：判断路径是否存在，如果路径存在则返回真

lower：判断包含字母的字符串中的字母是否是纯小写，字符串中的字母全部为小写则返回真
upper：判断包含字母的字符串中的字母是否是纯大写，字符串中的字母全部为大写则返回真

version：可以用于对比两个版本号的大小，或者与指定的版本号进行对比，使用语法为 version('版本号', '比较操作符')
subset：判断一个list是不是另一个list的子集，是另一个list的子集时返回真
superset : 判断一个list是不是另一个list的父集，是另一个list的父集时返回真
number：判断对象是否是一个数字，是数字则返回真

failed_when: false 此步骤永不失败,用于跳过错误。

#避免重复下载一个大的压缩文件包
- name: Ansible check file exists
  shell: if [ ! $(ls /data/wwwroot/knowage | grep Knowage-*.sh) ]; then echo "need_download";else echo "downloaded";fi
  register: result

- name: Download Knowage, it have 2G, need 10 minutes
  unarchive:
    src: "{{knowage_download_url}}"
    dest: "/data/wwwroot/knowage"
    remote_src: yes
    mode: 0750
  when: result.stdout == "need_download"


#变量testpath是路径信息"/testdir"，判断路径是否存
- debug:
    msg: "file exist"
  when: testpath is exists
  #when: testpath is not exists
 
#判断是否包含"."号 
- name: replace
  debug: msg="323.2323"
  when: teststr is match("[0-9]+\.[0-9]+")

#判断变量：定义，未定义，none
vars:
  testvar: "test"
  testvar1:
tasks:
- debug:
    msg: "Variable is defined"
  when: testvar is defined
- debug:
    msg: "Variable is undefined"
  when: testvar2 is undefined
- debug:
    msg: "The variable is defined, but there is no value"
  when: testvar1 is none

#判断变量是否在数组中
- name: Check OS support, if not support, exit ansible
  fail: msg="OS not supported,exit!"
  when: ansible_distribution not in common_os_support

```

### 获取管理主机信息
```
当我们需要把管理主机获得的信息,到远程主机执行时,可以用如下参数:
connection、delegate_to、local_action
# 检查管理主机文件是否存在?
- name: Check that the compose file exists
  stat:
    path: ./roles/role_docker/templates/apps-{{docker_appname}}-compose.yml
  delegate_to: localhost
  register: file_status

- name: Check that the compose file exists
  stat:
    path: ./roles/role_docker/templates/apps-{{docker_appname}}-compose.yml
  connection: local
  register: file_status

- name: Check that the compose file exists
  local_action:
    stat:
      path: ./roles/role_docker/templates/apps-{{docker_appname}}-compose.yml
  connection: localhost
  register: file_status

 补充: connection: local 可以针对playbook全局使用，而delegate_to: localhost 只能针对role task等局部代理, local_action 不常用
```

### 正则表达式

```
#change string "x.y" to "xy"
- set_fact:
    postgresql_version_regex: "{{ postgresql_version | regex_replace('^(?P<before>.+).(?P<after>\\d+)$', '\\g<before>\\g<after>')}}"
```

### 过滤器
```
tasks:
  - debug:
      #转化为list
      msg: "{{ testvar | list }}"
  - debug:
      #转化为json
      msg: "{{ testvar | list | to_json }}"
  - debug:
      #转化为整数类型
      msg: "{{ testvar | int}}"

#json_query: 用来过滤数组,json的元素属性
users:
- name: tom
  age: 18
- name: jerry
  age: 20

- debug:
      msg: "{{ testvar | json_query('users[*].name') }}"

tasks:
  - debug:
      #将字符串转换成纯大写
      msg: "{{ testvar | upper }}"
  - debug:
      #将字符串转换成纯小写
      msg: "{{ testvar | lower }}"
  - debug:
      #将字符串变成首字母大写,之后所有字母纯小写
      msg: "{{ testvar | capitalize }}"
  - debug:
      #将字符串反转
      msg: "{{ testvar | reverse }}"
  - debug:
      #返回字符串的第一个字符
      msg: "{{ testvar | first }}"
  - debug:
      #返回字符串的最后一个字符
      msg: "{{ testvar | last }}"
  - debug:
      #将字符串开头和结尾的空格去除
      msg: "{{ testvar1 | trim }}"
  - debug:
      #将字符串放在中间，并且设置字符串的长度为30，字符串两边用空格补齐30位长
      msg: "{{ testvar1 | center(width=30) }}"
  - debug:
      #返回字符串长度,length与count等效,可以写为count
      msg: "{{ testvar2 | length }}"
  - debug:
      #将字符串转换成列表，每个字符作为一个元素
      msg: "{{ testvar3 | list }}"
  - debug:
      #将字符串转换成列表，每个字符作为一个元素，并且随机打乱顺序
      msg: "{{ testvar3 | shuffle }}"
  - debug:
      #将字符串转换成列表，每个字符作为一个元素，并且随机打乱顺序
      #在随机打乱顺序时，将ansible_date_time.epoch的值设置为随机种子
      #也可以使用其他值作为随机种子，ansible_date_time.epoch是facts信息
      msg: "{{ testvar3 | shuffle(seed=(ansible_date_time.epoch)) }}"

tasks:
  #在调用shell模块时，如果引用某些变量时需要添加引号，则可以使用quote过滤器代替引号
  - shell: "echo {{teststr | quote}} > /testdir/testfile"
  #上例中shell模块的写法与如下写法完全等效
  #shell: "echo '{{teststr}}' > /testdir/testfile"
  #上例中，如果不对{{teststr}}添加引号，则会报错，因为teststr变量中包含"\n"转义符

  #ternary过滤器可以实现三元运算的效果 示例如下
  #如下示例表示如果name变量的值是John，那么对应的值则为Mr,否则则为Ms
  #简便的实现类似if else对变量赋值的效果
  - debug: 
      msg: "{{ (name == 'John') | ternary('Mr','Ms') }}"
  #而这和"{{ 'Mr' if name == 'John' else 'Ms' }}"是等价的

  #basename过滤器可以获取到一个路径字符串中的文件名
  - debug:
      msg: "{{teststr | basename}}"

  #获取到一个windows路径字符串中的文件名,2.0版本以后的ansible可用
  - debug:
      msg: "{{teststr | win_basename}}"

  #dirname过滤器可以获取到一个路径字符串中的路径名
  - debug:
      msg: "{{teststr | dirname}}"

  #realpath过滤器可以获取软链接文件所指向的真正文件
  - debug:
      msg: "{{ path | realpath }}"

  #relpath过滤器可以获取到path对于“指定路径”来说的“相对路径”
  - debug:
      msg: "{{ path | relpath('/testdir/testdir') }}"
    vars:
      path: "/testdir/ansible"

  #splitext过滤器可以将带有文件名后缀的路径从“.后缀”部分分开
  - debug:
      msg: "{{ path | splitext }}"

  #可以配置之前总结的过滤器，获取到文件后缀
  #msg: "{{ path | splitext | last}}"
  #可以配置之前总结的过滤器，获取到文件前缀名
  #msg: "{{ path | splitext | first | basename}}"

  #to_uuid过滤器能够为对应的字符串生成uuid
  - debug:
      msg: "{{ teststr | to_uuid }}"

  #bool过滤器可以根据字符串的内容返回bool值true或者false
  #字符串的内容为yes、1、True、true则返回布尔值true，字符串内容为其他内容则返回false
  - debug:
      msg: "{{ teststr | bool }}"

  #当和用户交互时，有可能需要用户从两个选项中选择一个，比如是否继续，
  #这时，将用户输入的字符串通过bool过滤器处理后得出布尔值，从而进行判断，比如如下用法
  #- debug:
  #    msg: "output when bool is true"
  #  when: some_string_user_input | bool

  #map过滤器可以从列表中获取到每个元素所共有的某个属性的值，并将这些值组成一个列表
  #当列表中嵌套了列表，不能越级获取属性的值，也就是说只能获取直接子元素的共有属性值。
  - vars:
      users:
      - name: tom
        age: 18
        hobby:
        - Skateboard
        - VideoGame
      - name: jerry
        age: 20
        hobby:
        - Music
    debug:
      msg: "{{ users | map(attribute='name') | list }}"
  #也可以组成一个字符串，用指定的字符隔开，比如分号
  #msg: "{{ users | map(attribute='name') | join(';') }}"

  #使用base64编码方式对字符串进行编码
  - debug:
      msg: "{{ 'hello' | b64encode }}"
  #使用base64编码方式对字符串进行解码
  - debug:
      msg: "{{ 'aGVsbG8=' | b64decode }}"

  #使用sha1算法对字符串进行哈希
  - debug:
      msg: "{{ '123456' | hash('sha1') }}"
  #使用md5算法对字符串进行哈希
  - debug:
      msg: "{{ '123456' | hash('md5') }}"
  #获取到字符串的校验和,与md5哈希值一致
  - debug:
      msg: "{{ '123456' | checksum }}"
  #使用blowfish算法对字符串进行哈希，注:部分系统支持
  - debug:
      msg: "{{ '123456' | hash('blowfish') }}"
  #使用sha256算法对字符串进行哈希,哈希过程中会生成随机"盐",以便无法直接对比出原值
  - debug:
      msg: "{{ '123456' | password_hash('sha256') }}"
  #使用sha256算法对字符串进行哈希,并使用指定的字符串作为"盐"
  - debug:
      msg: "{{ '123456' | password_hash('sha256','mysalt') }}"
  #使用sha512算法对字符串进行哈希,哈希过程中会生成随机"盐",以便无法直接对比出原值
  - debug:
      msg: "{{ '123123' | password_hash('sha512') }}"
  #使用sha512算法对字符串进行哈希,并使用指定的字符串作为"盐"
  - debug:
      msg: "{{ '123123' | password_hash('sha512','ebzL.U5cjaHe55KK') }}"
  #如下方法可以幂等的为每个主机的密码生成对应哈希串
  #有了之前总结的过滤器用法作为基础，你一定已经看懂了
  - debug:
      msg: "{{ '123123' | password_hash('sha512', 65534|random(seed=inventory_hostname)|string) }}"
```

### 循环
| 循环类型 | 关键字 |
|  ----  | ----  |
|标准循环|with_items|   
|遍历字典|with_dict|   
|遍历目录文件|with_fileglob|   
|遍历文件列表的内容|with_file|   
|嵌套循环|with_nested|    
|并行遍历列表|	with_together   |
|遍历列表和索引	|with_indexed_items|   
|重试循环	|until|   
|查找第一个匹配文件|	with_first_found |  
|随机选择	|with_random_choice|  
|在序列中循环	|with_sequence |
```
种类一、标准循环
添加多个用户，并将用户加入不同的组内。
- name: add several users
  user: name={{ item.name }} state=present groups={{ item.groups }}
  with_items:
    - { name: 'testuser1', groups: 'wheel' }
    - { name: 'testuser2', groups: 'root' }

种类二、锚点嵌套循环
分别给用户授予3个数据库的所有权限
- name: give users access to multiple databases
  mysql_user: name={{ item[0] }} priv={{ item[1] }}.*:ALL append_privs=yes password=foo
  with_nested:
    - [ 'alice', 'bob' ]
    - [ 'clientdb', 'employeedb', 'providerdb' ]

种类三、锚点遍历字典
输出用户的姓名和电话
tasks:
  - name: Print phone records
    debug: msg="User {{ item.key }} is {{ item.value.name }} ({{ item.value.telephone }})"
    with_dict: {'alice':{'name':'Alice Appleworth', 'telephone':'123-456-789'},'bob':{'name':'Bob Bananarama', 'telephone':'987-654-3210'} }

种类四、锚点并行遍历列表
tasks:
  - debug: "msg={{ item.0 }} and {{ item.1 }}"
    with_together:
    - [ 'a', 'b', 'c', 'd','e' ]
    - [ 1, 2, 3, 4 ]
如果列表数目不匹配，用None补全

种类五、锚点遍历列表和索引
 - name: indexed loop demo
    debug: "msg='at array position {{ item.0 }} there is a value {{ item.1 }}'"
    with_indexed_items: [1,2,3,4]
item.0 为索引，item.1为值

种类六、锚点遍历文件列表的内容
---
- hosts: all
  tasks:
       - debug: "msg={{ item }}"
      with_file:
        - first_example_file
        - second_example_file

种类七、锚点遍历目录文件
with_fileglob匹配单个目录中的所有文件，非递归匹配模式。
---
- hosts: all
  tasks:
    - file: dest=/etc/fooapp state=directory
    - copy: src={{ item }} dest=/etc/fooapp/ owner=root mode=600
      with_fileglob:
        - /playbooks/files/fooapp/*
当在role中使用with_fileglob的相对路径时，Ansible解析相对于roles/<rolename>/files目录的路径。

种类八、锚点遍历ini文件
lookup.ini
[section1]
value1=section1/value1
value2=section1/value2

[section2]
value1=section2/value1
value2=section2/value2

- debug: msg="{{ item }}"
  with_ini: value[1-2] section=section1 file=lookup.ini re=true
获取section1 里的value1和value2的值

种类九、锚点重试循环 until
- action: shell /usr/bin/foo
  register: result
  until: result.stdout.find("all systems go") != -1
  retries: 5
  delay: 10
"重试次数retries" 的默认值为3，"delay"为5。

锚点查找第一个匹配文件
  tasks:
  - debug: "msg={{ item }}"
    with_first_found:
     - "/tmp/a"
     - "/tmp/b"
     - "/tmp/default.conf"
依次寻找列表中的文件，找到就返回。如果列表中的文件都找不到，任务会报错。

种类十、锚点随机选择with_random_choice
随机选择列表中得一个值
- debug: msg={{ item }}
  with_random_choice:
     - "go through the door"
     - "drink from the goblet"
     - "press the red button"
     - "do nothing"
循环程序的结果
tasks:
debug: "msg={{ item }}"
with_lines: ps aux

种类十一、锚点循环子元素
定义好变量
#varfile
---
users:
  - name: alice
    authorized:
      - /tmp/alice/onekey.pub
      - /tmp/alice/twokey.pub
    mysql:
        password: mysql-password
        hosts:
          - "%"
          - "127.0.0.1"
          - "::1"
          - "localhost"
        privs:
          - "*.*:SELECT"
          - "DB1.*:ALL"
  - name: bob
    authorized:
      - /tmp/bob/id_rsa.pub
    mysql:
        password: other-mysql-password
        hosts:
          - "db1"
        privs:
          - "*.*:SELECT"
          - "DB2.*:ALL"
  tasks:
  - user: name={{ item.name }} state=present generate_ssh_key=yes
    with_items: "{{ users }}"
  - authorized_key: "user={{ item.0.name }} key='{{ lookup('file', item.1) }}'"
    with_subelements:
      - "{{ users }}"
      - authorized
  - name: Setup MySQL users
    mysql_user: name={{ item.0.name }} password={{ item.0.mysql.password }} host={{ item.1 }} priv={{ item.0.mysql.privs | join('/') }}
    with_subelements:
      - "{{ users }}"
      - mysql.hosts
{{ lookup('file', item.1) }} 是查看item.1文件的内容
with_subelements 遍历哈希列表，然后遍历列表中的给定（嵌套）的键。

种类十二、锚点在序列中循环with_sequence
with_sequence以递增的数字顺序生成项序列。 您可以指定开始，结束和可选步骤值。 参数应在key = value对中指定。 'format'是一个printf风格字符串。
数字值可以以十进制，十六进制（0x3f8）或八进制（0600）指定。 不支持负数。
  tasks:
    # 创建组
    - group: name=evens state=present
    - group: name=odds state=present
    # 创建格式为testuser%02x 的0-32 序列的用户
    - user: name={{ item }} state=present groups=evens
      with_sequence: start=0 end=32 format=testuser%02x
    # 创建4-16之间得偶数命名的文件
    - file: dest=/var/stuff/{{ item }} state=directory
      with_sequence: start=4 end=16 stride=2
    # 简单实用序列的方法：创建4 个用户组分表是组group1 group2 group3 group4
    - group: name=group{{ item }} state=present
      with_sequence: count=4

种类十三、锚点随机选择with_random_choice
随机选择列表中得一个值
- debug: msg={{ item }}
  with_random_choice:
     - "go through the door"
     - "drink from the goblet"
     - "press the red button"
     - "do nothing"
```

### 安装

#### yum

#### apt

#When the service name is added, changed or renamed(created soft link ) on Ubuntu 20.04,
#you must reload service before restart the service.
#egg. There is a service at following path(/lib/systemd/system/php-fpm.service)

```
#指定deb在线安装,效果== $ wget https://packages.graylog2.org/repo/packages/graylog-3.3-repository_latest.deb
#                     $ sudo dpkg -i graylog-3.3-repository_latest.deb
- name: Install Graylog
  apt:
    deb: "{{graylog_deb_url}}"
    state: present
    update_cache: yes


# Add specified repository into sources list.
# {{ansible_distribution_version}}=$(lsb_release -cs) 变量转换成 bionic,xenial,focal等。有待进一步优化
# {{ansible_machine}}=$(arch) 变量转成 x86_64

- apt_repository:
    repo: deb http://archive.canonical.com/ubuntu $(lsb_release -cs) partner $(arch)
    repo: deb http://archive.canonical.com/ubuntu {{ansible_distribution_version}} partner {{ansible_machine}}
    #http://mirror.centos.org/centos/6/os/x86_64/
    repo: http://mirror.centos.org/centos/$releasever/os/$basearch/
    state: present

- name: Create a PHP soft link
  file:
    src: '{{item.src}}'
    dest: '{{item.dest}}'
    state: link
  with_items:
    - {src: '/lib/systemd/system/php{{php_version}}-fpm.service',dest: /lib/systemd/system/php-fpm.service}

- name: Ubuntu20.4 must reload service
  shell: systemctl daemon-reload  
  
- name: Restart PHP-FPM
  service:
    name: php-fpm
    state: restarted
    enabled: yes
```

#### aptitude

aptitude 是 Debian GNU/Linux 系统中, 非常神奇的的软件包管理器,基于 APT 机制, 整合了 dselect 和 apt-get的所有功能, 并提供的更多特性,特别是在依赖关系处理上。

```
- name: Use aptitude to skip low version dependencies on libxmlsec1-dev installation
  shell: echo -e "n\ny\n" |aptitude  install libxmlsec1-dev 
```

### 交互

与交互有关的有：pause, expect, prompt 等，各自的用法为：

```
- block:
  - pause:
      prompt: "Give your secret code for Odoo ee download"
    register: prompt
    no_log: yes
    run_once: yes

  - name: Install a .deb package from the internet.
    apt:
      deb: "https://libs.websoft9.com/apps/Odoo/{{ prompt.user_input | b64encode }}/odoo_{{odoo_version}}_e_latest_all.deb"
      autoclean: yes
    when: odoo_distribution == "ee"
    
vars_prompt:
  - name: release_version
    prompt: Product release version
    default: "1.0"
```

