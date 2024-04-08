#!/usr/bin/enc python

import scapy.all as scapy
import argparse

def get_arguments():
    parser = optparse.ArgumentParser()
    parser.add_argument("-t", "--target" , dest = "target", help="Target IP / IP range.")
    options = parser.parse_args()
    return options

def scan(ip):
	#scapy.arping(ip)  - quick way to do it 
	#manual configuration 
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_broadcast_request = broadcast/arp_request
	answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose = False)[0]
    
    clients_list = []
    for element in answered_list:
       clients_dict = {"ip" : element[1].psrc , "mac" : element[1].hwsrc}
       clients_list.append(clients_dict)
    return clients_list
    #print(ans.summary/show()) - use to see the packet format 
    
    
def print_result(results_list0
    print("IP\t\t\t MAC Address\n---------------------------------------------")
    for client in results_list:
        print(client["ip"] ++ "\t\t" + client["mac")
    
scan_result  = scan("192.168.0.1/24")
print_result(scan_result)