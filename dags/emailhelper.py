import smtplib

def send():
  
  try:
    x=smtplib.SMTP("smtp.gmail.com",587)
    x.starttls()
    x.login("username","password")
    subject="Testing"
    body_text="Testing email automation"
    message="subject{}{}".format(subject,body_text)
    x.sendmail("sender","receiver",message)
    print("success")
  except Exception as exception:
    print(exception)
    print("failure")