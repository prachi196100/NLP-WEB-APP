from flask import Flask,render_template,request, redirect,session
#render_template= load the html files so in return we have string so rather than this
                    # we will return the login.html
import  api
from db import Database


dbo = Database()
app=Flask(__name__)
@app.route("/")
def index():
   # return "<h1 style='color:green'>Prachi Patel Bharatbhai<h1>"
    return render_template('login.html ')

@app.route('/register')
def register():
    return render_template('register.html')




@app.route('/perform_registration',methods=['post']) #Called when in register.html someone clicks on register then all the data will come in post request
def perform_registration():
    name=request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    response=dbo.insert(name,email,password)
    if response==1:
        return render_template("login.html",message="Registration Successful! Kindly login to proceed.")  #Agar succesfully registred then redirect to login form
    else:
        return  render_template("register.html",message="Email already registered.")#If login form exsist then show email already exsisted


@app.route('/perform_login',methods=['post'])
def perform_login():
    given_email = request.form.get('email')
    given_password = request.form.get('password')
    response=dbo.search(given_email,given_password)
    if response:
        session['logged_in']=1
        return  redirect('/profile')
    else:
        return render_template('login.html',message="Incorrect Email or Password")

@app.route('/profile')
def profile():
    if session['logged_in']==1: #If user is logged in then only show profile.html
        return render_template('profile.html')
    else:
       return redirect('/')  #Else redirect to the home page
@app.route('/ner')
def ner():
    if session['logged_in'] == 1:
         return render_template('ner.html')
    else:
        return redirect('/')

@app.route('/perform_ner',methods=['post'])
def perform_ner():
  if session['logged_in'] == 1:
    text=request.form.get('ner_text')
    response=api.ner(text) #Now api.py mathi textbox ma je text hase ae aavse
    print(response)


    return  render_template('ner.html',response=response) #This will show the result in the ner.html page only
  else:
      return redirect('/')

app.run(debug=True)
# WE HAVE TAKEN DATA FROM REGISTER.HTML ---> APP.PY ---> STORE IT IN THE JSON FILE
