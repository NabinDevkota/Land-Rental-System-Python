import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import subprocess

from operations import calculate_price
from read import read_lands_data
from write import write_invoice

def open_land_entry_form():
    try:
        subprocess.run(["python", "land_entry_form.py"])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def generate_invoice_gui(invoice_data):
    invoice_window = tk.Toplevel()
    invoice_window.title("Invoice")

    tree = ttk.Treeview(invoice_window)
    tree["columns"] = ("Property", "Value")
    tree.column("#0", width=120, minwidth=120)
    tree.column("Property", anchor=tk.CENTER, width=120, minwidth=120)
    tree.column("Value", anchor=tk.CENTER, width=200, minwidth=200)
    tree.heading("#0", text="Index", anchor=tk.CENTER)
    tree.heading("Property", text="Property", anchor=tk.CENTER)
    tree.heading("Value", text="Value", anchor=tk.CENTER)

    index = 1
    for line in invoice_data.split('\n'):
        label_text = line.split(':')
        tree.insert("", index, text=index, values=(label_text[0], label_text[1]))
        index += 1

    tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    close_button = ttk.Button(invoice_window, text="Close", command=invoice_window.destroy)
    close_button.pack(pady=10)

def generate_rent_invoice(kitta, name, duration, phone, status):
    print("Generating rent invoice...")
    lands_data = read_lands_data('lands_data.json')
    land_found = False
    for item in lands_data:
        if item.get('Kitta') == kitta:
            land_found = True
            price = calculate_price(item['Price'], duration)
            invoice_data = f'Name: {name}\nPhone Number: {phone}\nKitta Number: {item.get("Kitta")}\nCity: {item.get("City/District")}\nDirection: {item.get("Direction of land")}\nArea: {item.get("Aana")}\nDuration (months): {duration}\nPrice: {price}\nStatus: {status}'
            print("Rent Invoice Data:", invoice_data)
            generate_invoice_gui(invoice_data)
            print("Rent Invoice generated successfully.")

            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime('%Y-%m-%d_%H-%M-%S')
            file_name = f"rent_invoice_{formatted_time}.txt"
            write_invoice(file_name, invoice_data)
            break

    if not land_found:
        messagebox.showerror("Error", f"Error: Land with kitta number {kitta} not found for rent.")

def display_available_lands():
    lands_data = read_lands_data('lands_data.json')
    available_lands = [f"{land['Kitta']}: {land['City/District']} - {land['Direction of land']}" for land in lands_data]
    available_lands_text = "\n".join(available_lands)
    messagebox.showinfo("Available Lands", f"Available Lands:\n{available_lands_text}")

def rent_land(kitta, name, duration, phone, status):
    try:
        generate_rent_invoice(kitta, name, duration, phone, status)
        messagebox.showinfo("Success", "Congratulations! You rented a land. Please Check the invoice.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Land Rental Application")

# Set the size of the root window
window_width = 800
window_height = 600

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position of the window
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

# Set the geometry of the window
root.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")

tk.Label(root, text="Kitta Number:", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", padx=10, pady=5)
tk.Label(root, text="Name:", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", padx=10, pady=5)
tk.Label(root, text="Duration (in months):", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w", padx=10, pady=5)
tk.Label(root, text="Phone Number:", font=("Helvetica", 12)).grid(row=3, column=0, sticky="w", padx=10, pady=5)

kitta_entry = ttk.Entry(root, font=("Helvetica", 12))
name_entry = ttk.Entry(root, font=("Helvetica", 12))
duration_entry = ttk.Entry(root, font=("Helvetica", 12))
phone_entry = ttk.Entry(root, font=("Helvetica", 12))
kitta_entry.grid(row=0, column=1, padx=10, pady=5)
name_entry.grid(row=1, column=1, padx=10, pady=5)
duration_entry.grid(row=2, column=1, padx=10, pady=5)
phone_entry.grid(row=3, column=1, padx=10, pady=5)

rent_button = ttk.Button(root, text="Rent", command=lambda: rent_land(int(kitta_entry.get()), name_entry.get(), int(duration_entry.get()), phone_entry.get(), 'Land rented successfully'))
rent_button.grid(row=4, column=0, columnspan=2, pady=10)

display_lands_button = ttk.Button(root, text="Display Available Lands", command=display_available_lands)
display_lands_button.grid(row=5, column=0, columnspan=2, pady=10)

# Button to open the land entry form
open_form_button = ttk.Button(root, text="Open Land Entry Form", command=open_land_entry_form)
open_form_button.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
