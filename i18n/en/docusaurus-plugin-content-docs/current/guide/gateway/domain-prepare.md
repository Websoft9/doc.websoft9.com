---
sidebar_position: 0.1
slug: /domain-prepare
---

# Prepare domain name

A domain is a unique address used to identify a website on the internet. Domains make it easier for users to access websites without needing to remember numerical IP addresses. 

There are five steps associated with domain names, of which registration (purchase), certification, and filing are business processes; resolution and binding are technical uses of the steps.     

## Prepare domain{#prepare-domain}

### Register your domain{#domainreg}

Subscribe to the desired domain name at the domain name service provider, usually on a yearly basis.  

### Authenticate domain ownership{#domainauth}

Provide your personal or company's legal identity documents for the domain name owner's real name authentication.

### Filing domain (optional){#domainbei}

Some countries require that filing domains comply with their own laws. For example: **ICP filing** in China.  

If you have **ICP filing** problem, you can get [support from Websoft9](./helpdesk)

## Use domain{#use-domain}

Using a domain name involves two sequential operations: resolution and binding.

### Resolve domain{#domainresolve}

Resolving a domain refers to the process of translating a human-readable domain name (such as example.com) into an IP address (such as 192.0.2.1) that computers use to identify each other on the network.   

This process is handled by the Domain Name System (DNS) and management by Domain provider console.    


### Bind domain{#domainbind}

Domain binding links different domains to specific applications on the same server via a HTTP Server.  

User can [bind domain](./domain-set) by [Proxy Hosts](./gateway-proxy) of Websoft9 Gateway.   

## FAQs{#faq}

#### Domain vs subdomain?

- `example.com` is domain
- `www.example.com` is subdomain

#### What is wildcard of domain?{#wildcard}

A wildcard is a domain name that includes a wildcard character (usually an asterisk *) to represent multiple subdomains. This allows a single domain name to match multiple subdomains without having to specify each one individually.   

Below is sample for domain `abc.com`,  it show what is wildcard of domain:  

| Record type | Record | Record value (IP) | The result of domain name resolution                                                         |
| -------- | -------------------- | ------------------- | ------------------------------------------------------------ |
| A        | *                    | 47.92.175.172       | Ending in `abc.com` are available, like `n1.abc.com` |
| A        | *.test               | 47.92.175.172       | Ending in `test.abc.com` are available, like `n1.test.abc.com`|
| A        | *.test.web           | 47.92.175.172       | Ending in `test.web.abc.com` are available, like `n1.test.web.abc.com`|