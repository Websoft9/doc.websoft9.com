---
sidebar_position: 3
slug: /runtime/nodejs
tags:
  - Node.js
  - Node
  - Runtime
---

# Deploy Node app

## Deploy Your Node.js application

Deploying a website (application) on the Node.js environment is to add a virtual host.

From a global perspective, only three steps are needed: **Upload website code** + **Run NPM command** + [**Virtual machine host configuration file**](../runtime#path)** Add server in {} configuration section**

> server{} is also called virtual host configuration section, each website must correspond to a unique server{} in default.conf.

### Delete sample program

This deployment scheme has already installed and started the [Express framework](https://www.expressjs.com.cn/) by default, let's delete it first:

1. Run `npm list` to query running Node.js programs
   ```
   ┌────┬────────────────────┬──────────┬──────┬───────────┬──────────┬──────────┐
   │ id │ name               │ mode     │ ↺    │ status    │ cpu      │ memory   │
   ├────┼────────────────────┼──────────┼──────┼───────────┼──────────┼──────────┤
   │ 0  │ www                │ fork     │ 0    │ online    │ 0.1%     │ 48.7mb   │
   ```
2. Delete the process of pm2 sample program
   ```
   pm2 delete 0
   ```   
3. Save the modification
   ```
   pm2 save
   ```
4. Delete the folder of program
   ```
   rm -rf /data/wwwroot/express.example.com
   ```
5. delete the PM2 init script
   ```
   //delete the PM2 init script
   pm2 unstartup systemd

   //delete the have been saved PM2 file of process
   rm -rf /root/.pm2
   ```


### Install Express

1. Create a directory
   ```
   mkdir myapp
   cd myapp
   ```
2. Install Express Application Framework
   ···
   npx express-generator
   ···
3. Install dependencies
   ```
   npm install
   ```
4. Start the application and access the application via: *http://server public IP:3000*
   ```
   DEBUG=myapp:* npm start
   ```

> You can also use pm2 to manage applications

## Maintain Node.js Environment

Refer to：[《Node.js Guide》](../nodejs) and [《Node.js Advanced](../nodejs/advanced) 



