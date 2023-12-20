---
sidebar_position: 1
slug: /java
---

# Guide

This charter include JDK and Java application Server: Tomcat, Jetty

## Tutorial

### Use Maven{#maven}

A sample to use Maven

```
mvn archetype:generate -DgroupId=com.companyname.automobile -DartifactId=trucks -DarchetypeArtifactId=maven-archetype-webapp  -DinteractiveMode=false
```

### Web Framework{#framework}

### Change JDK version{#changeversion}

## Troubleshoot{#troubleshoot}

## Parameters

### Path{#path}

Java installation directory:  */data/java*    
Java logs directory:  */data/logs/java*    

Tomcat install directory: */usr/local/tomcat*    
Tomcat configuration file: */usr/local/tomcat/conf/server.xml*     
Tomcat logs: */var/log/tomcat*  

### CLI{#cmd}

These tools from docs: [Tools and Commands Reference](https://docs.oracle.com/javase/10/tools/tools-and-command-reference.htm)  

- **[javac](https://docs.oracle.com/javase/10/tools/javac.htm#GUID-AEEC9F07-CB49-4E96-8BC7-BCC2C7F725C9)**: You can use the `javac` tool and its options to read Java class and interface definitions and compile them into bytecode and class files.
- **[javap](https://docs.oracle.com/javase/10/tools/javap.htm#GUID-BE20562C-912A-4F91-85CF-24909F212D7F)**: You use the `javap` command to disassemble one or more class files.
- **[javadoc](https://docs.oracle.com/javase/10/tools/javadoc.htm)**: You use the `javadoc` tool and its options to generate HTML pages of API documentation from Java source files.
- **[java](https://docs.oracle.com/javase/10/tools/java.htm#GUID-3B1CE181-CD30-4178-9602-230B800D4FAE)**: You can use the `java` command to launch a Java application.
- **[appletviewer](https://docs.oracle.com/javase/10/tools/appletviewer.htm#GUID-43CF0B10-0BE3-48C6-B289-FD77952D4926)**: You use the `appletviewer` command to launch the AppletViewer and run applets outside of a web browser.
- **[jar](https://docs.oracle.com/javase/10/tools/jar.htm#GUID-51C11B76-D9F6-4BC2-A805-3C847E857867)**: You can use the `jar` command to create an archive for classes and resources, and to manipulate or restore individual classes or resources from an archive.
- **[jlink](https://docs.oracle.com/javase/10/tools/jlink.htm)**: You can use the `jlink` tool to assemble and optimize a set of modules and their dependencies into a custom runtime image.
- **[jmod](https://docs.oracle.com/javase/10/tools/jmod.htm)**: You use the `jmod` tool to create JMOD files and list the content of existing JMOD files.
- **[jdeps](https://docs.oracle.com/javase/10/tools/jdeps.htm#GUID-A543FEBE-908A-49BF-996C-39499367ADB4)**: You use the `jdeps` command to launch the Java class dependency analyzer.
- **[jdeprscan](https://docs.oracle.com/javase/10/tools/jdeprscan.htm)**: You use the `jdeprscan` tool as a static analysis tool that scans a jar file (or some other aggregation of class files) for uses of deprecated API elements.

### Version{#version}

```
java -v
```

### Service{#service}

```
# Docker
sudo docker start jdk
sudo docker stop jdk
sudo docker restart jdk
sudo docker stats jdk
```