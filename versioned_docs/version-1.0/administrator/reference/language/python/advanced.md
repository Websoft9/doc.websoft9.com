---
slug: /python/advanced
---
# 进阶

[Python](https://www.python.org/) 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。Python 的语法具有非常好的可读性，是典型的**简单主义思想**的语言，是初级程序员非常喜爱的一个入门语言。同时，Python拥有完整的生态，有海量的开源库可用，从简单的文字处理到web开发，再到科学计算甚至是深度学习，都占有一席之地。


- **Python 是一种解释型语言：** 这意味着开发过程中没有了编译这个环节。类似于PHP和Perl语言。
- **Python 是交互式语言：** 这意味着，您可以在一个 Python 提示符 **>>>** 后直接执行代码。
- **Python 是面向对象语言:** 这意味着Python支持面向对象的风格或代码封装在对象的编

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/python/python-gui-websoft9.png)


## 安装

Python 广受欢迎，故大部分 Linux 发行版，默认都安装了 Python。只需在 Linux 命令上输入命令 `python`，就会进入它的交互式界面。

```
>> python
```

如果你的Linux上没有Python，可以通过如下两种方式进行安装：

### 在线安装

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


### 源码安装

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

### 升级

对 Python 来说，大版本之间有较大的差异，官方表示没有升级的方案，只能安装更高的版本，可以实现多版本共存。

## 概念与原理

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

### 虚拟环境

用户在编写应用程序的时候，通常会安装第三方的 Python 包，不同的应用程序可能对包有不同的要求，而特定的包可能会依赖其他的 Python 包，这种多版本和复杂依赖的情况下，很有可能会导致包冲突。  

虚拟环境就是为每一个用户的应用程序创建一个单独的 Python 隔离环境，用户所安装的第三方包会安装到虚拟隔离环境的位置，从而避免冲突。

**创建**

Python3.6 之后，默认提供了虚拟环境模块 [venv](https://docs.python.org/zh-cn/3/tutorial/venv.html)，只需要运行如下命令，即可创建虚拟环境。
```
python3 -m venv myapp
```
下图是创建的隔离环境目录，可见 venv 帮助我们创建了完整的 Python 所需的文件系统。  
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/python/python-venv001-websoft9.png)

**激活**

通过 source 命令，激活虚拟环境:

```
source myapp/bin/activate
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

### Gunicorn

## 问题解答

#### 如何找到 Python 资源？

* [Awesome Python](https://github.com/vinta/awesome-python)
* [Python3 菜鸟教程](https://www.runoob.com/python3/python3-tutorial.html)
* [Django 菜鸟教程](https://www.runoob.com/django/django-tutorial.html)

#### 运行环境是否支持多个 Python 版本？

除了操作系统自带的 Python2 之外，默认安装了 Python3.x 中的版本之一。  
用户可以自由安装更多的 Python3.x 版本，然后使用虚拟隔离环境，可以方便的安装应用而互不影响。

#### `python` 命令为何显示的版本是 2.7？

部分云平台默认已经安装 Python2，且设置为默认版本。

#### Python 默认字符编码是什么？

For python2.x, default encoding is ASCII   
For python3.x, default encoding is UTF-8  

#### Python 包是否可以被编译成二进制文件？

可以。建议使用 pyinstaller 或 cpython 这两种工具之一

#### Python 有哪些解释器？

| **Implementation** | **Virtual Machine**        | **Compatible Language** |
| ------------------ | -------------------------- | --------------------------- |
| [CPython](http://www.python.org/) (default)  | CPython VM                 | C                           |
| [Jython](https://www.jython.org/)             | JVM                        | Java                        |
| [IronPython](http://ironpython.net/)         | CLR                        | C#                          |
| Brython            | Javascript engine(e.g. V8) | JavaScript                  |
| RubyPython         | Ruby VM                    | Ruby                        |
| [PyPy](http://pypy.org)               | PyPy Executable            | JIT                         |
| [PythonNet](http://pythonnet.github.io/)          | PythonNet Executable            | .NET                         |

> 其中 CPython 是官方默认的解释器。

#### Python 解释器是如何工作的？

In a CPython interpreter, bytecode is fed to PVM (Python Virtual Machine) which is responsible for running your code.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/python/python-interpreter-websoft9.png)  

#### Python 有那些编译器？

* [CPython](http://www.python.org/) is the reference implementation of Python, written in C. 
* [PyPy](http://pypy.org/) is a Python interpreter implemented in a restricted statically-typed subset of the Python language called RPython. 
* [Jython](http://www.jython.org/) is a Python implementation that compiles Python code to Java bytecode which is then executed by the JVM (Java Virtual Machine). 
* [IronPython](http://ironpython.net/) is an implementation of Python for the .NET framework. 
* [Python for .NET](http://pythonnet.github.io/) is a package which provides near seamless integration of a natively installed Python installation with the .NET Common Language Runtime (CLR).

#### 什么是 ".egg" file？
Python Eggs are a way of bundling additional information with a Python project, that allows the project's dependencies to be checked and satisfied at runtime, as well as allowing projects to provide plugins for other projects.

#### 什么是 virtualenv？
virtualenv is a tool to create isolated Python environments. virtualenv homepage and documentation. [http://www.virtualenv.org/en/latest/](http://www.virtualenv.org/en/latest/)

#### Python 多版本如何安装网站？

可以，创建隔离环境的时候指定具体版本，例如：

```
python3.8 -m venv --system-site-packages "/data/wwwroot/yoursite1"
```

#### 为什么需要创建隔离环境？

避免不同的应用对同一个 Python 软件包有不同的版本冲突，隔离环境完美解决此问题

#### 一个 django 环境支持多个 django 项目？

可以