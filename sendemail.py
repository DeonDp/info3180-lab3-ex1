import smtplib 
from_addr = 'noednikretep@gmail.com' 
to_addr = 'deongohard@hotmail.com' 
from_name ='Noed Nikretep'
to_name ='Deon Peterkin'
subject ='INFO3180 mail'
msg= 'I am king'
message = """From: {} <{}> 
To: {} <{}> 
Subject: {} 
{} 
""" 
message_to_send = message.format(from_name, from_addr, to_name, 
to_addr, subject, msg) 
# Credentials (if needed) 
username = '' 
password = '' 
# The actual mail send 
server = smtplib.SMTP('smtp.gmail.com:587') 
server.starttls() 
server.login(username, password) 
server.sendmail(from_addr, to_addr, message_to_send) 
server.quit()