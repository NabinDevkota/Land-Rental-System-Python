import tkinter as tk
from tkinter import ttk
import json

def save_land_data():
    data = {
        "Kitta": int(kitta_entry.get()),
        "City/District": city_entry.get(),
        "Direction of land": direction_entry.get(),
        "Aana": int(aana_entry.get()),
        "Price": int(price_entry.get()),
        "Availability Status": availability_status_var.get()
    }
    with open('lands_data.json', 'r+') as file:
        lands_data = json.load(file)
        lands_data.append(data)
        file.seek(0)
        json.dump(lands_data, file, indent=4)
    clear_entries()
    print("Land data saved successfully.")

def clear_entries():
    kitta_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)
    direction_entry.delete(0, tk.END)
    aana_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Land Entry Form")

# Labels
tk.Label(root, text="Kitta Number:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
tk.Label(root, text="City/District:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
tk.Label(root, text="Direction of Land:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
tk.Label(root, text="Aana:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
tk.Label(root, text="Price:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
tk.Label(root, text="Availability Status:").grid(row=5, column=0, padx=5, pady=5, sticky="w")

# Entry fields
kitta_entry = ttk.Entry(root)
kitta_entry.grid(row=0, column=1, padx=5, pady=5)
city_entry = ttk.Entry(root)
city_entry.grid(row=1, column=1, padx=5, pady=5)
direction_entry = ttk.Entry(root)
direction_entry.grid(row=2, column=1, padx=5, pady=5)
aana_entry = ttk.Entry(root)
aana_entry.grid(row=3, column=1, padx=5, pady=5)
price_entry = ttk.Entry(root)
price_entry.grid(row=4, column=1, padx=5, pady=5)

# Combobox for Availability Status
availability_status_var = tk.StringVar()
availability_status_combobox = ttk.Combobox(root, textvariable=availability_status_var, values=["Available", "Not Available"])
availability_status_combobox.grid(row=5, column=1, padx=5, pady=5)

# Save button
save_button = ttk.Button(root, text="Save", command=save_land_data)
save_button.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
