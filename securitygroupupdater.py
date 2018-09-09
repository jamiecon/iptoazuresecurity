"""Updates a rule in an Azure security group with a new IP address."""
import azure.mgmt.network
from azure.common.credentials import ServicePrincipalCredentials

class SecurityGroupUpdater(object):
    """Uses the Azure API to update a security group rule with a new IP.
       Docs: https://docs.microsoft.com/en-gb/python/api/azure-mgmt-network/azure.mgmt.network.networkmanagementclient?view=azure-python
    """
    def __init__(self, subscription_id, resource_group, client_id, secret, tenant):
        self.resource_group = resource_group
        self.credentials = ServicePrincipalCredentials(
            client_id=client_id,
            secret=secret,
            tenant=tenant
        )
        self.client = azure.mgmt.network.NetworkManagementClient(self.credentials, subscription_id)

    def update(self, security_groups, rule_name, ip_address):
        """Updates the rule in the security groups with the specified IP address."""
        security_group_names = security_groups.split(",")

        for security_group in security_group_names:
            sec_group = self.client.network_security_groups.get(self.resource_group, security_group)
            for rule in sec_group.security_rules:
                if rule.name == rule_name:
                    rule.source_address_prefix = ip_address

            self.client.network_security_groups.create_or_update(
                self.resource_group,
                sec_group.name,
                sec_group)

        return True
