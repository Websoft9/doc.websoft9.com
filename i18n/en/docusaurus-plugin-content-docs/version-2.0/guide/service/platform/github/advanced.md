---
sidebar_position: 2
slug: /github/advanced
---

# 进阶

Git 和 GitHub 是广泛使用的代码管理工具。

## 原理

### 配置

```
git config --global user.name "websoft9"
git config --global user.email "help@websoft9.com"
git config --global credential.helper store
git clone https://github.com/websoft9dev/role_init_password.git
```
经过以上配置，默认会在用户目录中生成：/root/.gitconfig 和  /root/.git-credentials 两个文件


### Github CLI

GitHub CLI 是用于在计算机上使用 GitHub 功能的命令行工具。可以将以下 GitHub 功能与 GitHub CLI 结合使用。

* 查看、创建、克隆和复刻仓库
* 创建、关闭和列出议题和拉取请求
* 审查、差异和合并拉取请求
* 创建、编辑、列出和查看 Gist


## 问题解答

#### 如何给 Github 项目体积？

本地运行 `git clone --depth=1`拉取项目，然后再 push 回远程。depth 数字越小，项目体积减少越多

#### 如何恢复误删的文件？

```
git status
git restore filename
```

#### Github 每次 push 都需要输入 token?

Github 不再支持账号和密码的方式来 push，而是采用新的 token 模式。下面是设置任何 repository 均有效的步骤：

1. [创建个人访问令牌 - GitHub Docs](https://docs.github.com/cn/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
2. 设置 Git 缓存策略
   ```
    #默认缓存15分钟 git config --global credential.helper cache
       #可以更改默认的密码缓存时限 git config --global credential.helper 'cache --timeout=3600000'
   ```
3. Push 操作时，输入你的用户名和token，即设置成功

如果 token 仅设置为 repository 有效，只需在 repository 目录下运行如下命令：
```
git remote set-url origin https://token@github.com/websoft9/ansible-mingdao
```

#### 如何在Github上插入小图标（表情）？

在 [emoji-cheat-sheet](https://www.webfx.com/tools/emoji-cheat-sheet)  找到图标，插入代码 :iconname: 即可