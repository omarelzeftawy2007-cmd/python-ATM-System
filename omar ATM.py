



import tkinter as tk
from tkinter import messagebox

class BankAccount:
    def __init__(self, name, balance, pin, account_number): 
        self.name = name
        self.balance = balance
        self.pin = pin
        self.account_number = account_number

    def check_pin(self, entered_pin):
        return self.pin == entered_pin

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")
        print(f"Current Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
            return False
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
            print(f"Current Balance: {self.balance}")
            return True

    def show_balance(self):
        print(f"Your Balance is: {self.balance}")

def start_atm():
    my_account = BankAccount("omar", 1000, "1234", "100200")
    
    root = tk.Tk()
    root.title("ATM System")
    root.geometry("500x400")

    
    login_frame = tk.Frame(root)
    main_frame = tk.Frame(root)

    def show_main_screen():
        login_frame.pack_forget()
        main_frame.pack(pady=20)

    def handle_login():
        entered_acc = entry_acc.get()
        entered_pin = entry_pin.get()
        if entered_acc == my_account.account_number and entered_pin == my_account.pin:
            show_main_screen()
        else:
            messagebox.showerror("Error", "Wrong Account Number or PIN")

    
    login_frame.pack(pady=50)
    
    tk.Label(login_frame, text="Account Number:").pack()
    entry_acc = tk.Entry(login_frame)
    entry_acc.pack(pady=5)

    tk.Label(login_frame, text="PIN:").pack()
    entry_pin = tk.Entry(login_frame, show="*")
    entry_pin.pack(pady=5)

    tk.Button(login_frame, text="Login", command=handle_login, bg="blue", fg="white").pack(pady=10)

    
    def update_display():
        lbl_balance.config(text=f"Balance: {my_account.balance}")

    def handle_deposit():
        try:
            amt = float(entry_amount.get())
            my_account.deposit(amt)
            update_display()
            messagebox.showinfo("Success", "Money added!")
            entry_amount.delete(0, tk.END)
        except:
            messagebox.showerror("Error", "Invalid input")

    def handle_withdraw():
        try:
            amt = float(entry_amount.get())
            if my_account.withdraw(amt):
                update_display()
                messagebox.showinfo("Success", "Money withdrawn!")
            else:
                messagebox.showwarning("Warning", "No enough money")
            entry_amount.delete(0, tk.END)
        except:
            messagebox.showerror("Error", "Invalid input")

    lbl_balance = tk.Label(main_frame, text=f"Balance: {my_account.balance}", font=("Arial", 14))
    lbl_balance.pack(pady=20)

    entry_amount = tk.Entry(main_frame, font=("Arial", 12))
    entry_amount.pack(pady=10)

    btn_deposit = tk.Button(main_frame, text="Deposit", command=handle_deposit, width=15, bg="lightgreen")
    btn_deposit.pack(pady=5)

    btn_withdraw = tk.Button(main_frame, text="Withdraw", command=handle_withdraw, width=15, bg="orange")
    btn_withdraw.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    start_atm()