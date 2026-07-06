from tkinter import *
from tkinter import messagebox
from twilio.rest import Client
from openpyxl import load_workbook
import os

file_path = os.path.join(os.path.dirname(__file__), "contacts.xlsx")

account_sid = "ACf6621a3ddbec253533f97c66a4f49f66"
auth_token = "dd38fa96a34095d5ac1d17a21c0f7716"

client = Client(account_sid, auth_token)

twilio_number = "+12317902643"

root = Tk()
root.title("Excel SMS Sender")
root.geometry("350x200")
root.resizable(False, False)

Label(root, text="Send SMS From Excel", font=("Arial", 14, "bold")).pack(pady=20)

def send_excel_sms():
    try:
        workbook = load_workbook(file_path)
        print("File:",file_path)
        sheet = workbook.active
        print("Rows:",sheet.max_row)

        count = 0

        for row in range(2, sheet.max_row + 1):
            number = sheet.cell(row=row, column=1).value
            message = sheet.cell(row=row, column=2).value
            print(number,message)

            if number and message:
                client.messages.create(
                    body=str(message),
                    from_=twilio_number,
                    to=str(number)
                )
                count += 1

        messagebox.showinfo("Success", f"{count} SMS Sent Successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))

Button(
    root,
    text="SEND EXCEL SMS",
    command=send_excel_sms,
    width=20,
    bg="lightgray"
).pack(pady=20)

root.mainloop()