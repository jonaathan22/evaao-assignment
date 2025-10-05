import json
import sys
from datetime import datetime

# --- Data Handling Functions ---
def load_expenses():
    """Loads expenses from the JSON file."""
    try:
        with open('expenses.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):
    """Saves the expenses list to the JSON file."""
    with open('expenses.json', 'w') as f:
        json.dump(expenses, f, indent=4)

# --- Core Features ---
def add_expense(amount, date, note):
    """Adds a new expense."""
    expenses = load_expenses()
    
    # Basic Validation
    try:
        amount = float(amount)
    except ValueError:
        print("Error: Amount must be a number.")
        return

    # Create a new expense dictionary
    new_expense = {
        'id': len(expenses) + 1,
        'amount': amount,
        'date': date,
        'note': note
    }
    
    expenses.append(new_expense)
    save_expenses(expenses)
    print(f"Successfully added expense: {note}")

def view_expenses():
    """Views all expenses."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
        
    print("\n--- All Expenses ---")
    for expense in expenses:
        print(f"ID: {expense['id']}, Amount: {expense['amount']}, Date: {expense['date']}, Note: {expense['note']}")
    print("--------------------\n")

# --- Main Program Logic ---
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tracker.py <command> [arguments]")
        print("Commands: add, view")
        sys.exit(1)

    command = sys.argv[1]

    if command == 'add':
        if len(sys.argv) != 5:
            print("Usage: python tracker.py add <amount> <date YYYY-MM-DD> \"<note>\"")
        else:
            add_expense(sys.argv[2], sys.argv[3], sys.argv[4])
    elif command == 'view':
        view_expenses()
    else:
        print(f"Unknown command: {command}")