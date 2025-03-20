---
sidebar_position: 4
slug: /troubleshoot/tree
---

# Fault Tree Analysis

[Fault tree analysis(FTA)](https://www.ibm.com/topics/fault-tree-analysis) is a deductive, top-down approach to determining the cause of a specific undesired event within a complex system. It involves breaking down the root cause of a failure into its contributing factors and representing it through a graphical model called a fault tree, which helps managers and engineers identify potential failure modes—and the probability of each failure mode—for safety and reliability analyses.  

Basic events for Websoft9 issues includes: **Computing resource limited, Connection loose, Stack failure**  


#### Computing resource limited

Resource limited refer to insufficient computing resources: overloaded CUPs, insufficient memory, full disk space, insufficient bandwidth, mutual process exclusion, full ports, and so on.

You can use below commands to check them:

```
# check memory
free

# check disk
df -hl 

# check process and CPU
top

# check ports
netstat -tunlp
```

#### Poor connection between stacks

Poor connectivity includes network failures, insufficient access authority, account errors, blacklisting issues, incorrect connection objects, etc.  

Common connection scenarios:

- Application connect to database
- Client connect to Server
- Browser connect to appplication

You can use below commands to check them:

```
# check port open or close for Internet
nmap -p 22 47.92.175.174
nmap -p 80 47.92.175.174

# check local ports
nmap -sT 127.0.0.1
nmap -sU 127.0.0.1

# DNS dig
dig websoft9.com

# ping
ping websoft9.com

# trace route
traceroute websoft9.com

# Telnet
telnet websoft9.com 9090

# Ping and traceroute
mtr websoft9.com
```

#### Stack failure

Stack failure can lead to failure of other stacks that depend on it.    

Stack failure include: inoperability, damage, failure to start, unscheduled stop, lockout, commercial factors (unpaid bills), security incidents, etc.  