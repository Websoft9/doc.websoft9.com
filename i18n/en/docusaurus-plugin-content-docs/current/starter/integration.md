---
sidebar_position: 1.3
slug: /apps-integration
---

# Integrate multiple applications

In cloud-native architecture, isolated apps limit data sharing and collaboration. Websoft9 applications hosting platform uses unified standards for deployment and integration.  

## Plan integration use cases

Architects need to clearly define integration goals and determine the type of integration required.

Below is the most use cases for integration:  

- **Process Integration**: Integrating from the perspective of application workflow changes. For example, an action in Application A triggers a specific operation in Application B to collaboratively complete a task.
- **Data Integration**: Ensuring data consistency and availability through synchronization between applications.
- **UI Integration**: Merging interfaces from multiple applications into a unified interface to enhance user experience.
- **Dependency Integration**: Dependencies between applications, such as a website analytics tool relying on a CMS.

Once the kown what integration need, the next step is to create usable connections between applications.  


## Connection network for application

The network method of connection needs to be clarified as soon as possible:  

- **Intranet connection**: Connection through a local network to ensure security and efficiency.
- **Public network connection**: Public access via the Internet for application that require extensive access.

### Intranet{#intranet}

The containers for all applications share the same network **websoft9** with **container_name** as the DNS.   

- Container connect container as **container_name**.   
  Get container_name from **Websoft9 Console > My Apps > Your application > Containers**  


- Container connect host machine as virtual bridge **docker0** (Typically address is: 172.17.0.1)   
  Get docker0 address from **Websoft9 Console > Containers > Network > bridge**
 

### Public network{#internet}

Websoft9 offers tools to manage Internet access for web applications needing connectivity.  

For more information, see the related chapter:   

- [Access application and set network](./app-network)
- [Configure domain and security access for application](./gateway)


## Integrate application by iPaaS

In today's enterprise environments, where the number of applications continues to grow, it is clear that manually integrating these applications is bound to be time-consuming, labor-intensive, and error-prone.

Automation have clear advantages and have evolved into standardized integration platforms as a service ([iPaaS](https://www.ibm.com/cn-zh/topics/ipaas)).   

Typical tools include


- Open Source

    * [n8n](./n8n)

    * [Huginn](./huginn)

    * [Activepieces](https://www.activepieces.com/)

- SaaS

    * [Zapier](https://zapier.com/) 

    * [Unito ](https://unito.io/)

    * [Automate.io](https://automate.io/)

    * [Tray Platform](https://tray.io/)

    * [IFTTT](https://ifttt.com/)

