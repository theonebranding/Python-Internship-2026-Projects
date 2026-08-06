import smtplib as s

ob =s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('saadvahora2005@gmail.com','jcad frvg qfqe yoko')
subject="test python"
body="I LOVE Python"
massage="subject:{}\n\n{}".format(subject,body)
listadd=['saadvahora222@gmail.com',"saadvahora861@gmail.com"]
ob.sendmail('saadvahora2005@gmail.com',listadd,massage)
print("send mail")
ob.quit()