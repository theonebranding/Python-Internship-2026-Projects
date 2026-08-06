import requests


BOT_TOKEN = '8941560330:AAEKYMFypEltioXDChsHbMpGK9w2qa7WJuo'
Chat_id='5447310082'


msg='hello this is internship project given by professor and my name is mohammadsaad firoj bhai vahora , i am from anand '
url= f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={Chat_id}&text={msg}"
r=requests.get(url)
print(r.json())