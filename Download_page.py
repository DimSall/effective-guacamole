#!/usr/bin/env python 
import requests
url = "google" 

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

with open(f"C:/Users/dsallako/OneDrive - Cisco/Desktop/Python/subdomains.list.txt" , "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "/" + url
        response = request(test_url)
        if response:
            print("Discovered subdomain" + test_url)