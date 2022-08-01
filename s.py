import smtplib
import imghdr
from email.message import EmailMessage
import pandas as pd
import dataframe_image
from datetime import datetime as dt
import requests


pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)
df=pd.read_excel("cars.xlsx")
# print(df)

new_df=df.tail(10)

token='5360919649:AAGZgsx4IpU1SGe64v82Oj9fmjPMVOBakQU'
chat_id="-1001687356814"


dataframe_image.export(new_df,f"./images/{dt.now().date()}.png")

Sender_Email = "yashwanthbs1208@gmail.com"
Reciever_Email = ["nirupgowda0882@gmail.com"]#,"htv6902@gmail.com","niruphombegowda1999@gmail.com",'nirupgowda1999@gmail.com']
Password = "ofhqncekyefrrrxw"

newMessage = EmailMessage()                         
newMessage['Subject'] = f"Checkout {dt.now().date()} Cars Work Report " 
newMessage['From'] = Sender_Email                   
newMessage['To'] = Reciever_Email                   
newMessage.set_content('Image attached!') 


files = [f"./images/{dt.now().date()}.png"]
file=open(f"./images/{dt.now().date()}.png",'rb')
msg=newMessage['Subject']
data={'chat_id':chat_id,
    'caption':msg}
telegram_msg = f'https://api.telegram.org/bot{token}/sendPhoto'
requests.post(telegram_msg,data,files={'photo':file})


for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Sender_Email, Password)              
    smtp.send_message(newMessage)

import subprocess
def run(*args):
    return subprocess.check_call(['git'] + list(args))

def commit():
    commit_message ="Type in your commit message: "
    run("add","-A")
    run("commit", "-am", commit_message)
    run("push")

commit()

print("success updated website and mail sent.. closing the program")