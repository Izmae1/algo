from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def mainPg():
    return render_template('main.html')

@app.route('/about')
def aboutPg():
    return render_template('about.html')
@app.route('/contact')
def contactPg():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()