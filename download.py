#!usr/bin/env python
import requests

def download(url):
	get_response = requests.get(url)
	file_name = url.split("\")[-1]
	with open(file_name, "wb") as out_file:
		out_file.write(get_response.content)

#Here we can add a file that we have on a server we own 
download()