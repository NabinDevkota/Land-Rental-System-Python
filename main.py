import json
import tkinter as tk
from tkinter import messagebox
from write import read_lands_data, generate_invoice
import  read


def rent_land(lands_data_path, kitta, name, duration, phone):
    with open(lands_data_path, "r") as file:
        lands_data = json.load(file)
    
    available = False
    for land in lands_data:
        if land['kitta_number'] == kitta:
            if land['status'] == 'Available':
                available = True
                # Update status to 'Rented'
                land['status'] = 'Rented'
                break
            else:
                messagebox.showerror("Error", f"Land with Kitta number {kitta} is not available for rent.")
                return

    if available:
        # Save updated data back to file
        with open(lands_data_path, "w") as file:
            json.dump(lands_data, file, indent=4)
        
        # Generate invoice
        status = 'Land rented successfully'
        generate_invoice(kitta, name, duration, phone, status)
        messagebox.showinfo("Success", "Congratulations! You rented a land. Please Check the invoice.")

