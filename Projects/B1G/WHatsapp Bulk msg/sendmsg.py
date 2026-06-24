import pandas as pd
import pywhatkit as kit
from datetime import datetime, timedelta
import time

df = pd.read_excel("contact2.xlsx")
df.columns =df.columns.str.strip().str.upper()

now =datetime.now()

for index, row in df.iterrows():
    if str(row['SEND(Y/N)']).strip().upper() == 'Y':
        phone = str(row['PHONE']).strip()
        if not phone.startswith("+"):
            phone = '+' + phone

        Message =str(row['MESSAGE']).strip()

        send_time = now + timedelta(minutes=3 + index)
        send_hour =send_time.hour
        send_minute =send_time.minute

        try:
            kit.sendwhatmsg(phone, Message, send_hour, send_minute, wait_time=30, tab_close=False)
            print(f"Message scheduled to {phone} at {send_hour}:{send_minute}")
            time.sleep(20)
        except Exception as e:
            print(f"Failed for {phone}: {e}")
