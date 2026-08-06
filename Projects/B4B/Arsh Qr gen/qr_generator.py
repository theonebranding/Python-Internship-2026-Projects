import qrcode

#taking upi ID as a input
upi_id = input("Enter Your UPI ID =")

#upi://pay?pa=UPI_ID&pn=NAME=Amount&cu=CURRENCY&tn=MESSAGE 

#defining the payment URL based on the UPI ID and the payment app
#you can modify these URLs based on the payment apps you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=recipient%20name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=recipient%20name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=recipient%20name&mc=1234'

#create QR code for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#save the qr code to image file(optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png') 

#display the qr code(you may need to install PIL/Pillow library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()