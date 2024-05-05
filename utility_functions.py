import tkinter as tk
from tkinter import ttk
import calculate
import json
import datetime


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


# Updated generate_invoice function
def generate_invoice(kitta, name, duration, phone, status):
    print("Generating invoice...")
    lands_data = read_lands_data()  # Read lands_data from file
    for item in lands_data:
        if item.get('Kitta') == kitta:
            price = calculate.calculate_price(item['Price'], duration)
            invoice_data = f'Name: {name}\nPhone Number: {phone}\nKitta Number: {item.get("Kitta")}\nCity: {item.get("City/District")}\nDirection: {item.get("Direction of land")}\nArea: {item.get("Aana")}\nPrice: {price}\nStatus: {status}'
            print("Invoice Data:", invoice_data)
            generate_invoice_gui(invoice_data)  # Display invoice in GUI format
            print("Invoice generated successfully.")

            # Write invoice data to text file
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime('%Y-%m-%d_%H-%M-%S')
            file_name = f"invoice_{formatted_time}.txt"
            with open(file_name, 'w') as file:
                file.write(invoice_data)
            print(f"Invoice saved as {file_name}.")
            break
    else:
        print("Error: Land not found with the provided kitta number.")
