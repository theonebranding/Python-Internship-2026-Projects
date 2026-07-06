from tkinter import *
from tkinter import messagebox
from twilio.rest import Client

account_sid ="ACf6621a3ddbec253533f97c66a4f49f66"
auth_token = "dd38fa96a34095d5ac1d17a21c0f7716"

client = Client(account_sid, auth_token)

twilio_number = "+12317902643"

root = Tk()
root.title("Message Sender")
root.geometry("350x300")
root.resizable(False, False)


Label(root, text="Mobile Number", font=("Arial", 12)).pack(pady=5)

textNumber = Entry(root, width=35)
textNumber.pack()

Label(root, text="Message", font=("Arial", 12)).pack(pady=5)


textMessage = Text(root, width=35, height=8)
textMessage.pack()

def send_sms(number, message):
    client.messages.create(
        body=message,
        from_=twilio_number,
        to=number
    )

def sendClick():
    num = textNumber.get()
    msg = textMessage.get("1.0", END).strip()

    if num == "" or msg == "":
        messagebox.showerror("Error", "All fields are required!")
    else:
        try:
            send_sms(num, msg)
            messagebox.showinfo("Success", "SMS Sent Successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))



Button(
    root,
    text="SEND SMS",
    command=sendClick,
    width=15,
    bg="lightgray"
).pack(pady=10)

root.mainloop()