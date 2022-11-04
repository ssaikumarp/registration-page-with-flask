from flask import Flask, render_template,request


app = Flask(__name__)

@app.route('/')
@app.route('/register')
def registrationpage():
    return render_template('register.html')

@app.route("/success",methods=['POST','GET'])
def success():
      if request.method=='POST':
            a=request.form.get('username')
            b=request.form.get('email')
            c=request.form.get('phonenumber')
            return render_template('success.html',username=a,email=b,phonenumber=c)

if __name__ == "__main__":
    app.run(debug = True)