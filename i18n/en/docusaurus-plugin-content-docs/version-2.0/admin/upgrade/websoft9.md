---
sidebar_position: 1
slug: /upgrade-websoft9
---

# Upgrade Websoft9

## Upgrade Websoft9

The install script supports both **fresh install** and **upgrade**, and auto-detects the current environment. Back up your data before upgrading.

```
wget -O install.sh https://artifact.websoft9.com/websoft9/release/install.sh && sudo bash install.sh
```

> Upgrade does not affect deployed applications.

## Troubleshooting

#### Unable to access some features after upgrade?

**Description**: Cannot access Gateway or Repository interface at Websoft9 Console, showing network error
**Solution**: Clear your browser cache

Below is an example of clearing cache on Microsoft Edge: press F12 to enter browser developer mode

![](./assets/websoft9-edge-clearcache.png)


