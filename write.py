import datetime

def write_invoice(file_name, invoice_data):
    try:
        with open(file_name, 'w') as file:
            file.write(invoice_data)
        print(f"Invoice saved as {file_name}.")
    except Exception as e:
        print(f"Error: {e}")
