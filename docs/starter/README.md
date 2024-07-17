import DocCardList from '@theme/DocCardList';
import {useCurrentSidebarCategory} from '@docusaurus/theme-common';


# 快速入门

## 快速了解

在正式使用 Websoft9 部署应用之前，先在此明确几个重要概念：  

- **Websoft9 控制台**：Websoft9 控制台是一个 Web 界面。用户通过它可以方便地一键部署应用、自动化管理和维护应用。

- **应用与容器**：在 Websoft9 托管平台中，"应用" 是指可以在平台上部署和运行的各种软件程序或服务。这些应用可以涵盖广泛的功能和用途。从技术上视角，每个应用由一个或多个容器组成。  

- **应用与服务器**：在 Websoft9 托管平台中，应用最终部署在服务器（虚拟机）上。服务器上需部署 Docker，方可运行应用。  

然后，开始登陆 Websoft9 控制台，部署所需的应用。

## 部署应用

<DocCardList items={useCurrentSidebarCategory().items}/>


