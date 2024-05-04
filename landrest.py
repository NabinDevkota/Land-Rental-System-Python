
def landrent():
    lands_data = read.available_land("lands_data.json")  # Replace "lands_data.csv" with the path to your file
    while True:
        print("Enter 'rent' to rent the land, 'return' to return the land, or 'exit' to quit: ")
        user_input = input().strip().lower() 
        if user_input == 'rent':
            userinterface.rent(lands_data)
        elif user_input == 'return':
            userinterface.return_land(lands_data)
        elif user_input == 'exit':
            break
        else:
            print("Invalid input. Please try again!")

if __name__ == "__landrent__":
    landrent()
