import smtplib as s

ob =s.SMTP('.smtp.gmail.com' ,465)
ob.ehlo()
ob.starttls()
ob.login("mahinvahora167@gmail.com" ,'Mahin1622')
subject="test python"
body="i love python"
massage="subject:{}\n\n{}".format(subject,body)
listadd=["vahoraaksha21@gmail.com",
         "shanavahora524@gmail.com"]
ob.sendmail('abc@gmail.com' ,listadd,massage)      
print("send mail")
ob.quit()