# This script was used as a proof of concept as a final lab in a python class. 
# Currently working on trying to get the program to read from Ultimate-Hosts-Blacklist DNS server rather then writing to a file localy


'''
script: Phishing-Detector
action: This script is used to detect phishing URLs/Ip addresses using a list of known and updated phishing URLs and IP addresses.
version: 0.2
date  :05/08/2025
author:Outofregs
'''

import os
import requests

# List of known phishing URLs and IP addresses (raw content URLs)
url_list = [
    'https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt',
    'https://raw.githubusercontent.com/Ultimate-Hosts-Blacklist/Ultimate.Hosts.Blacklist/refs/heads/master/ips/ips0.list',
    'https://raw.githubusercontent.com/Ultimate-Hosts-Blacklist/Ultimate.Hosts.Blacklist/refs/heads/master/domains/domains1.list',
    'https://raw.githubusercontent.com/Ultimate-Hosts-Blacklist/Ultimate.Hosts.Blacklist/refs/heads/master/domains/domains2.list',
    'https://raw.githubusercontent.com/Ultimate-Hosts-Blacklist/Ultimate.Hosts.Blacklist/refs/heads/master/domains/domains3.list',
    'https://raw.githubusercontent.com/Ultimate-Hosts-Blacklist/Ultimate.Hosts.Blacklist/refs/heads/master/domains/domains4.list',
    'https://raw.githubusercontent.com/Ultimate-Hosts-Blacklist/Ultimate.Hosts.Blacklist/refs/heads/master/domains/domains5.list',
    ]

# Input suspected URL or IP address
suspected_url = input("Enter the suspected URL or IP address: ").strip()

def download_blacklist(urls):
    """Download blacklists from the given URLs and save them to a file."""
    blacklist = set()
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                blacklist.update(response.text.splitlines())
            else:
                print(f"Failed to download blacklist from {url}. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error downloading blacklist from {url}: {e}")
    # Save the combined blacklist to a file
    with open('Blacklist.txt', 'w') as f:
        f.write('\n'.join(blacklist))
    return blacklist

def check_url(blacklist, suspected_url):
    """Check if the suspected URL or IP address is in the blacklist."""
    if suspected_url in blacklist:
        print(f"{suspected_url} is a known phishing URL or IP address.")
    else:
        print(f"{suspected_url} is not a known phishing URL or IP address.")

def main():
    """Main function to download the blacklist and check the suspected URL."""
    # Download the blacklist
    blacklist = download_blacklist(url_list)
    # Check the suspected URL
    check_url(blacklist, suspected_url)

if __name__ == "__main__":
    main()
