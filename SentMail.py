import smtplib

content = "Deneme Mail Gonderimi"
sender = "halilberk2002@gmail.com"
password = "halilberk2002"
to = "halilberk2002@gmail.com"

server = smtplib.SMTP("smtp.gmail.com",587)
server.ehlo()
server.starttls()
server.login(sender,password)
server.sendmail(sender,to,content)
server.close()
