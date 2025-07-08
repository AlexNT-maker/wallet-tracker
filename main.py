from flask import Flask, render_template, request, redirect, url_for
import functionality

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


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)