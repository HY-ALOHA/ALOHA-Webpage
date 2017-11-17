from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignin')
def showSignin():
    return render_template('signin.html')
    
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run()
