#created by Rakshit Jain and Himank Jain XI A
# Step 1: Initialize an empty dictionary to store the linked data
linked_data = {}

# Step 2: Define a function to add a person’s information
def add_person():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    sport = input("Enter preferred sport: ")
    key = (name, age)  # Create a tuple (name, age)
    linked_data[key] = sport  # Map the tuple to the preferred sport
    print(f"Data added: ({name}, {age}) -> {sport}")

# Step 3: Define a function to retrieve the sport based on name and age
def get_sport():
    name = input("Enter name to search: ")
    age = int(input("Enter age to search: "))
    key = (name, age)
    if key in linked_data:
        print(f"Preferred sport for ({name}, {age}) is: {linked_data[key]}")
    else:
        print("No sport found for this person.")

# Step 4: Define a function to display all entries in the linked data
def display_all_data():
    if linked_data:
        print("Current entries in the linked data:")
        for key, value in linked_data.items():
            print(f"Name: {key[0]}, Age: {key[1]} -> Sport: {value}")
    else:
        print("No data available.")

# Main Menu to interact with the user
def main_menu():
    while True:
        print("\n--- Menu ---")
        print("1. Add person")
        print("2. Get sport")
        print("3. Display all data")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_person()
        elif choice == '2':
            get_sport()
        elif choice == '3':
            display_all_data()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

# Run the main menu
main_menu()
