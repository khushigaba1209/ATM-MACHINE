# atm_frontend.py

import tkinter as tk
from tkinter import messagebox
from atm_backend import ATM

user = ATM("Khushi", "1234", 5000)

root = tk.Tk()
root.title("ATM Simulator - Frame Based")
root.geometry("400x400")
root.configure(bg="pink")

login_frame = tk.Frame(root, bg="pink")
menu_frame = tk.Frame(root, bg="pink")
deposit_frame = tk.Frame(root, bg="pink")
withdraw_frame = tk.Frame(root, bg="pink")

def show_frame(frame):
    for f in [login_frame, menu_frame, deposit_frame, withdraw_frame]:
        f.place_forget()
    frame.place(x=0, y=0, width=400, height=400)


tk.Label(login_frame, text="Welcome to ATM ", font=("Helvetica", 16, "bold"), bg="pink").pack(pady=20)
tk.Label(login_frame, text="Enter 4-digit PIN:", bg="pink").pack()
pin_entry = tk.Entry(login_frame, show="*")
pin_entry.pack(pady=10)

def verify_pin():
    if user.check_pin(pin_entry.get()):
        show_frame(menu_frame)
    else:
        messagebox.showerror("Invalid", " Incorrect PIN!")

tk.Button(login_frame, text="Login", command=verify_pin, bg="pink", fg="white").pack(pady=10)

tk.Label(menu_frame, text="ATM Main Menu ", font=("bold",14), bg="#e8f6f3").pack(pady=20)
tk.Button(menu_frame, text="Check Balance", width=20, command=lambda: messagebox.showinfo("Balance", f"💰 ₹{user.get_balance()}" )).pack(pady=5)
tk.Button(menu_frame, text="Deposit Money", width=20, command=lambda: show_frame(deposit_frame)).pack(pady=5)
tk.Button(menu_frame, text="Withdraw Money", width=20, command=lambda: show_frame(withdraw_frame)).pack(pady=5)
tk.Button(menu_frame, text="Exit", width=20, command=root.quit).pack(pady=10)


tk.Label(deposit_frame, text="Deposit Money ", font=("Italic", 14, "bold"), bg="pink").pack(pady=20)
dep_entry = tk.Entry(deposit_frame)
dep_entry.pack()

def deposit_amount():
    amount_text = dep_entry.get()
    if amount_text.isdigit():
        amount = int(amount_text)
        if user.deposit(amount):
            messagebox.showinfo("Success", f" ₹{amount} deposited!")
            dep_entry.delete(0, tk.END)
            show_frame(menu_frame)
        else:
            messagebox.showerror("Error", " Enter valid amount.")
    else:
        messagebox.showerror("Error", "Invalid input. Please enter a number.")

tk.Button(deposit_frame, text="Deposit", command=deposit_amount).pack(pady=5)
tk.Button(deposit_frame, text="Back", command=lambda: show_frame(menu_frame)).pack(pady=5)


tk.Label(withdraw_frame, text="Withdraw Money ", font=("Helvetica", 14, "bold"), bg="#e8f6f3").pack(pady=20)
with_entry = tk.Entry(withdraw_frame)
with_entry.pack()

def withdraw_amount():
    amount_text = with_entry.get()
    if amount_text.isdigit():
        amount = int(amount_text)
        if user.withdraw(amount):
            messagebox.showinfo("Success", f" ₹{amount} withdrawn!")
            with_entry.delete(0, tk.END)
            show_frame(menu_frame)
        else:
            messagebox.showerror("Error", " Insufficient balance.")
    else:
        messagebox.showerror("Error", " Invalid input. Please enter a number.")

tk.Button(withdraw_frame, text="Withdraw", command=withdraw_amount).pack(pady=5)
tk.Button(withdraw_frame, text="Back", command=lambda: show_frame(menu_frame)).pack(pady=5)

show_frame(login_frame)
root.mainloop()
