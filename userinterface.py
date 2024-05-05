import tkinter as tk
from tkinter import messagebox
import datetime
from tkinter import ttk
import json
from utility_functions import read_lands_data, generate_invoice

# Function to rent land
def rent_land():
    kitta = int(kitta_entry.get())
    name = name_entry.get()
    duration = int(duration_entry.get())
    phone = phone_entry.get()
    status = 'Land rented successfully'

    generate_invoice(kitta, name, duration, phone, status)
    # change_status(kitta)  # If you have this function, you can call it here
    messagebox.showinfo("Success", "Congratulations! You rented a land. Please Check the invoice.")


# Create Tkinter window
root = tk.Tk()
root.title("Land Rental Application")

# Labels
tk.Label(root, text="Kitta Number:").grid(row=0, column=0, sticky="w")
tk.Label(root, text="Name:").grid(row=1, column=0, sticky="w")
tk.Label(root, text="Duration (in months):").grid(row=2, column=0, sticky="w")
tk.Label(root, text="Phone Number:").grid(row=3, column=0, sticky="w")

# Entry fields
kitta_entry = tk.Entry(root)
name_entry = tk.Entry(root)
duration_entry = tk.Entry(root)
phone_entry = tk.Entry(root)
kitta_entry.grid(row=0, column=1)
name_entry.grid(row=1, column=1)
duration_entry.grid(row=2, column=1)
phone_entry.grid(row=3, column=1)

# Rent button
rent_button = tk.Button(root, text="Rent", command=rent_land)
rent_button.grid(row=4, column=0, columnspan=2)

root.mainloop()
