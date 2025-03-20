---
sidebar_position: 1.1
slug: /brandwith-infra
---

# Plan bandwidth and traffic

Network bandwidth is important for the performance for hosting applications by Websoft9. Correctly estimating bandwidth requirements improve your quality of service and save costs.  

The key points related to network bandwidth:  

- **User Experience**: High bandwidth provides faster load times and smoother interactions.
- **Concurrency Support**: More bandwidth supports more concurrent users.
- **Transmission Efficiency**: Bandwidth affects upload and download speeds.
- **Search Engine Ranking**: Load speed impacts search engine rankings.

## Dimensions for calculating bandwidth

The dimensions for calculating bandwidth related to your application performance indicators: 

- **Number of users:** More users or concurrent users require more bandwidth.
- **User behavior:** Frequent large file downloads/uploads need more bandwidth.
- **Application type:** Streaming, gaming, file sharing need more bandwidth than static sites.
- **Data type:** Video and large media files consume more bandwidth than text/images.
- **Expected growth:** Anticipate user growth and service expansion in bandwidth planning.
- **Redundancy and peak capacity:** Reserve extra bandwidth for traffic spikes.

## Uncontrolled traffic

You needs to consider the negative impact of some unavailable or uncontrolled traffic performance and billing.  

- **Malicious traffic**: Traffic from cyber attacks like DDoS, potentially causing high costs.
- **Bot and crawler traffic**: Traffic from search engine crawlers and automated scripts, not real users.
- **Other invalid traffic**: Misconfigurations, fraudulent visits, repeated transmissions, unauthorized access, etc.

## Improve access from outside the bandwidth  

Improving application access speed is not limited to increasing the network bandwidth of the server. It also includes:  

- Use [CDN](./gateway-cdn)
- Use cache layer
- Intranet transfer between servers