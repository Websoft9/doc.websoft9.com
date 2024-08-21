---
sidebar_position: 2
slug: /security-code-injection
---

# Dealing with Code Injection

Code injection is a type of security vulnerability that occurs when an attacker is able to introduce malicious code into a program by exploiting insufficient input validation. This malicious code is then executed by the host system, potentially leading to unauthorized actions, data breaches, or system compromises.  

## Code injection type

Code injection can take many forms, including but not limited to:  

- **SQL Injection**: This involves inserting or "injecting" SQL code into a query to manipulate the database.
- **Command Injection**: Attacker execute arbitrary commands on the host operating system via a vulnerable application.
- **Script Injection**: This includes Cross-Site Scripting (XSS), injecting malicious scripts into web pages viewed by users.
- **Template Injection**: This occurs when an attacker injects code into a server-side template, executed by the server.


## Diagnosis Code injection

Although have different types of Code injections, the standard process for diagnosing a Code injection is as follows:  

1. Use online check tool [sitecheck.sucuri.net](https://sitecheck.sucuri.net/) to check your webiste

2. Use [ClamAV](./clamav) for a total [vulnerability scanning](./admin/security/security-scan)

3. Use [Datalog](https://www.datadoghq.com/) or [Cloudcare](https://www.cloudcare.cn/) for monitoring your website

3. More manual diagnostic and analysis commands
   ```
   # Retrieve specific documents
   grep -r search_term <directory>
   
   # Check process
   ps -ef
   top
   pstree
   
   # List all system account
   cat /etc/passwd
   
   # Check login logs
   lastb
   last
   
   # Check SSH tunnel
   ps -ef | grep -v grep| grep "sshd: root@notty"
   
   # Check SSH connection
   netstat -antup | grep ssh
   ps auxf | grep ssh
   ps auxf | grep notty
   
   # Check crontab
   crontab  -l
   ```
4. Synthesize test results to make accurate judgments

## Samples

### Sample1：Solve WordPress code injection

Please refer to below steps to diagnose and troubleshoot WordPress code injection:     

1. Use [sitecheck.sucuri.net](https://sitecheck.sucuri.net) to check your site

2. Login to WordPress console, and install scan plugin [Wordfence Scan Enabled](https://wordpress.org/plugins/wordfence/) to check your site
   ![](./assets/wordpress-wordfence-websoft9.png)
   
3. The results marked with **Critical** are processed manually one by one.