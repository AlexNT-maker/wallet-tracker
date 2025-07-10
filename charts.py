import matplotlib.pyplot as plt
import os

def generate_pie_chart(income, expenses, balance, output_path= 'static/images/pie_chart.png'):
    """  Generate a pie chart showing income, expenses, and balance for the dashboard. 
    Parameters:
        income (int or float): Total income amount.
        expenses (int or float): Total expenses amount.
        balance (int or float): Remaining balance amount.
        output_path (str): Path to save the generated pie chart image.
    """

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    labels= ['Income', 'Expenses', 'Balance']
    sizes= [income, expenses, balance]
    colors= ['#4CAF50', '#F44336', '#2196F3']  # Green for income, red for expenses, blue for balance
    explode= (0.1, 0, 0)  # Explode the income slice for emphasis

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct= '%1.1f%%', startangle=90)
    plt.title('Financial Overview')
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()  # Close the plot to free up memory