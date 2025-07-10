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
    return redirect(url_for('income_expenses'))

@app.route('/add_expense', methods=['POST'])
def add_expense():
    """ Handle the form submission for adding expenses. """
    amount= request.form['amount']
    description= request.form['description']
    functionality.save_to_expense_dict(amount, description)
    functionality.save_expenses_to_json()
    return redirect(url_for('income_expenses'))


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)