import tkinter as tk
from tkinter import messagebox, ttk
import json
import datetime
from operations import calculate_price
import read
# Function to read lands_data from JSON file
def read_lands_data():
    with open('lands_data.json', 'r') as file:
        lands_data = json.load(file)
    return lands_data

# Function to generate invoice in GUI format
def generate_invoice_gui(invoice_data):
    invoice_window = tk.Toplevel()
    invoice_window.title("Invoice")

    # Create Treeview widget
    tree = ttk.Treeview(invoice_window)
    tree["columns"] = ("Property", "Value")
    tree.column("#0", width=120, minwidth=120)
    tree.column("Property", anchor=tk.CENTER, width=120, minwidth=120)
    tree.column("Value", anchor=tk.CENTER, width=120, minwidth=120)
    tree.heading("#0", text="Index", anchor=tk.CENTER)
    tree.heading("Property", text="Property", anchor=tk.CENTER)
    tree.heading("Value", text="Value", anchor=tk.CENTER)

    # Insert invoice data into Treeview
    index = 1
    for line in invoice_data.split('\n'):
        label_text = line.split(':')
        tree.insert("", index, text=index, values=(label_text[0], label_text[1]))
        index += 1

    tree.pack(padx=10, pady=10)

    # Close button
    close_button = tk.Button(invoice_window, text="Close", command=invoice_window.destroy)
    close_button.pack(pady=10)

# Function to generate invoice for renting land
def generate_rent_invoice(kitta, name, duration, phone, status):
    print("Generating rent invoice...")
    lands_data = read_lands_data()  # Read lands_data from file
    for item in lands_data:
        if item.get('Kitta') == kitta:
            price = calculate_price(item['Price'], duration)
            invoice_data = f'Name: {name}\nPhone Number: {phone}\nKitta Number: {item.get("Kitta")}\nCity: {item.get("City/District")}\nDirection: {item.get("Direction of land")}\nArea: {item.get("Aana")}\nPrice: {price}\nStatus: {status}'
            print("Rent Invoice Data:", invoice_data)
            generate_invoice_gui(invoice_data)  # Display invoice in GUI format
            print("Rent Invoice generated successfully.")

            # Write invoice data to text file
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime('%Y-%m-%d_%H-%M-%S')
            file_name = f"rent_invoice_{formatted_time}.txt"
            with open(file_name, 'w') as file:
                file.write(invoice_data)
            print(f"Rent Invoice saved as {file_name}.")
            break
    else:
        print("Error: Land not found with the provided kitta number for rent.")

# Function to generate invoice for returning land
def generate_return_invoice(kitta, name, phone, status):
    print("Generating return invoice...")
    lands_data = read_lands_data()  # Read lands_data from file
    for item in lands_data:
        if item.get('Kitta') == kitta:
            invoice_data = f'Name: {name}\nPhone Number: {phone}\nKitta Number: {item.get("Kitta")}\nCity: {item.get("City/District")}\nDirection: {item.get("Direction of land")}\nArea: {item.get("Aana")}\nStatus: {status}'
            print("Return Invoice Data:", invoice_data)
            generate_invoice_gui(invoice_data)  # Display invoice in GUI format
            print("Return Invoice generated successfully.")

            # Write invoice data to text file
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime('%Y-%m-%d_%H-%M-%S')
            file_name = f"return_invoice_{formatted_time}.txt"
            with open(file_name, 'w') as file:
                file.write(invoice_data)
            print(f"Return Invoice saved as {file_name}.")
            break
    else:
        print("Error: Land not found with the provided kitta number for return.")

# Function to rent land
def rent_land():
    kitta = int(kitta_entry.get())
    name = name_entry.get()
    duration = int(duration_entry.get())
    phone = phone_entry.get()
    status = 'Land rented successfully'

    generate_rent_invoice(kitta, name, duration, phone, status)
    # Add your logic to handle the rent process here
    messagebox.showinfo("Success", "Congratulations! You rented a land. Please Check the invoice.")

# Function to return land
def return_land():
    kitta = int(kitta_entry.get())
    name = name_entry.get()
    phone = phone_entry.get()
    status = 'Land returned successfully'

    generate_return_invoice(kitta, name, phone, status)
    # Add your logic to handle the return process here
    messagebox.showinfo("Success", "Thank you for returning the land.")

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
rent_button.grid(row=4, column=0)

# Return button
return_button = tk.Button(root, text="Return", command=return_land)
return_button.grid(row=4, column=1)

root.mainloop()
