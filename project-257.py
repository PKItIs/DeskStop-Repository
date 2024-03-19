from tkinter import *
from web3 import Web3
from PIL import ImageTk, Image

root = Tk()
root.title("Account Details")

ganache_url = 'http://127.0.0.1:7545'

web3 = Web3(Web3.HTTPProvider(ganache_url))

img = ImageTk.PhotoImage(Image.open("logo.png"))
panel = Label(root, image=img, bg='white')
panel.pack(side="top")

frame = Frame(
    root,
    bg='white',
    padx=5,
    pady=5
)

Label(frame, text="Account 1:", fg="black", bg="white").grid(row=0, column=0, sticky=W, pady=10)
Label(frame, text="Account 2:", fg="black", bg="white").grid(row=1, column=0, sticky=W, pady=10)
Label(frame, text="Account 3:", fg="black", bg="white").grid(row=2, column=0, sticky=W, pady=10)
Label(frame, text="Account 4:", fg="black", bg="white").grid(row=3, column=0, sticky=W, pady=10)

# account1 = Entry(frame).grid(row=0, column=1, sticky=W, pady=20, padx=10)
# account2 = Entry(frame).grid(row=1, column=1, sticky=W, pady=20, padx=10)
# account3 = Entry(frame).grid(row=2, column=1, sticky=W, pady=20, padx=10)
# account4 = Entry(frame).grid(row=3, column=1, sticky=W, pady=20, padx=10)
account1 = Entry(
    frame,

)

account2 = Entry(
    frame,

)

account3 = Entry(
    frame,

)
account4 = Entry(
    frame,

)

account1.grid(row=0, column=1, pady=10, padx=20)
account2.grid(row=1, column=1, pady=10, padx=20)
account3.grid(row=2, column=1, pady=10, padx=20)
account4.grid(row=3, column=1, pady=10, padx=20)
result = Text(root, height=5, width=25, bg="white")


def check_balance_function():
    account_no = []
    account_no.append(account1.get())
    account_no.append(account2.get())
    account_no.append(account3.get())
    account_no.append(account4.get())
    count = 1
    for i in account_no:
        balance = web3.eth.getBalance(i)
        balance = balance * 0.000000000000000001
        result.insert(END, f"Account {count} balance is {balance} \n")
        count = count + 1

frame.pack()
check_balance = Button(
    root,
    width=15,
    text='CHECK BALANCE',
    command=check_balance_function,
    highlightbackground='white',
)
check_balance.pack(fill='both')

result.pack(pady=5)
root.mainloop()