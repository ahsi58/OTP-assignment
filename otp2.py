from twilio.rest import Client
import random
import keys
import smtplib

client=Client(keys.account_sid, keys.auth_token)

digits="0123456789"

# function for otp generation
def generate_otp():
    otp=""
    for i in range(6):
      otp+=random.choice(digits)

    return otp

fotp=generate_otp()

# function for checking mobile number
def validate_mobile(num):
    return len(num) == 10 and num.isdigit()

# function to send otp via sms ans validate number
def send_otp_over_mobile(target_no,fotp):
    
    if(validate_mobile(target_no)):
        target_no="+91"+target_no
        message=client.messages.create(
          body="Your OTP is "+fotp,
          from_=keys.twilio_no,
          to=keys.target_no
        )
        print(message.body)
      
    else:
       print("INVALID MOBILE NUMBER!")
       target_no=input("ENTER AGAIN: ")
       validate_mobile(target_no)
       send_otp_over_mobile(target_no,fotp)

#function to check email
def validate_email(mail):
   if "@" not in mail and "." not in mail:
      return False
   else:
      return True

# function to send otp via email and validate email
def send_otp_over_email(mail,fotp,sender,password):
   if(validate_email(mail)):
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender,password)
        msg_body="Your OTP is "+fotp
        server.sendmail(sender,mail,msg_body)
        print("OTP sent! ",fotp)
   else:
        print("INVALID MAIL!")
        mail=input("ENTER AGAIN: ")
        validate_email(mail)
        send_otp_over_email(mail,fotp,sender,password)
      
 
# drivers code
print("Welcome to generate OTP.How do you want to send the otp?")
ans=input("Through Mobile or Email: ")

sender="ahsipatil369@gmail.com"  
password="znnozwrslhfdavcu"


if(ans.lower()=="mobile"):
    
    number=input("ENTER YOUR MOBILE NUMBER: ")
    validate_mobile(number)
    send_otp_over_mobile(number,fotp)

elif(ans.lower()=="email"):
    
    recipent=input("ENTER YOUR MAIL ID: ")
    send_otp_over_email(recipent,fotp,sender,password)

# end of program

