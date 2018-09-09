IP address to Azure Network Security Group
==========================================

This program gets the current machine's public IP address and updates the configured security group with the details.

Useful for people with frequently changing public IPs who need to SSH to Azure instances.

To build, run and distribute use _virtualenv_ and _pyinstaller_.

To run
------
```
cd iptoazuresecurity
virtualenv env
source env/bin/activate
pip install -r requirements.txt
pip install azure-mgmt-network
python iptoazuresecurity.py
```
