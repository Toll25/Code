#!/usr/bin/env python3

import ipaddress
import threading
from icmplib import ping


def check_responsiveness(ipaddress):
    response = ping(str(ipaddress), 1)
    if response.is_alive:
        responsive.append(ipaddress)
    else:
        nonResponsive.append(ipaddress)


network = input("Enter a valid IPv4 Network (192.168.0.0/24): ")

network = ipaddress.ip_network(network)
responsive = []
nonResponsive = []
threads = []

for host in network.hosts():
    threads.append(threading.Thread(target=check_responsiveness, args=(host,)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


print("Responsive:")
for ip in responsive:
    print(ip)

print("Non-Responsive:")
for ip in nonResponsive:
    print(ip)
