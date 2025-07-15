from flask import Flask, render_template, request, redirect, url_for
import functionality
from charts import generate_pie_chart

# Create a Flask application instance
app = Flask(__name__)

@app.route('/')
def home():
    """ Render the home page with a form to input a URL. """
    return render_template('welcome.html')

@app.route('/why_track')
def why_track():
    """ Render the 'Why Track' page. """
    return render_template('why_track.html')

@app.route('/dashboard')
def dashboard():
    """ The dashboard page that displays the tracking results. """
    income= functionality.total_income()  
    expenses= functionality.total_outcome()  
    
    # If income or expenses are None, set them to 0
    # This ensures that the pie chart can be generated without errors
    if income is None:
        income = 0
    if expenses is None:
        expenses = 0
    

    balance= income - expenses

    if (
        income is None or expenses is None or balance is None or
        not isinstance(income, (int, float)) or
        not isinstance(expenses, (int, float)) or
        not isinstance(balance, (int, float)) or
        income + expenses + balance == 0
    ):
        message = "No data available yet. Start tracking your income and expenses!"
        return render_template("dashboard.html", message=message)
    
    # Generate the pie chart with the financial data
    generate_pie_chart(income, expenses, balance)

    return render_template('dashboard.html', message=None)

@app.route('/income_expenses')
def income_expenses():
    """Render the income and expenses page with a form to input data."""
    return render_template('income_expenses.html')

@app.route('/add_income', methods=['POST'])
def add_income():
    """Handle the form submission for adding income."""
    amount = request.form['amount']
    description = request.form['description']
    functionality.save_to_dict(amount, description)
    functionality.save_incomes_to_json()
    return redirect(url_for('income_expenses', message="Income added successfully!"))

@app.route('/add_expense', methods=['POST'])
def add_expense():
    """ Handle the form submission for adding expenses. """
    amount= request.form['amount']
    description= request.form['description']
    functionality.save_to_expense_dict(amount, description)
    functionality.save_expenses_to_json()
    return redirect(url_for('income_expenses', message="Expense added successfully!"))

@app.route('/add_repeating_income', methods=['POST'])
def add_repeating_income():
    """Add a repeating income entry."""
    amount= request.form['amount']
    description= request.form['description']
    day= request.form['day']

    if not amount.isdigit() or not day.isdigit():
        return "Invalid input. Amount and day must be numeric.", 400
    
    functionality.save_to_repeating_dict(amount, description, int(day))
    return redirect(url_for('income_expenses', message="Repeating income added successfully!"))

@app.route('/remove_repeating_income', methods=['POST'])
def remove_repeating_income():
    """Remove a repeating income entry."""
    amount = request.form['amount']
    description = request.form['description']
    day = request.form['day']

    if not amount.isdigit() or not day.isdigit():
        return "Invalid input. Amount and day must be numeric.", 400
    
    functionality.remove_repeating_income(amount, description, day)
    functionality.save_repeating_incomes_to_json()
    return redirect(url_for('income_expenses', message="Repeating income removed successfully!"))

@app.route('/remove_income', methods=['POST'])
def remove_income():
    """Remove an income entry."""
    amount = request.form['amount']
    description = request.form['description']
    functionality.remove_income(amount, description)
    functionality.save_incomes_to_json()
    return redirect(url_for('income_expenses', message="Income removed successfully!"))

@app.route('/remove_expense', methods=['POST'])
def remove_expense():
    """Remove an expense entry."""
    amount = request.form['amount']
    description = request.form['description']
    functionality.remove_expense(amount, description)
    functionality.save_expenses_to_json()
    return redirect(url_for('income_expenses', message="Expense removed successfully!"))

@app.route('/subscriptions')
def subscriptions():
    """Render the subscriptions page with the current subscriptions."""
    return render_template('subscriptions.html',
                            subscriptions=functionality.subscriptions) # Pass the subscriptions data to the template

@app.route('/add_subscriptions', methods=['POST'])
def add_subscriptions():
    """Add a subscription."""
    amount = request.form['amount']
    description = request.form['description'].lower().strip()

    if not amount.isdigit():
        return "Invalid input. Amount must be numeric.", 400
    
    functionality.save_to_subscription_dict(amount, description)
    functionality.save_subscriptions_to_json()

    return redirect(url_for('subscriptions', message="Subscription added successfully!"))


@app.route('/remove_subscription', methods=['POST'])
def remove_subscription():
    amount = request.form['amount']
    description = request.form['description'].lower().strip()

    if not amount.isdigit():
        return "Invalid input. Amount must be numeric.", 400
    
    functionality.remove_subscription(amount, description)
    functionality.save_subscriptions_to_json()
    
    return redirect(url_for('subscriptions', message="Subscription removed successfully!"))

@app.route('/financial_targets')
def financial_targets():
    """Render the financial targets page"""
    message=request.args.get('message') # Get the message from the query parameters
    return render_template('financial_targets.html', targets=functionality.financial_targets, message = message)

@app.route('/add_target', methods=['POST'])
def add_target():
    """ Add a new financial target"""
    target_amount= request.form['target_amount']
    description= request.form['description'].lower().strip()
   
    if not target_amount.isdigit():
        return "Invalid target amount. Please enter a numeric value.", 400
    functionality.financial_targets.append({"Target": int(target_amount), "Description": description})
    functionality.save_targets_to_json()
    
    return redirect(url_for('financial_targets', message="Target added successfully!"))

@app.route('/remove_target', methods=['POST'])
def remove_target():
    """ Remove a financial target"""
    target_amount = request.form['target_amount']
    description = request.form['description'].lower().strip()

    for entry in functionality.financial_targets:
        if entry["Target"] == int(target_amount) and entry["Description"].lower().strip() == description:
            functionality.financial_targets.remove(entry)
            functionality.save_targets_to_json()
            break  # Stop after removing the matching entry

    functionality.save_targets_to_json()
    return redirect(url_for('financial_targets', message="Target removed successfully!"))
    




if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)