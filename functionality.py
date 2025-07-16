import json
import datetime

incomes=[]
expenses=[]
repeating_incomes=[]
subscriptions=[]
personal_details={}
financial_targets=[]

def save_to_dict(amount, description):
    """Save the current state of the incomes to a dictionary. I use this function for abstracting the logic of saving."""
    incomes.append({"Income": int(amount), "Description": description})
    print(f"The amount of {amount}$ added with description: {description}")


def save_to_repeating_dict(amount, description, day_of_month):
    """Save the current state of the repeating incomes to a dictionary."""
    repeating_incomes.append({"Income": int(amount), "Description": description, "Day": day_of_month})
    print(f"The repeating income of {amount}$ added with description: {description} on day {day_of_month}")
    save_repeating_incomes_to_json()  # Save to JSON after adding a new repeating income

def save_to_expense_dict(amount, description):
    """Save the current state of the expenses to a dictionary."""
    expenses.append({"Expense": int(amount), "Description": description})
    print(f"The expense of {amount}$ added with description: {description}")

def save_to_subscription_dict(amount, description):
    """Save the current state of the subscriptions to a dictionary."""
    subscriptions.append({"Subscription": int(amount), "Description": description})
    print(f"The subscription of {amount}$ added with description: {description}")

def save_personal_details():
    """Save the personal details to a dictionary."""
    personal_details.update({"Wallet Name": personal_details["Wallet Name"], "Name": personal_details["Name"], "Email": personal_details["Email"], "Phone": personal_details["Phone"], "Job": personal_details["Job"]})
    print("Personal details saved successfully.")

def add_income():
    """Add a new income entry."""
    amount=(input("Enter income amount: " + "$"))
    description=input("Enter income description: ").lower().strip()
    if not amount.isdigit():
        print("Invalid income amount. Please enter a numeric value.")
        return
    save_to_dict(amount,description)


def remove_income(amount, description):
    """Remove an income entry using passed data."""
    try:
        amount = int(amount)
    except ValueError:
        print("Invalid income amount.")
        return

    description = description.lower().strip()

    for entry in incomes:
        if entry["Income"] == amount and entry["Description"].lower().strip() == description:
            incomes.remove(entry)
            print(f"Removed income: {amount}$ with description: {description}")
            return
    
    print("No matching income found.")




def repeat_income():
    """Set up a repeating income entry."""
    amount = input("Enter the repeating income amount: " + "$")
    description = input("Enter the repeating income description: ").lower().strip()
    if not amount.isdigit():
        print("Invalid income amount. Please enter a numeric value.")
        return
    day_of_month = day()
    if day_of_month is None:
        print("Invalid day input. Please try again.")
        return
    save_to_repeating_dict(amount, description, day_of_month)
    

def check_and_add_repeating_income():
    """Check if the current date matches the repeating income day and add it if it does."""  
    today = datetime.date.today()
    for entry in repeating_incomes:
        if entry["Day"] == today.day:
            save_to_repeating_dict(entry["Income"], entry["Description"], entry["Day"])
            return
       
def remove_repeating_income(amount, description, day):
    """Remove an existing repeating income entry."""
    try:
        amount= int(amount)
        day = int(day)
    except ValueError:
        print("Invalid input. Amount and day must be numeric.")
        return
    
    for entry in repeating_incomes:
        if (entry["Income"] == amount and entry["Description"].lower().strip() == description.lower().strip() and 
        entry["Day"] == day):
            # Remove the entry from the repeating incomes list
            repeating_incomes.remove(entry)
            print(f"Removed repeating income: {amount}$ with description: {description} on day {day}")
            return
    print(f"No repeating income found with description: {description}, amount: {amount}$ and day: {day}.")

def check_if_repeating_income():
    """check if there are any repeating incomes for today"""
    today = datetime.date.today()
    for entry in repeating_incomes:
        if entry["Day"] == today.day:
            print(f"Repeating income found: {entry['Income']}$ with description: {entry['Description']} on day {entry['Day']}")
            return True
    # If no repeating income found for today
    print("No repeating income found for today.")

def wallet_details_testing_function():
    """Display the details of the wallet, for terminal use."""
    personal_details["Wallet Name"] = input("Enter your wallet name: ").lower().strip()
    personal_details["Name"] = input("Enter your name: ").lower().strip()
    personal_details["Email"] = input("Enter your email: ").lower().strip()
    personal_details["Phone"] = input("Enter your phone number: ").strip()
    personal_details["Job"] = input("Enter your job title: ").lower().strip()
    #Now will check if email, phone and job are null, if are null, the save will continue, the same and if they are not null, the save will continue.
    if personal_details["Email"]=="" or personal_details["Phone"]=="" or personal_details["Job"]=="":
        save_personal_details()
        return
    save_personal_details()



