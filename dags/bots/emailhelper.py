import smtplib
from mongodbhelper import get_single_document


def send():
  
  try:
    x=smtplib.SMTP("smtp.gmail.com",587)
    x.starttls()
    config_data= get_single_document("config",{"name":"email_config"},{"username":1,"password":1,"_id":0})
    print(config_data)
    x.login(config_data["username"],config_data["password"])
    subject="Testing"
    body_text="Testing email automation"
    message="subject{}\n\n{}".format(subject,body_text)
    x.sendmail("abhisim0098@gmail.com","saitamasaysokay@gmail.com",message)
    print("success")
  except Exception as exception:
    print(exception)
    print("failure")
    
if __name__ == "__main__":
  send()