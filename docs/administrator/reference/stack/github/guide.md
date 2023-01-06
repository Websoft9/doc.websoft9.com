---
sidebar_position: 1
slug: /github
---

# 指南

## 场景

### 创建 Github 模板项目

可以将一个普通Github项目设置为模板项目，然后基于这个模板项目创建新的项目，具体如下：

1. 选择一个已有 repository，点击：【settings】，然后勾选【Template repository 】
2. 创建成功后，在项目的标题右侧会有"Template"的标记
3. 点击“Use this template”按钮，基于模板项目创建新项目

### Github 分支管理

打开项目，输入新的分支名称，回车后即可基于默认分支创建一个新的分支

### Github 看板中勾选模板

```
:sparkles: **Welcome to GitHub Projects** :sparkles:
We're so excited that you've decided to create a new project! Now that you're here, let's make sure you know how to get the most out of GitHub Projects.
- [x] Create a new project
- [x] Give your project a name
- [ ] Press the <kbd>?</kbd> key to see available keyboard shortcuts
- [ ] Add a new column
- [ ] Drag and drop this card to the new column
- [ ] Search for and add issues or PRs to your project
- [ ] Manage automation on columns
- [ ] [Archive a card](https://docs.github.com/articles/archiving-cards-on-a-project-board/) or archive all cards in a column
```

### Github Action 范例

参考核心项目：[docker-library](https://github.com/Websoft9/docker-library/tree/main/.github/workflows)、[websoft9.com](https://github.com/Websoft9/www.websoft9.com/tree/main/.github/workflows)

### Github 成员管理

Github 支持组织和 repository 两种级别的邀请成员方式L：

* Repository 级：【Settings】>【Collaborators and teams】>【Manage access】
* 组织级：进入组织首页后，通过【people】标签进行管理



## 故障排除{#troubleshoot}

#### Git push 时，报错：refusing to allow a Personal Access Token...？

错误信息：[remote rejected] main -> main (refusing to allow a Personal Access Token to create or update workflow `.github/workflows/ci.yml` without `workflow` scope)  
解决方案：找到所采用的 [Personal access tokens](https://github.com/settings/tokens)，【Select scopes】中勾选【workflow】  

#### 合并 pull request 冲突？

冲突产生时，会弹出手动合并命令。只需在 git pull 命令后面加上 --allow-unrelated-histories

```
git pull https://github.com/MariaDB/mariadb-docker.git master --allow-unrelated-histories
```