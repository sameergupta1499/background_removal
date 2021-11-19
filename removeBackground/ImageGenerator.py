
import requests
import os
from zipfile import ZipFile
import os
from os.path import basename
file1 = open('url.txt', 'r')
count = 0
url_list = []
# print(os.getcwd())
cwd = os.getcwd()
image_dir = cwd + "/images/"
print(image_dir)
import os

###deleting already exist image folder
try:
    import shutil
    shutil.rmtree(image_dir, ignore_errors=True)
except OSError:
    print ("Directory doesnt Exist" % image_dir)
try:
    os.mkdir(image_dir)
except OSError:
    print ("Creation of the directory %s failed" % image_dir)
import time
time.sleep(1)
flag = False
bad_url=False
try:
    while True:
        count += 1
        if count ==1 and flag==False:
            url = file1.readline()
            url = url.replace('\n','')
            url = [int(i) for i in url.split() if i.isdigit()][0]
            count = int(url)-1
            flag=True
            continue
        url = file1.readline()
        url = url.replace('\n','')
        url_list.append(url)
        if not url:
            break
        try:
            r = requests.get(url)
            # print(url)
            if ('.jpg' not in url.lower()) and ('.png' not in url.lower()) and ('.jpeg' not in url.lower()):
                bad_url = True
        except:
            bad_url = True
        with open(image_dir+str(count)+".jpg", 'wb') as f:
            if bad_url==True:
                bad_url=False
                print('bad_url')
                import base64
                string_img='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'
                # base64_bytes = base64.encode(string_img)
                base64_img_bytes = string_img.encode('utf-8')
                decoded_image_data = base64.decodebytes(base64_img_bytes)
                f.write(decoded_image_data)
            else:
                # print(type(r.content))
                f.write(r.content)

    file1.close()
except(requests.exceptions.MissingSchema):
    print("ignoring this exception")

print("images Downloaded")

# #
# # with ZipFile('images.zip', 'w') as zipObj:
# #    # Iterate over all the files in directory
# #    for folderName, subfolders, filenames in os.walk(image_dir):
# #        for filename in filenames:
# #            #create complete filepath of file in directory
# #            filePath = os.path.join(folderName, filename)
# #            # Add file to zip
# #            zipObj.write(filePath, basename(filePath))
# #
# # import smtplib
# # from email.mime.multipart import MIMEMultipart
# # from email.mime.text import MIMEText
# # from email.mime.application import MIMEApplication
# # mail_content = ""
# # sender_address = 'sameergupta1499@gmail.com'
# # sender_pass = '97Reemas97@'
# # receiver_address = 'tanya.verma422@gmail.com'
# #
# # message = MIMEMultipart()
# # message['From'] = sender_address
# # message['To'] = receiver_address
# # message['Subject'] = 'File Successfully Converted!'   #The subject line
# # message.attach(MIMEText(mail_content, 'plain'))
# # with open(cwd+"/images.zip", 'rb') as file:
# #     message.attach(MIMEApplication(file.read(), Name='images.zip'))
# # session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
# # session.starttls() #enable security
# # session.login(sender_address, sender_pass) #login with mail_id and password
# # text = message.as_string()
# # session.sendmail(sender_address, receiver_address, text)
# # session.quit()
# # print('Mail Sent')