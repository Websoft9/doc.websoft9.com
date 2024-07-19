---
sidebar_position: 1.1
slug: /iaas-azure
---

# Azure

This chapter provides a quick guide for using Websoft9 on Azure.  

## Quick References

### Create VM{#create-vm}

You can create Azure VM by below methods

- Create VM by image
- Create VM by VHD

### DNS for VM{#ip-domain}

[Azure DNS alias](https://learn.microsoft.com/en-us/azure/dns/dns-alias) records are qualifications on a DNS record set. They can reference Azure VM from within your DNS zone.   

If you create VM, Azure created a DNS `your_alias.centralus.cloudapp.azure.com` for it.  

### Security Group{#security-group}

Azure Portal can set security group by: **VM console > Network > Network Settings**.  

And it support **Application Security Groups (ASG)** security policy.    

### Azure CLI

[Azure CLI](https://learn.microsoft.com/en-us/cli/azure/what-is-azure-cli) commands that may be used when hosting applications with Websoft9.  

- Get Websoft9 image information

    ```
    az vm image list --location westus -p vmlabinc1613642184700 --output table
    ```

- Create VM from Websoft9 image
  ```
  # docs: https://docs.microsoft.com/en-us/powershell/module/azurerm.compute/set-azurermvmplan?view=azurermps-6.13.0&viewFallbackFrom=azurermps-6.6.0
    az vm create -n akeneo-test -g networkwatcherrg --attach-os-disk akeneo-test_OsDisk_1_8a98e493bc144ffd8d68a62b8da35532  --os-type linux --location centralus  --plan-publisher Bitnami --plan-name '1-4' --plan-product Akeneo --image Bitnami:akeneo:1-4:3.2.1910031550
  ```


## Configure Options

- Azure Console connect VM (√): **VM console > Connect**

- VM Backup (√): [Azure Backup](https://azure.microsoft.com/en-us/products/backup/)

- Change the size of VM (√): **VM console > Availability + Scaling > Size**

- Redeploy VM (√): **VM console > Support > Redeploy**

- Default credential of VM: Create username and password or key pair by user

- Spot Virtual Machines (√)

- Replace VM image (×)

- VM username and password [requirements](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/faq)


## Related Azure docs

- [Enable root account password](./linux#enable)
- [Deploy Websoft9 at Azure](./install/azure)
- [Azure Virtual machines](https://learn.microsoft.com/en-us/azure/virtual-machines/)
- [Azure Blob](https://learn.microsoft.com/en-us/azure/storage/blobs/)
- [Azure Storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal)
- [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/what-is-azure-cli)


## Troubleshoot
