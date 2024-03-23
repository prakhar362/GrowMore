from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Sign Up', methods=['POST'])
def signup():
    email = request.form['email']
    password = request.form['password']
    
    # Here you'll write the code to save the email and password to a text file
    
    return "Registration successful!"

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password= request.form['password']

    # Here you'll write the code to check if the provided email and password match the stored credentials
    
    return "Login successful!"

if __name__ == '__main__':
    app.run(debug=True)