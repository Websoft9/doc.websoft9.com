# Python

Python技术体系博大精深，我们不会在此处展开长篇大论。本章我们重点梳理我们在工作中可能涉及与Python相关的技术，以帮助更好的改善我们的产品，更好的帮助客户建立一个对Python的全局认识。

## 关于

Python 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。Python的语法具有非常好的可读性，是典型的**简单主义思想**的语言，是初级程序员非常喜爱的一个入门语言。同时，Python拥有完整的生态，有海量的开源库可用，从简单的文字处理到web开发，再到科学计算甚至是深度学习，都占有一席之地。

- **Python 是一种解释型语言：** 这意味着开发过程中没有了编译这个环节。类似于PHP和Perl语言。
- **Python 是交互式语言：** 这意味着，您可以在一个 Python 提示符 **>>>** 后直接执行代码。
- **Python 是面向对象语言:** 这意味着Python支持面向对象的风格或代码封装在对象的编程技术。

## 安装

Python由于过于受欢迎，大部分Linux发行版，默认都安装了Python。只需在Linux命令上输入命令 python，就会进入它的交互式界面。

```
>> python
```

如果你的Linux上没有Python，可以通过如下两种方式进行安装：

### 在线安装

在线安装就是通过Linux系统的 yum 或 atp 命令进行安装。

```
# Centos & redhat
yum install python
yum install python3

# Ubuntu&Debian
apt install python
apt install python3
```

在线安装完成就可以立即使用。

### 源码安装

源码安装顾名思义就是将Python的源码下载到服务器，然后完成编译、环境变量设置等一序列后续安装步骤。

源码安装参考Python官方文档，这个是最权威最全面的参考资料

源码安装相对在线安装会更为复杂，建议初学者通过采用在线安装方式。

## 配置文件

## 包管理

Python 是一个有良好生态的开发语言，全球数百万开发者贡献了大量优秀的软件包，Python的包管理工具就是管理和维护第三方扩展软件包的工具。

Python 环境中使用 pip 命令完成各种不同类型的包管理操作：

```
#安装pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python get-pip.py

#查看pip版本
pip --version

#查看包信息
pip show Django

#列出所有已安装的包
pip list

#查看可升级的包
pip list -o

#安装Python包，以Django为例
pip install Django              # 安装
pip install Django -U           # 安装并更新至最新版本
pip install Django==2.1.7       # 指定版本
pip install 'Django>=2.1.7'     # 最小版本

#升级Python模块
pip install --upgrade django==2.1.7

#pip自身的升级
python -m pip install --upgrade pip  
python3 -m pip install --upgrade pip
```

> 一般情况 pip 对应的是 Python 2.7，pip3 对应的是 Python 3.x

## Web 服务

本节我们介绍Python如何处理 http 访问

## Python与系统运维

## 热门软件包

Python是当前最流行的编程语言之一

