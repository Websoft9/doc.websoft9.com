---
title: MongoDB
slug: /mongodb
tags:
  - Document Database
  - Cloud Database
  - JASON
---

import Meta from './_include/mongodb.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. After completing the installation of MongoDB in the **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

2. Follow the installation wizard step by step

### CLI connection

1. Enter the MongoDB container and run the MongoDB Shell command
   ~~~
   $ mongosh admin -u root -p YOURPASSWORD
   MongoDB shell version v5.0.10
   connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
   ...
   ~~~

2. List the default databases and users
   ```
   # List all databases
   show dbs

   # Switch to the admin database and list all users.
   use admin
   show users
   ```

### Graphical Web 

Websoft9 provides a web-based application to access   [MongoDB Compass](./mongocompass#wizard) 

### Commands

The most commonly used MongoDB commands are listed below for you reference:  

#### Display, create and switch databases. 

```shell

> show dbs
admin     0.000GB
config    0.000GB
local     0.000GB

# Create the test database (if not exist)
> use test
switched to db test

# Display current database.
> db
test

# Display all users. 
> show users

# Insert data to database.
> db.test.insert({"name":"company"})
WriteResult({ "nInserted" : 1 })
```
#### Delete database.
```
> show dbs
admin     0.000GB
config    0.000GB
local     0.000GB
test      0.000GB
websoft9  0.000GB

> use test
switched to db test
> use test
> db.dropDatabase()
{ "dropped" : "test", "ok" : 1 }
> show dbs
admin     0.000GB
config    0.000GB
local     0.000GB
websoft9  0.000GB
```
#### Create administrator  account.

```
> mongo
> use admin
switched to db admin
> db.createUser( { user: "webs_admin", pwd: "websoft9", roles: ["userAdminAnyDatabase"] } )
Successfully added user: { "user" : "webs_admin", "roles" : [ "userAdminAnyDatabase" ] }


# Display accounts.
> show users
{
        "_id" : "admin.webs_admin",
        "user" : "webs_admin",
        "db" : "admin",
        "roles" : [
                {
                        "role" : "userAdminAnyDatabase",
                        "db" : "admin"
                }
        ],
        "mechanisms" : [
                "SCRAM-SHA-1",
                "SCRAM-SHA-256"
        ]
}
```
#### Change administrator password. 

  ```
  > db = db.getSiblingDB('admin')
  admin
  > db.changeUserPassword("root", "NEWPASSWORD")
  > exit
  ```

## Configuration options{#configs}

- [Configuration file](https://docs.mongodb.com/v4.0/reference/configuration-options/#conf-file) (mounted): */etc/mongod.conf*  

- Enable public access: Modify the `bindIp: 0.0.0.0` field in the configuration file

- Server command: `mongod`

- Client command: `mongo`

- Commands: `mongod` is the server-side management command for MongoDB, while `mongo` is the client used to access the MongoDB service

- No authentication access (√): refer to [Access Control](https://docs.mongodb.com/manual/tutorial/enable-authentication/) settings

- Default database admin: database users with global administrative privileges are stored in the admin database

## Administer{#administrator}

- **Shut down MongoDB access authentication**: From the Websoft9 console, select **My Apps > Compose > Go to Edit Repository > .env**, comment out the environment variable with the prefix  **MONGO_INITDB_**, and rebuild.

- **Forgot administrator password**: After disabling MongoDB access authentication, enter the container and run the reset command, then restore the password. 
   ```
   mongo
   > db = db.getSiblingDB('admin')
   admin
   > db.changeUserPassword(“root”, “NEWPASSWORD”)
   ```

- Backups: Use **mongodump** and **mongorestore** for MongoDB backup and recovery. For more details, refer to ([MongoDB Backup Methods](https://docs.mongodb.com/manual/core/backups/))
  ```
   # Backup
   mongodump --authenticationDatabase admin --username root --password PASSWORD -d DATABASE_NAME -h localhost

   # Recover
   mongorestore --authenticationDatabase admin --username root --password PASSWORD PATH_TO_BACKUP_FILE
  ```

## Troubleshooting{#troubleshooting}

#### MongoDB compass cannot connect?

Verify that connection parameters such as prefix port, bindIP, and account authentication meet the specified requirements.
