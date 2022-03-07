---
sidebar_position: 3
slug: /python/study
tags:
  - Python
  - 运行环境
---


# 原理学习

**Python Runtime** 是一个产品化的全栈运行环境，包含：[Python](https://www.python.org/), Django, Nginx, MySQL, Docker 以及其他组件，它让用户专注于应用程序的发布，以可靠、稳定、可控的方式部署各种不同类型的 Python 应用程序，在提示效率的同时减少生产环境中人为出错的风险。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/python/python-infra-websoft9.png)

## 架构管理

### 关于

[Python](https://www.python.org/) 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。Python 的语法具有非常好的可读性，是典型的**简单主义思想**的语言，是初级程序员非常喜爱的一个入门语言。同时，Python拥有完整的生态，有海量的开源库可用，从简单的文字处理到web开发，再到科学计算甚至是深度学习，都占有一席之地。


- **Python 是一种解释型语言：** 这意味着开发过程中没有了编译这个环节。类似于PHP和Perl语言。
- **Python 是交互式语言：** 这意味着，您可以在一个 Python 提示符 **>>>** 后直接执行代码。
- **Python 是面向对象语言:** 这意味着Python支持面向对象的风格或代码封装在对象的编

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/python/python-gui-websoft9.png)


### 安装

Python 广受欢迎，故大部分 Linux 发行版，默认都安装了 Python。只需在 Linux 命令上输入命令 `python`，就会进入它的交互式界面。

```
>> python
```

如果你的Linux上没有Python，可以通过如下两种方式进行安装：

#### 在线安装

在线安装是通过系统的 `yum` 或 `apt` 命令下拉远程仓库中提供的已有 Python 安装包的方式进行安装。

```
# Centos & redhat
yum install python
yum install python3

# Ubuntu&Debian
apt install python
apt install python3
```

在线安装有两个注意事项：

* 在服务器配置好软件仓库
* 不同的仓库中 Python 的包的名称不同，可能是：python3, python38, python3.8, rh-python38-scl 等。


#### 源码安装

源码安装将 Python 的源码下载到服务器后，在服务器再编译和配置的一种安装方法。  

源码安装参考官方文档 [Building Python](https://docs.python.org/3.9/using/unix.html#building-python)，这个是最权威最全面的参考资料。

源码安装相对在线安装会更为复杂，且编译过程中可能需处理异常情况才能成功安装。

### 卸载

Python 的卸载会有多个步骤，但总体思路是：获取已安装的模块和内核清单，然后卸载模块，再删除 Python 主文件夹。  

下面以卸载 Python 3.8 为例，介绍卸载的方法：

```
sudo python3.8 -m ensurepip
sudo python3.8 -m pip list
sudo python3.8 -m pip uninstall $(python3.8 -m pip list | cut -d" " -f1)
sudo rm -rf /usr/local/lib*/python3.8/
```

### 解释器

Python 解释器（Interpreter）即 Python 的运行内核，下面的图精准的解释 Python 程序的运行原理：

![Python 解释器 Websoft9](https://libs.websoft9.com/Websoft9/DocsPicture/zh/python/python-interpreter-websoft9.png)

从图中可见 **Interpreter** 是 Python 最重要的内核之一，它具有编译器和虚拟机两方面的功能。

* 编译器：词法分析，语法解释，将 Python 代码编译成字节码（一种类似汇编的代码）
* 虚拟机：模仿可执行文件的入栈出栈调用顺序执行 Python 程序

> 正因为有了解释器的存在，使得 Python 程序无需编译成机器码，就可以实现跨平台运行。

### 编译

虽然 Python 无需像 C/C++ 那样编译成字节码，但为了提高运行速度，Python 也支持将程序预先编译成 .pyc 结尾的文件。

### 模块与包

一个 xxx.py 程序文件，即一个 Python 模块。  

多个模块以一定的规则，组合成树形结构的文件夹就是包。  

下面是一个典型的 Python 包，其中 `sound` 是包的名字。

```
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

通过 import sound.effects.echo 的方式加载包中的模块。

### 包构建与分发

下面讲述如何构建一个包（[延伸阅读](https://zhuanlan.zhihu.com/p/128020789)），并发布到 [pip 官网](https://pypi.org)。  

1. 在项目中新建两个文件：setup.py, MANIFEST.in
2. setup.py 文件中存放下面的示例代码
   ```
   from setuptools import setup, find_packages
   setup(
    name = "demo",
    version = "0.1",
    packages = find_packages(),
   )
   ```
3. MANIFEST.in 存放项目所需的静态资源（非必须）
   ```
   recursive-include font *
   recursive-include Images *
   recursive-include sounds *
   ```
4. 在当前目录下输入打包命令，打包成功，在目录下生成 dist文件夹 
   ```
   python setup.py sdist
   ```
5. pip 官网上[注册账号](https://pypi.org/account/register/)，运行下面的命令发布
   ```
   pip install twine
   twine upload dist/*
   ```

发布包的难点在于构建包，也就是编写 setup.py 文件。另外，也可用编写 Makefile 来给 Python 打包。  

与安装打包相关的技术包括：setuptools（distutils改进版）, pip（asyInstall改进版），Python 二进制包格式（.egg，.whl）

### 虚拟环境

用户在编写应用程序的时候，通常会安装第三方的 Python 包，不同的应用程序可能对包有不同的要求，而特定的包可能会依赖其他的 Python 包，这种多版本和复杂依赖的情况下，很有可能会导致包冲突。  

虚拟环境就是为每一个用户的应用程序创建一个单独的 Python 隔离环境，用户所安装的第三方包会安装到虚拟隔离环境的位置，从而避免冲突。

#### 创建

Python3.6 之后，默认提供了虚拟环境模块 [venv](https://docs.python.org/zh-cn/3/tutorial/venv.html)，只需要运行如下命令，即可创建虚拟环境。
```
python3 -m venv myapp
```
下图是创建的隔离环境目录，可见 venv 帮助我们创建了完整的 Python 所需的文件系统。  
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/python/python-venv001-websoft9.png)

#### 激活

通过 source 命令，激活虚拟环境:

```
source myapp/bin/active
```

一旦进入激活状态之后，Shell 的前缀便变成 `(myapp) [root@...]#` 的样式。


### 可执行脚本

在 Linux 系统中，Python 模块经过几个步骤的修改，就可以像 Shell 脚本一样运行。

下面介绍一个完整的范例：

1. 创建一个 Python 模块，假如名称为 websoft9.py
2. 增加一段代码到文件中
   ```
   #!/usr/bin/env python3.6
   print("hello world!")

   ```
3. 修改模块为可执行文件
   ```
   chmod +x websoft9.py
   ```

4. 执行运行 `./websoft9.py` 测试效果。

### pip

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


### uWSGI

[uWSGI](https://uwsgi-docs.readthedocs.io/) 是一个快速的、纯C语言开发的、自维护的、对开发者友好的 WSGI 服务器，旨在提供专业的 Python web应用发布和开发。可使用 C/C++/Objective-C 来为 uWSGI 编写插件。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/python/django-behind-uwsgi-nginx.png)

全局路径：  

uWSGI 配置文件： */etc/uwsgi.ini*  
uWSGI 目录： */etc/uwsgi.d*  

## 词汇表

#### CPython
[CPython](http://www.python.org/) 是 Python 的参考实现，用 C 语言编写。它将 Python 代码编译为中间字节码，然后由虚拟机解释。 CPython 提供与 Python 包和 C 扩展模块的最高级别的兼容性。

#### PyPy
[PyPy](http://pypy.org/) 是一种 Python 解释器，在称为 RPython 的 Python 语言的受限静态类型子集中实现。 解释器具有即时编译器并支持多个后端（C、CLI、JVM）。
PyPy 旨在最大程度地兼容参考 CPython 实现，同时提高性能。

#### Jython
[Jython](http://www.jython.org/) 是一种 Python 实现，可将 Python 代码编译为 Java 字节码，然后由 JVM（Java 虚拟机）执行。 此外，它还能够导入和使用任何 Java 类，例如 Python 模块。
如果您需要与现有的 Java 代码库交互或有其他原因需要为 JVM 编写 Python 代码，那么 Jython 是最佳选择。

#### IronPython
[IronPython](http://ironpython.net/) 是用于 .NET 框架的 Python 实现。 它可以同时使用 Python 和 .NET 框架库，还可以将 Python 代码暴露给 .NET 框架中的其他语言。
[Visual Studio 的 Python 工具](http://ironpython.net/tools/) 将 IronPython 直接集成到 Visual Studio 开发环境中，使其成为 Windows 开发人员的理想选择。

#### PythonNet
[Python for .NET](http://pythonnet.github.io/) 是一个包，可将本地安装的 Python 安装与 .NET 公共语言运行时 (CLR) 无缝集成。 这与 IronPython（见上文）所采用的方法相反，与其竞争相比，它更具互补性。

#### ".egg" 文件
Python Eggs 是一种将附加信息与 Python 项目捆绑在一起的方式，它允许在运行时检查和满足项目的依赖关系，并允许项目为其他项目提供插件。

### virtualenv
是一个创建隔离 Python 环境的工具。 virtualenv 的[主页和文档](http://www.virtualenv.org/en/latest/)。

#### easy_install

#### Pip

#### WSGI

#### uWSGI

#### Gunicorn

## 参考

* [Awesome Python](https://github.com/vinta/awesome-python)
* [Python3 菜鸟教程](https://www.runoob.com/python3/python3-tutorial.html)
* [Django 菜鸟教程](https://www.runoob.com/django/django-tutorial.html)