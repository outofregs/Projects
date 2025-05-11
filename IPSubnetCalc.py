"""
Script: IP Subnet Calculator
Action: Takes a given IP address gives you the subnet mask, network address, broadcast address, and number of hosts in the subnet.
Author: Outofregs 
Date  : 05/01/2024 
"""

import ipaddress
import sys
import argparse
import matplotlib.pyplot as plt

# Input the IP address and CIDR notation
def get_ip_info(ip_str):
    try:
        # Parse the IP address and CIDR notation
        ip = ipaddress.ip_interface(ip_str)
        network = ip.network
        broadcast = network.broadcast_address
        num_hosts = network.num_addresses - 2  # Exclude network and broadcast addresses

        return {
            'IP Address': str(ip.ip),
            'Subnet Mask': str(network.netmask),
            'Network Address': str(network.network_address),
            'Broadcast Address': str(broadcast),
            'Number of Hosts': num_hosts,
            'CIDR Notation': str(network.prefixlen)
        }
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

# Display the results in a table format
def display_results(results):
    print("\nIP Address Information:")
    print("-" * 40)
    for key, value in results.items():
        print(f"{key}: {value}")
    print("-" * 40)

# Main execution block
if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="IP Subnet Calculator")
    parser.add_argument("ip", help="IP address with CIDR notation (e.g., 192.168.x.x/24)")
    args = parser.parse_args()

    # Get IP information and display results
    ip_InFo = get_ip_info(args.ip)
    display_results(ip_InFo)
