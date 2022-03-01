# Ruby

Ruby，一种简单快捷的面向对象（面向对象程序设计）脚本语言，在20世纪90年代由日本人松本行弘(Yukihiro Matsumoto)开发，遵守GPL协议和Ruby License。它的灵感与特性来自于 Perl、Smalltalk、Eiffel、Ada以及 Lisp 语言。由 Ruby 语言本身还发展出了JRuby（Java平台）、IronRuby（.NET平台）等其他平台的 Ruby 语言替代品。Ruby的作者于1993年2月24日开始编写Ruby，直至1995年12月才正式公开发布于fj（新闻组）。因为Perl发音与6月诞生石pearl（珍珠）相同，因此Ruby以7月诞生石ruby（红宝石）命名。

## 安装

### 在线安装

如果您的计算机已经连接到 Internet，那么最简单安装 Ruby 的方式是使用 **yum** 或 **apt-get**。在命令提示符中输入以下的命令，即可在您的计算机上安装 Ruby。

```
$  sudo yum install ruby    # CentOS, Fedora, 或 RHEL 系统

或

sudo apt-get install ruby-full # Debian 或 Ubuntu 系统
```

如果你是苹果系统，可以使用 **brew** 命令安装：

```
$ brew install ruby
```

### 源码安装

- 下载最新版的 Ruby 压缩文件。[请点击这里下载](http://www.ruby-lang.org/en/downloads/)。
- 下载 Ruby 之后，解压到新创建的目录下：

```
$ tar -xvzf ruby-2.2.3.tgz    
$ cd ruby-2.2.3
```

- 现在，配置并编译源代码，如下所示：

```
$ ./configure
$ make
$ sudo make install
```

- 安装后，通过在命令行中输入以下命令来确保一切工作正常：

```
$ruby -v
ruby 2.2.3……
```

## 安装扩展

## Gemfile

Gemfile.local

Gemfile 

优先级，使用方法

## 包管理

Gem,Bundler

