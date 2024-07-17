---
sidebar_position: 1.0
slug: /runtime/java
---

# For Java App

Websoft9 App Runtime for Java covers the entire Java ecosystem including JDK, Jetty, Tomcat, Tomee, maven, and more.

## Configuration options

- JDK runtime root path: */usr/src/app*
- Jetty runtime root path: *var/lib/jetty/webapps*
- Tomcat runtime root path: */usr/local/tomcat*
- Tomee runtime root path: */usr/local/tomee*
- [CLI](https://docs.oracle.com/javase/10/tools/tools-and-command-reference.htm): java, javac, jar, jdeprscan
- Package management: maven, gradle

## Deploy a Java application{#deploy}

Refer to: [App Runtime tutorials](../runtime#quick)

## Manage runtime{#administrator}

- **Install package tools**: Refer to [Install maven, gradle at JDK runtime](https://websoft9.github.io/docker-library/apps/openjdk/src/cmd.sh)

## Troubleshoot

### Which Java runtime should I use?

The Java open source community have multiple JDK branches and a variety of distinctive application servers and middleware.   

The Websoft9 Java runtime made it possible for users to choose from a wide range of suitable options.   

Below is a list of recommended choices that are best suited for real-world scenarios. 

- If you are running a war package that includes a web server, choose **OpenJDK**.
- If you are running a war package that does not include a web server, then choose **Jetty**, **Tomcat**, or **Tomee**.
- If you're just building and packaging, choose **Maven**.


### Tomcat 404 error?

**Description**: Access URL 404 error when running Tomcat runtime     

**Reason**: There not have application for Tomcat runtime  

**Solution**: Deploy your Java package

### war package extracted failed at Jetty?

**Description**: I can not find the extracted files at root directory of Jetty runtime   

**Reason**: The extracted files is not at root directory  