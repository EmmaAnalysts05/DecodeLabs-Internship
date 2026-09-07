import json
import os

# Path to store expenses
EXPENSES_FILE = "expenses.json"

# Load existing expenses
def load_expenses():
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, 'r') as f:
            return json.load(f)
    return []

# Save expenses to file
def save_expenses(expenses):
    with open(EXPENSES_FILE, 'w') as f:
        json.dump(expenses, f, indent=2)

# A. INITIALIZATION: Load previous expenses and calculate total
expenses = load_expenses()
total = sum(expenses)

# Display previously saved expenses
if expenses:
    print(f"Previously saved expenses: {expenses}")
    print(f"Current total: {total}\n")

# B. CONTINUOUS AUDIT LOOP: Keep accepting values until stopped
while True:
    # C. INPUT GATEKEEPER: Capture raw user data
    user_input = input("Enter an expense amount (or type 'quit' to exit): ")
    
    # D. THE KILL SWITCH: Check for sentinel value to end execution gracefully
    if user_input.lower() == 'quit':
        break  
        
    # E. DEFENSIVE CODING: Shield interface to implement type-safety & catch errors
    try:
        # Transforming raw unstructured string data into numeric data
        expense = int(user_input) 
    except ValueError:
        # Preventative measure: catches invalid data (like text) so the app doesn't crash
        print("Invalid Data. Please enter a valid number.")
        continue  # Skips back to the beginning of the loop
        
    # F. ACCUMULATOR PATTERN: Update stateful ledger formula
    # State(new) = State(old) + Input
    total += expense
    expenses.append(expense)
    
    # Save to file after each entry
    save_expenses(expenses)
    print(f"Running total: {total}")

# G. OUTPUT STREAM: Decouple backend engine calculation from final display interface
print(f"\nFINAL TOTAL SPENT: {total}") 