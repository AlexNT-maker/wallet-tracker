import matplotlib.pyplot as plt
import os

def create_pie_chart(income, expenses, balance):
    """Create a pie chart and save it as an image with transparent background."""
    labels = ['Income', 'Expenses', 'Balance']
    sizes = [income, expenses, balance]

    # Avoid division by zero
    if sum(sizes) == 0:
        sizes = [1, 1, 1]

    fig, ax = plt.subplots(figsize=(6, 6), facecolor='black')  #Black background for the chart
    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        textprops={'color': 'white'}
    )
    ax.set_title("Financial Overview", color='white')
    ax.axis('equal')

    plt.tight_layout()
    plt.savefig("static/images/pie_chart.png", transparent=True)  # Transparent background at PNG
    plt.close()