def edit_wallet_details_testing_function():
    """Edit the details of a wallet, for terminal use."""
    print("Current Wallet Details:")
    for key, value in personal_details.items():
        print(f"{key}: {value}")
    
    field_to_edit = input("Enter the field you want to edit (Wallet Name, Name, Email, Phone, Job): ").strip().lower()
    
    if field_to_edit in personal_details:
        new_value = input(f"Enter new value for {field_to_edit.capitalize()}: ").strip()
        personal_details[field_to_edit] = new_value
        save_personal_details()
    else:
        print("Invalid field. Please try again.")

def add_expense_testing_function():
    """Add a new expense entry, for terminal use."""    
    amount=input("Enter expense amount: " + "$")
    description=input("Enter expense description: ").lower().strip()
    if not amount.isdigit():
        print("Invalid expense amount. Please enter a numeric value.")
        return
    save_to_expense_dict(amount, description)

def remove_expense(amount, description):
    """Remove an expense entry using passed data."""
    try:
        amount = int(amount)
    except ValueError:
        print("Invalid expense amount.")
        return

    for entry in expenses:
        if entry["Expense"] == amount and entry["Description"].lower().strip() == description.lower().strip():
            expenses.remove(entry)
            print(f"Removed expense: {amount}$ with description: {description}")
            return
    print("No matching expense found.")

def add_subscription_testing_function():
    """Add a new subscription, for terminal use."""
    amount = input("Enter subscription amount: " + "$")
    description = input("Enter subscription description: ").lower().strip()
    if not amount.isdigit():
        print("Invalid subscription amount. Please enter a numeric value.")
        return
    save_to_subscription_dict(amount, description)

def remove_subscription(amount, description):
    """Remove an existing subscription using passed data."""
    try:
        amount = int(amount)
    except ValueError:
        print("Invalid subscription amount.")
        return

    for entry in subscriptions:
        if entry["Subscription"] == amount and entry["Description"].lower().strip() == description.lower().strip():
            subscriptions.remove(entry)
            print(f"Removed subscription: {amount}$ with description: {description}")
            return
    print("No matching subscription found.")

def remove_subscription_testing_function():
    """Remove an existing subscription, only for console use."""
    subscription_description = input("Enter the description of the subscription to remove: ").lower().strip()
    amount = input("Enter the amount of the subscription to remove: " + "$")
    if not amount.isdigit():
        print("Invalid subscription amount. Please enter a numeric value.")
        return
    amount = int(amount)
    # Check if the subscription exists
    for entry in subscriptions:
        if entry["Subscription"] == amount and entry["Description"] == subscription_description:
            subscriptions.remove(entry)
            print(f"Removed subscription: {amount}$ with description: {subscription_description}")
            return
    print(f"No subscription found with description: {subscription_description} and amount: {amount}$")


def add_target_testing_function():
    """Add a new financial target, for terminal use."""
    target_amount = input("Enter the target amount: " + "$")
    description = input("Enter the target description: ").lower().strip()
    if not target_amount.isdigit():
        print("Invalid target amount. Please enter a numeric value.")
        return
    financial_targets.append({"Target": int(target_amount), "Description": description})
    print(f"Financial target of {target_amount}$ added with description: {description}")


def remove_target_testing_function():
    """Remove an existing financial target, for terminal use."""
    target_description = input("Enter the description of the target to remove: ").lower().strip()
    target_amount = input("Enter the amount of the target to remove: " + "$")
    if not target_amount.isdigit():
        print("Invalid target amount. Please enter a numeric value.")
        return
    target_amount = int(target_amount)
    # Check if the target exists
    for entry in financial_targets:
        if entry["Target"] == target_amount and entry["Description"] == target_description:
            financial_targets.remove(entry)
            print(f"Removed financial target: {target_amount}$ with description: {target_description}")
            return
    print(f"No financial target found with description: {target_description} and amount: {target_amount}$")

def total_income():
    """Calculate the total income."""
    total=count_the_incomes()
    print("Total income is: " + str(count_the_incomes()) + "$")
    return total

def total_outcome():
    """Calculate the total expenses."""
    total=count_the_expenses()
    print("Total expenses are: " + str(count_the_expenses()) + "$")
    return total

def save_incomes_to_json():
    """Save the incomes to a JSON file."""
    with open('incomes.json', 'w') as file:
        json.dump(incomes, file, indent=4)
    print("Incomes saved to incomes.json")

def save_subscriptions_to_json():
    """Save the subscriptions to a JSON file."""
    with open('subscriptions.json', 'w') as file:
        json.dump(subscriptions, file, indent=4)
    print("Subscriptions saved to subscriptions.json")

def save_targets_to_json():
    """Save the financial targets to a JSON file."""
    with open('financial_targets.json', 'w') as file:
        json.dump(financial_targets, file, indent=4)
    print("Financial targets saved to financial_targets.json")

def save_expenses_to_json():
    """Save the expenses to a JSON file."""
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=4)
    print("Expenses saved to expenses.json")

def save_repeating_incomes_to_json():
    """Save the repeating incomes to a JSON file."""
    with open('repeating_incomes.json', 'w') as file:
        json.dump(repeating_incomes, file, indent=4)
    print("Repeating incomes saved to repeating_incomes.json")

