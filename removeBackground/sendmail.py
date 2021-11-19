import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from email.mime.application import MIMEApplication
cwd = os.getcwd()
mail_content = ""
sender_address = 'sameergupta1499@gmail.com'
sender_pass = '97Reemas97@'
receiver_address = 'tanya.verma422@gmail.com'

message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'File Successfully Converted!'   #The subject line
message.attach(MIMEText(mail_content, 'plain'))

file1 = open('url.txt', 'r')
file_name = file1.readline()
total_lines = [i for i in file_name.split() if i.isdigit()][0]
file_name=file_name.replace(total_lines,'')
file_name=file_name.replace(' ','_')
file_name=file_name.replace('\n','')
file_name = file_name+'.zip'
if file_name=='.zip':
    file_name='images.zip'

#with open(cwd+"/zip/"+file_name, 'rb') as file:
with open("/home/sameer/.ssh/id_rsa.pub",'rb') as file:
    message.attach(MIMEApplication(file.read(), Name=file_name))
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')
