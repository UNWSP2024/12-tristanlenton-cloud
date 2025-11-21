import tkinter as tk
from tkinter import messagebox


def calculate_charge():
    try:
        minutes = float(minutes_entry.get())
        if minutes < 0:
            messagebox.showerror("Error", "Minutes must be a positive number.")
            return

        rate = rate_var.get()
        charge = minutes * rate

        messagebox.showinfo("Call Charge", f"Total charge: ${charge:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

window = tk.Tk()
window.title("Telephone Call Charge Calculator")

rate_var = tk.DoubleVar()
rate_var.set(0.02)

tk.Label(window, text="Select Rate Category:").grid(row=0, column=0, sticky="w")

tk.Radiobutton(window, text="Daytime (6:00 AM - 5:59 PM)  $0.02/min",
               variable=rate_var, value=0.02).grid(row=1, column=0, sticky="w")

tk.Radiobutton(window, text="Evening (6:00 PM - 11:59 PM)  $0.12/min",
               variable=rate_var, value=0.12).grid(row=2, column=0, sticky="w")

tk.Radiobutton(window, text="Off-Peak (Midnight - 5:59 AM)  $0.05/min",
               variable=rate_var, value=0.05).grid(row=3, column=0, sticky="w")

tk.Label(window, text="Enter call length (minutes):").grid(row=4, column=0, pady=5, sticky="w")
minutes_entry = tk.Entry(window)
minutes_entry.grid(row=5, column=0, pady=5)

tk.Button(window, text="Calculate Charge", command=calculate_charge).grid(row=6, column=0, pady=10)

window.mainloop()