def save_personal_details_to_json():
    """Save the personal details to a JSON file."""
    with open('personal_details.json', 'w') as file:
        json.dump(personal_details, file, indent=4)
    print("Personal details saved to personal_details.json")

def day():
    """ A day function for inputting the repeating income. """
    day = input("Enter the day of the month for the repeating income: ")
    try:
        day = int(day)
        if 1 <= day <= 31:
            return day
        else:
            print("Invalid day. Please enter a number between 1 and 31.")
            return None
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return None
    
def count_the_incomes():
    """Count the total incomes."""
    total_income = sum(entry["Income"] for entry in incomes)
    total_repeating_income = sum(entry["Income"] for entry in repeating_incomes)
    total = total_income + total_repeating_income
    return total

def count_the_expenses():
    """Count the total expenses."""
    total_expenses = sum(entry["Expense"] for entry in expenses)
    total_subscriptions = sum(entry["Subscription"] for entry in subscriptions)
    total_expenses += total_subscriptions
    return total_expenses

def load_incomes_from_json():
    """Load incomes from a JSON file."""
    try:
        with open('incomes.json', 'r') as file:
            global incomes
            incomes = json.load(file)
        print("Incomes loaded from incomes.json")
    except FileNotFoundError:
        print("No incomes file found. Starting with an empty income list.")

def load_expenses_from_json():
    """Load expenses from a JSON file."""
    try:
        with open('expenses.json', 'r') as file:
            global expenses
            expenses = json.load(file)
        print("Expenses loaded from expenses.json")
    except FileNotFoundError:
        print("No expenses file found. Starting with an empty expense list.")

def load_subscriptions_from_json():
    """Load subscriptions from a JSON file."""
    try:
        with open('subscriptions.json', 'r') as file:
            global subscriptions
            subscriptions = json.load(file)
        print("Subscriptions loaded from subscriptions.json")
    except FileNotFoundError:
        print("No subscriptions file found. Starting with an empty subscription list.")


def load_repeating_incomes_from_json():
    """Load repeating incomes from a JSON file."""
    try:
        with open('repeating_incomes.json', 'r') as file:
            global repeating_incomes
            repeating_incomes = json.load(file)
        print("Repeating incomes loaded from repeating_incomes.json")
    except FileNotFoundError:
        print("No repeating incomes file found. Starting with an empty repeating income list.")

def load_personal_details_from_json():
    """Load personal details from a JSON file."""
    global personal_details
    try:
        with open('personal_details.json', 'r') as file:
            data = json.load(file)
            if isinstance(data, dict):
                personal_details = data
            else:
                personal_details = {}
        print("Personal details loaded from personal_details.json")
    except FileNotFoundError:
        print("No personal details file found. Starting with an empty personal details dictionary.")
        personal_details = {}
        save_personal_details_to_json()  # Create an empty file if it doesn't exist




def remove_income_testing_function():
    """Remove an existing income entry, only for console use."""
    income_description = input("Enter the description of the income to remove: ").lower().strip()
    amount =(input("Enter the amount of the income to remove: " + "$"))
    if not amount.isdigit():
        print("Invalid income amount. Please enter a numeric value.")
        return
    amount = int(amount)
    # Check if the income exists
    for entry in incomes:
        if entry["Income"] == amount and entry["Description"] == income_description:
            incomes.remove(entry)
            print(f"Removed income: {amount}$ with description: {income_description}")
            return
    print(f"No income found with description: {income_description} and amount: {amount}$")


def remove_expense_testing_function(): 
    """Remove an existing expense entry, only for console use."""  
    expense_description = input("Enter the description of the expense to remove: ").lower().strip()
    amount = input("Enter the amount of the expense to remove: " + "$")
    if not amount.isdigit():
        print("Invalid expense amount. Please enter a numeric value.")
        return
    amount = int(amount)
    # Check if the expense exists
    for entry in expenses:
        if entry["Expense"] == amount and entry["Description"] == expense_description:
            expenses.remove(entry)
            print(f"Removed expense: {amount}$ with description: {expense_description}")
            return
    print(f"No expense found with description: {expense_description} and amount: {amount}$")


def remove_repeating_income_testing_function():
    """Remove an existing repeating income entry, only for console use."""
    repeating_income_description = input("Enter the description of the repeating income to remove: ").lower().strip()
    amount = input("Enter the amount of the repeating income to remove: " + "$")
    if not amount.isdigit():
        print("Invalid repeating income amount. Please enter a numeric value.")
        return
    amount = int(amount)
    day = input("Enter the day of the month for the repeating income to remove: ")
    if not day.isdigit():
        print("Invalid day. Please enter a numeric value.")
        return
    day = int(day)
    
    # Check if the repeating income exists
    for entry in repeating_incomes:
        if (entry["Income"] == amount and entry["Description"].lower().strip() == repeating_income_description.lower().strip() and 
        entry["Day"] == day):
            repeating_incomes.remove(entry)
            print(f"Removed repeating income: {amount}$ with description: {repeating_income_description} on day {day}")
            return
    print(f"No repeating income found with description: {repeating_income_description}, amount: {amount}$ and day: {day}.")