---
sidebar_position: 0.1
slug: /login-console
---

# Login Websoft9 Console

After installing the Websoft9 server, the next step is to login to the Websoft9 Console.

## Preparation

Before using the application, you need to complete the following preparations:  

- Open the inbound ports in the server's security group:

   - Required ports: 80, 443, 22, 9000
   - Optional ports (for application access): 9001-9999

- Get the server's[account credentials](./credentials)(Websoft9 shares the account with the server)

## Login

Logging into Websoft9 does not require any additional special settings; you just need to access the corresponding server port from **your local browser**:    

1. Access via local browser: `http://server-public-IP:9000`, the Websoft9 login page
   ![Websoft9 Login page](./assets/websoft9-loginpage.png)

2. Input the server's [username and password](./credentials), after a successful login, you will be directed to the console overview page.  
 
   - username: The server's administrator account, it is recommended to use `root` for the first login. 
   - password: The server's administrator password.

   ![](./assets/websoft9-console-index.png)

3. Click on **App Store** to view all available application templates.
   ![](./assets/websoft9-appstore.png)

4. Click on **My Apps**to view the list of installed applications.
   ![](./assets/websoft9-myapps.png)

## Related Topics

- Binding Domains
- Managing Applications
- Databases
- Setting Up Application Access