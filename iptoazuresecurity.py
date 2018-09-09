"""Obtains the computer's public IP address and updates an Azure Security Group with the new
   details.
   https://docs.microsoft.com/en-us/python/api/overview/azure/dns?view=azure-python
"""
import json

import securitygroupupdater
import publicip

CONFIGURATION_FILE = "config.json"

print("Azure Security Group Updater")

with open(CONFIGURATION_FILE) as json_data_file:
    config = json.load(json_data_file)


config_output = """\nSubscription ID: {0}
Resource Group: {1}
Client ID: {2}
Client Secret: {3}
Tenant: {4}

Security Groups: {5}
Rule Name: {6}""".format(
    config["azure_subscription_id"],
    config["azure_resource_group"],
    config["azure_client_id"],
    config["azure_client_secret"],
    config["azure_tenant"],
    config["security_groups"],
    config["rule_name"]
)

print(config_output)

try:
    ip_address = publicip.PublicIP.get_ip_address()
except:
    print("ERROR: Unable to get public IP address. Program terminated.")
    quit()

print("\nIP address: " + ip_address)

updater = securitygroupupdater.SecurityGroupUpdater(
    config["azure_subscription_id"],
    config["azure_resource_group"],
    config["azure_client_id"],
    config["azure_client_secret"],
    config["azure_tenant"]
    )

print("\nUpdating Security Groups...")

result = updater.update(config["security_groups"], config["rule_name"], ip_address)

if result:
    print("Success.")
else:
    print("Error.")
