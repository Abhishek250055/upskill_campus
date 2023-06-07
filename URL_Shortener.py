from flask import Flask, redirect, render_template, request
import pyshorteners as st

app = Flask(__name__)


def generate_short_url(url):
    s= st.Shortener()
    short_url=s.tinyurl.short(url)
    return short_url


@app.route('/', methods=['GET', 'POST'])

def home():
    if request.method == 'POST':
        # Get the long URL from the form submission
        long_url = request.form.get('long_url')

        # Generate a unique shortened URL
        short_url = generate_short_url(long_url)

        return render_template('index.html', short_url=short_url)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
