---
sidebar_position: 2.1
slug: /url
---

# Manage base URL

When accessing web applications, it is common to encounter a setting called **base url** or **root url**. What is it exactly? What does it do? How is it set? This chapter will tell you all about it.

## Learn base URL

The base URL (or root URL) is the initial part of a URL that typically includes the protocol (such as HTTP or HTTPS) and the domain name (such as example.com). It serves as the starting point for constructing other URLs on the same website or web application. The base URL does not include any specific paths, parameters, or file names that come after the domain.

The base url is usually **hardcoded** in a configuration file of application, often used in content management systems (CMS) such as WordPress, Magento. 

Once your application have hardcoded base URL, it may have below features:  

- All internal links and resources are generated based on the preset base URL.
- Regardless of configured domains, they eventually redirect to the base URL.
- Any changes to the base URL require manual updates in configuration files or code.


## Replace base URL

Hardcoded base URLs offer stability but reduce flexibility for domain changes or server migrations.  

### Basic process

Changing the base URL is a serious and cautious task. Follow these steps:

- **Backup:** Before any changes, backup current configuration files and database.
- **Update:** Locate and update the base URL in configuration files, database, or code.
- **Test:** Thoroughly test the website to ensure all links and resources work.
- **Deploy:** Once confirmed, deploy the changes to the production environment.


### Replace URL at Websoft9 Console{#domain}

The Websoft9 Console simplifies base URL replacement for most applications by [changing the domain](./domain-set#appmanage).   

A few applications require manual changes to configure files, db, or code to replace base URL after changing the domain.









