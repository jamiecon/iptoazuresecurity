"""
   Gets the public IP address of the computer.
   IPify: https://www.ipify.org/
"""
import ipaddress
import requests

REQUEST_TIMEOUT_SECONDS = 20

class PublicIP:
    """Provides methods to get the computers's public IP address."""

    @staticmethod
    def get_ip_address():
        """Tries to get the computer's public IP."""
        try:
            request_output = requests.request(
                'GET',
                'https://api.ipify.org',
                timeout=REQUEST_TIMEOUT_SECONDS
            )
            ip_address = ipaddress.ip_address(request_output.text)
            public_ip = str(ip_address)
        except:
            raise requests.ConnectionError('Unable to get public IP')

        return public_ip
