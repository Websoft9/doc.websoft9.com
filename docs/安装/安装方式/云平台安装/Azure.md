# Azure

Websoft9 已经在 Azure Marketplace 上提供了多款镜像（**Azure的映像就是镜像**），覆盖常用的云场景，满足各种企业的需求。

>  是不是想了解有哪些镜像呢？点击 [此处](https://azuremarketplace.microsoft.com/en-us/marketplace/apps?page=1&search=websoft9) 查看 Websoft9 在 Azure 上发布的所有镜像。

那么如何在 Azure 上使用这些镜像呢？有三种方法：

## Marketplace部署

1. 访问 [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps) 网站

2. 搜索关键字"websoft9"，网站会列出所有相关的镜像
   ![搜索Websoft9镜像](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-mkss-websoft9.png)

3. 点击您所需的产品，进入产品详情页后点击"GET IT NOW"按钮
   ![安装镜像](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-rs-websoft9.png)

4. 点击“创建”按钮，开始创建与镜像配套的虚拟机
   ![创建虚拟机](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-imagecreate-websoft9.png)

5. 在虚拟机的映像信息栏中，你会看到已经显示的你选择的镜像
   ![选择镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-imagevm-websoft9.png)

6. 虚拟机创建完成后，镜像会作为虚拟机的系统盘启动，即镜像自动部署到虚拟机了



## Portal部署

1. 登录到Azure后台门户（Portal），点击“创建资源”，等同于通过后台进入Marketplace

2. 搜索关键字“websoft9”，列出所有相关镜像
   ![Azure Portal 搜索镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-portalmk-websoft9.png)

3. 点击你所需的产品，开始订阅镜像



## VM部署

1. 登录到Azure后台门户（Portal），点击“虚拟机”，
   ![创建虚拟机](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-vm-websoft9.png)

2. 进入虚拟机管理项，点击“添加”，即开始创建一个新的虚拟机
   ![创建虚拟机](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-addvm-websoft9.png)

3. 在映像一栏，点击“浏览所有公用和专用映像”，然后搜索关键件词“websoft9”，列出相关镜像
   ![选择 Websoft9 镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-vmimage-websoft9.png)

4. 选择一个你所需的镜像，开始部署


除了镜像订阅部署之外，你还可以通过我们发布到 [Github 上 自动化部署脚本](https://github.com/websoft9)，来实现自动部署。