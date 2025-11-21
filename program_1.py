import tkinter as tk
from tkinter import messagebox

def calculate_mpg():
    try:
        gallons = float(gallons_entry.get())
        miles = float(miles_entry.get())

        if gallons <= 0:
            messagebox.showerror("Error", "Gallons must be greater than zero.")
            return

        mpg = miles / gallons
        result_label.config(text=f"MPG: {mpg:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

window = tk.Tk()
window.title("Gas Mileage Calculator")

tk.Label(window, text="Gallons the car holds:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
gallons_entry = tk.Entry(window)
gallons_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Miles the car can travel on a full tank:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
miles_entry = tk.Entry(window)
miles_entry.grid(row=1, column=1, padx=10, pady=5)

calc_button = tk.Button(window, text="Calculate MPG", command=calculate_mpg)
calc_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(window, text="MPG: ")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

window.mainloop()
