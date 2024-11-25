terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.0"
    }
  }
}

provider "azurerm" {
  features {}
  client_id       = var.client_id
  client_secret   = var.client_secret
  subscription_id = var.subscription_id
  tenant_id       = var.tenant_id
}

variable "client_id" {
  description = "The Client ID for Azure"
}

variable "client_secret" {
  description = "The Client Secret for Azure"
}

variable "subscription_id" {
  description = "The Subscription ID for Azure"
}

variable "tenant_id" {
  description = "The Tenant ID for Azure"
}

variable "ssh_public_key" {
  description = "The SSH public key to access the virtual machine"
}

resource "azurerm_resource_group" "rg" {
  name     = "myResourceGroup"
  location = "North Europe"
}

resource "azurerm_virtual_network" "vnet" {
  name                = "himitsuVnet"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}

resource "azurerm_subnet" "subnet" {
  name                 = "himitsuSubnet"
  address_prefixes     = ["10.0.1.0/24"]
  virtual_network_name = azurerm_virtual_network.vnet.name
  resource_group_name  = azurerm_resource_group.rg.name
}

resource "azurerm_network_interface" "nic" {
  name                = "himitsuNic"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.subnet.id
    private_ip_address_allocation = "Dynamic"
  }
}

resource "azurerm_virtual_machine" "vm" {
  name                  = "HimitsuVM"
  location              = azurerm_resource_group.rg.location
  resource_group_name   = azurerm_resource_group.rg.name
  network_interface_ids = [azurerm_network_interface.nic.id]
  vm_size               = "Standard_DS1_v2"

  storage_os_disk {
    name              = "myOsDisk"
    create_option     = "FromImage"
    managed_disk_type = "Standard_LRS"
  }

  os_profile {
    computer_name  = "HimitsuVM"
    admin_username = "azureuser"
    custom_data = base64encode("echo 'Welcome to HimitsuVM' > /etc/motd")
  }

  os_profile_linux_config {
    disable_password_authentication = true
    ssh_keys {
      path     = "/home/azureuser/.ssh/authorized_keys"
      key_data = var.ssh_public_key
    }
  }

  storage_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "18.04.202302100"
  }
}

