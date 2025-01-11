import pandas as pd

# DataFrame initialization
filename = 'ExpenseTracker.csv'
try:
    df = pd.read_csv(filename)
except FileNotFoundError:
    df = pd.DataFrame({"Date": [], "Category": [], "Amount": [], "Type": []})

# Function to add a transaction
def add_transaction(df):
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport): ")
    
    while True:
        try:
            amount = float(input("Enter the amount: ")) 
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    
    trans_type = input("Enter the type (Expense/Income): ")

    # Create a new transaction and append it to the DataFrame
    new_row = pd.DataFrame({"Date": [date], "Category": [category], "Amount": [amount], "Type": [trans_type]})
    df = pd.concat([df, new_row], ignore_index=True)  # Append and return the updated DataFrame
    df.to_csv(filename, index=False)  # Save to CSV
    print("Added Successfully.")
    return df  # Return the updated DataFrame

# Function to edit a transaction
def edit_transaction(df):
    print("Current transactions:")
    print(df)
    index = int(input("Enter the index of the expense to edit: "))
    
    if index in range(len(df)):
        date = input("Enter the new date (YYYY-MM-DD): ")
        category = input("Enter the new expense category: ")
        
        while True:
            try:
                amount = float(input("Enter the new amount: "))
                break
            except ValueError:
                print("Invalid amount. Please enter a number.")
        
        trans_type = input("Enter the new expense type (Expense/Income): ")

        # Update the transaction
        df.loc[index] = {"Date": date, "Category": category, "Amount": amount, "Type": trans_type}
        df.to_csv(filename, index=False)  # Save to CSV
        print("Updated Successfully.")
    else:
        print("Invalid index. No changes made.")
    
    return df  # Return the updated DataFrame

# Function to delete a transaction
def delete_transaction(df):
    print("Current transactions:")
    print(df)
    index = int(input("Enter the index of the transaction you want to delete: "))
    
    if index in range(len(df)):
        df = df.drop(index).reset_index(drop=True)  # Delete the transaction and reset the index
        df.to_csv(filename, index=False)  # Save to CSV
        print("Transaction deleted successfully!")
    else:
        print("Invalid index. No changes made.")
    
    return df  # Return the updated DataFrame

# Function to view summary
def view_summary(df):
    total_amount = df['Amount'].sum()
    print(f"\nTotal amount spent: {total_amount}")

# Main loop
while True:
    print("""
    Personal Expense Tracker
        1. Add Transaction
        2. Edit Transaction
        3. Delete Transaction
        4. View Summary
        5. Save and Exit
    """)
    
    choice = input("Enter your choice: ")

    if choice == "1":
        df = add_transaction(df)  # Capture the updated DataFrame
    elif choice == "2":
        df = edit_transaction(df)  # Ensure edit_transaction returns the updated DataFrame
    elif choice == "3":
        df = delete_transaction(df)  # Ensure delete_transaction returns the updated DataFrame
    elif choice == "4":
        view_summary(df)
    elif choice == "5":
        df.to_csv(filename, index=False)  # Save the DataFrame to a CSV file
        print(f"Data saved to {filename}. Exiting...")
        break
    else:
        print("Invalid choice, please try again.")

