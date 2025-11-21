import tkinter as tk
from tkinter import messagebox

def calculate_total():
    total = 0
    if oil_var.get():
        total += 30
    if lube_var.get():
        total += 20
    if rad_var.get():
        total += 40
    if trans_var.get():
        total += 100
    if insp_var.get():
        total += 35
    if muffler_var.get():
        total += 200
    if tire_var.get():
        total += 20

    result_label.config(text=f"Total Charges: ${total:.2f}")

window = tk.Tk()
window.title("Joe's Automotive Service Calculator")

oil_var = tk.IntVar()
lube_var = tk.IntVar()
rad_var = tk.IntVar()
trans_var = tk.IntVar()
insp_var = tk.IntVar()
muffler_var = tk.IntVar()
tire_var = tk.IntVar()

tk.Checkbutton(window, text="Oil Change ($30)", variable=oil_var).grid(row=0, column=0, sticky="w")
tk.Checkbutton(window, text="Lube Job ($20)", variable=lube_var).grid(row=1, column=0, sticky="w")
tk.Checkbutton(window, text="Radiator Flush ($40)", variable=rad_var).grid(row=2, column=0, sticky="w")
tk.Checkbutton(window, text="Transmission Fluid ($100)", variable=trans_var).grid(row=3, column=0, sticky="w")
tk.Checkbutton(window, text="Inspection ($35)", variable=insp_var).grid(row=4, column=0, sticky="w")
tk.Checkbutton(window, text="Muffler Replacement ($200)", variable=muffler_var).grid(row=5, column=0, sticky="w")
tk.Checkbutton(window, text="Tire Rotation ($20)", variable=tire_var).grid(row=6, column=0, sticky="w")

tk.Button(window, text="Calculate Total", command=calculate_total).grid(row=7, column=0, pady=10)

result_label = tk.Label(window, text="Total Charges: $0.00", font=("Arial", 12, "bold"))
result_label.grid(row=8, column=0, pady=10)

window.mainloop()
