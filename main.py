from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import InputRequired,Length
from flask import Flask
import pyrebase
from getpass import getpass
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import Flask, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import Form, BooleanField, TextField, validators,PasswordField
from passlib.hash import sha256_crypt
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from firebase_admin import auth

from flask import request, redirect
import string
import random
import time

from flask import Flask, jsonify, render_template, request
import webbrowser
import time
from firebase_admin import credentials, firestore, initialize_app


firebaseConfig={
    "apiKey": "AIzaSyA83vlzicIwgWoEAmL_53zg5upUTtS7uPc",
    "authDomain": "ihubems-3dcee.firebaseapp.com",
    "databaseURL": "https://ihubems-3dcee.firebaseio.com",
    "projectId": "ihubems-3dcee",
    "storageBucket": "ihubems-3dcee.appspot.com",
    "messagingSenderId": "991844903084",
    "appId": "1:991844903084:web:3c3019f2b06fb100afd709",
    "measurementId": "G-8KN2R969GZ"
    }
firebase=pyrebase.initialize_app(firebaseConfig)
app = Flask(__name__)
app.config["SECRET_KEY"]="WDRFdwdcffefg"
from flask_mail import Mail,Message
app=Flask(__name__)
app.config["SECRET_KEY"]="WDRFdwdcffefg"
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'amitsorde011@gmail.com'
app.config['MAIL_PASSWORD'] = '7888888889'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] ='"ihub" <noreply@example.com>'
app.config["MAIL_DEBUG"]=True
mail = Mail(app)


cred = credentials.Certificate("ihubems-3dcee-firebase-adminsdk-1h52n-39ec34e394.json")
default_app=initialize_app(cred)
db = firestore.client()
user=db.collection('employee')





@app.route('/')
def student():
    name=[]
    docs=user.get()
    for doc in docs:
        d=doc.to_dict()
        try:
            name.append(d)            
        except:
            print("no name means error")        
    return render_template('employ.html', resultt=name)

@app.route('/result',methods = ['POST', 'GET'])
def result():
    data={}
    aadhaar={}
    if request.method == 'POST':
        result = request.form
        
        #aadhaar["Gender"]={"Gender":result["gender"]}
        aadhaar["Aadhaar"]={"Number":result["Aadhaar"]}
        aadhaar["Birthday"]={"birthday":result["Date of birth"]}
        aadhaar["Address"]={"Address":result["address"]}
        aadhaar["Dashboard"]={"Details":result["Details"],
                              "Certifications":result["Certifications"],
                              "performance":result["performance"],
                              "Tranings":result["Tranings"],
                              }
        aadhaar["Exprience"]={"City":result["City"],
                              "Country":result["Country"],
                              "Designation":result["Designation"],
                              "Form Date":result["From Date"],
                              "To Date":result["To Date"],
                              "Organization":result["organisation"],
                              "STatus":result["STatus"]
                              }
        
        aadhaar["Master_data"]={"Base Location":result["Base location"],
                               "Confirmed":result["Confirmed"],
                               "Current Location":result["Current Location"],
                               "Delivery Manager":result["Delivery Manager"],
                               "Delivery Unit":result["Delivery Unit"],
                               "Designation":result["Designation"],
                               "Department":result["Department"],
                               "Department":result["Department"],
                               "First Name":result["First Name"],
                               "Middel Name":result["Middle Name"],
                               "Reporting Manager":result["Reporting Manager"],
                               "Role":result["Role"],
                               "Team":result["Team"],
                                "Email":result["Email"]}
        aadhaar["pan"]={"No.":result["No."]}
        aadhaar["Passport"]={"Date of Expiry":result["Date of Expiry"],
                             "Pasport Number":result["Pasport Number"]}
        aadhaar["pernonal_Identity_information"]={"Date of Birth":result["Date of Birth"],
                                                   "Disability":result["Disability"],
                                                   "Gender":result["Gender"],
                                                   "Marital Status":result["Marital Status"],
                                                   "Nationality":result["Nationality"],
                                                   "Place of Birth":result["Place of Birth"],
                                                   "State":result["State"]}
        aadhaar["project"]={"From Date":result["From Date"],
                            "To Date":result["To Date"],
                            "Project code":result["Project code"],
                            }
        aadhaar["Qualification"]={"Additional Info":result["Additional Info"],
                                  "Branch":result["Branch"],
                                  "Collage Name":result["Collage Name"],
                                  
                                  "Location":result["Location"],
                                  "passing year":result["passing year"],
                                  "Qualification":result["Qualification"],
                                  "University":result["University"]
                                  }
        ad1={"Address Line 1":result["presentAddress line 1"],
                                                       "Address Line 2":result["presentAddress line 2"],
                                                       "Address Line 3":result["presentAddress line 3"],
                                                       "Area":result["address"],
                                                       "City":result["presentCity"],
                                                       "Full Name":result["presentfull"],
                                                       "Langitude":result["presentLangitude"],
                                                       "Latitude":result["presentLatitude"],
                                                       "Pincode":result["presentPincode"],
                                                       "State":result["presentstate123"],
                                                       }
        ad2={"Address Line 1":result["permanentAddress line 1"],
                                                       "Address Line 2":result["permanentAddress line 2"],
                                                       "Address Line 3":result["permanentAddress line 3"],
                                                       "Area":result["permanentaddress"],
                                                       "City":result["permanentCity"],
                                                       "Full Name":result["permanentfull"],
                                                       "Langitude":result["permanentLangitude"],
                                                       "Latitude":result["permanentLatitude"],
                                                       "Pincode":result["permanentPincode"],
                                                       "State":result["permanentstate"],
                                                       }

                                            
        ad3={"Address Line 1":result["EergencyAddress line 1"],
                                                       "Address Line 2":result["EergencyAddress line 2"],
                                                       "Address Line 3":result["EergencyAddress line 3"],
                                                       "Area":result["Eergencyaddress"],
                                                       "City":result["EergencyCity"],
                                                       "Full Name":result["Eergencyfull"],
                                                       "Langitude":result["EergencyLangitude"],
                                                       "Latitude":result["EergencyLatitude"],
                                                       "Pincode":result["EergencyPincode"],
                                                       "State":result["Eergencystate"],
                                                       }
        
        
        aadhaar["Address"]={"Address Type":{"Present":ad1,"Permanent":ad2,"Emergency":ad3}}
        
        user.add(aadhaar)        
    return render_template("employ.html")


@app.route('/process',methods = ['POST'])
def result2():
    data={}
    projects=[]
    users_ref = db.collection('employee')
    docs = users_ref.get()
    for doc in docs:
        d=doc.to_dict()
        idd=doc.id
        data[idd]=d        
    return jsonify(data)

@app.route('/<guest>')
def delete(guest):
    
    user = db.collection('employee').document(guest)
    user.delete()
    
    return render_template("employ.html")

@app.route('/updat')
def delete12():    
    return render_template("employ.html")



@app.route('/edit/<save1>',methods = ['POST', 'GET'])
def update(save1):
    print(save1)
    aadhaar={}
    if request.method == 'POST':
        result = request.form
       
        aadhaar["Aadhaar"]={"Number":result["Aadhaar"]}
        aadhaar["Birthday"]={"birthday":result["Date of birth"]}
        aadhaar["Address"]={"Address":result["address"]}
        aadhaar["Dashboard"]={"Details":result["Details"],
                              "Certifications":result["Certifications"],
                              "performance":result["performance"],
                              "Tranings":result["Tranings"],
                              }
        aadhaar["Exprience"]={"City":result["City"],
                              "Country":result["Country"],
                              "Designation":result["Designation"],
                              "Form Date":result["From Date"],
                              "To Date":result["To Date"],
                              "Organization":result["organisation"],
                              "STatus":result["STatus"]
                              }
        
        aadhaar["Master_data"]={"Base Location":result["Base location"],
                               "Confirmed":result["Confirmed"],
                               "Current Location":result["Current Location"],
                               "Delivery Manager":result["Delivery Manager"],
                               "Delivery Unit":result["Delivery Unit"],
                               "Designation":result["Designation"],
                               "Department":result["Department"],
                               "Department":result["Department"],
                               "First Name":result["First Name"],
                               "Middel Name":result["Middle Name"],
                               "Reporting Manager":result["Reporting Manager"],
                               "Role":result["Role"],
                               "Team":result["Team"],
                                "Email":result["Email"]}
        aadhaar["pan"]={"No.":result["No."]}
        aadhaar["Passport"]={"Date of Expiry":result["Date of Expiry"],
                             "Pasport Number":result["Pasport Number"]}
        aadhaar["pernonal_Identity_information"]={"Date of Birth":result["Date of Birth"],
                                                   "Disability":result["Disability"],
                                                   "Gender":result["Gender"],
                                                   "Marital Status":result["Marital Status"],
                                                   "Nationality":result["Nationality"],
                                                   "Place of Birth":result["Place of Birth"],
                                                   "State":result["State"]}
        aadhaar["project"]={"From Date":result["From Date"],
                            "To Date":result["To Date"],
                            "Project code":result["Project code"],
                            }
        aadhaar["Qualification"]={"Additional Info":result["Additional Info"],
                                  "Branch":result["Branch"],
                                  "Collage Name":result["Collage Name"],
                                  
                                  "Location":result["Location"],
                                  "passing year":result["passing year"],
                                  "Qualification":result["Qualification"],
                                  "University":result["University"]
                                  }
        print(aadhaar)
        field = {
            "Master data":123344
            }
       
        user = db.collection('employee').document(save1)
        user.update(aadhaar)

    return render_template("update.html",result="ok")











#################send the password#############################################


def send_password(user,passs,email,massage):
    for ema ,pas in zip(user,passs):
        msg=Message(massage,sender=email, recipients =[ema])
        msg.body=pas
        mail.send(msg)
        

#######################generate id  and password###############################


password=[]
def generate_password(email):
    def id_generator(size=6, chars=string.ascii_uppercase + string.digits+string.ascii_lowercase):
        return ''.join(random.choice(chars) for _ in range(size))
    for i in range(0,len(email)):
        idd=id_generator()
        password.append(idd)
    return password


    
##########################creare the  account##################################

def create_account_in_firebase(password,emailid):
    for passs, user in zip(password,emailid):
        try:
            user = auth.create_user_with_email_and_password(user, passs)
        except:
            return("user name is already there",user)




######################################################################################
from firebase import firebase
firebase=firebase.FirebaseApplication("https://ihubems-3dcee.firebaseio.com/" ,None)
def data(x,x1):
    emailid=[]
    for i in x:
        emailid.append(x1[i]["person"])
    return emailid
#######################################################################################


@app.route('/clear' ,methods=["GET","POST"])
def clear():
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://ihubems-3dcee.firebaseio.com/', None)
        #result = firebase.post('/phonebook',data)
    firebase.delete('/','phonebook')
    return render_template("employ.html")











#########################################################################################
@app.route('/admin' ,methods=["GET","POST"])
def rsend():
    if request.method == 'POST':
        email=request.form["name"]
        massage=request.form["password"]
        result1=firebase.get('/phonebook','')
        emailid=data(result1.keys(),result1)
        
        password=generate_password(emailid)
        create_account_in_firebase(password,emailid)
        try:
            send_password(emailid,password,email,massage)
            return render_template("employ.html", retur="all the message is send")
        except:
            return render_template("employ.html", retur="data base maybe not clear")
            
        
    return render_template("employ.html")
        
#####################################################################################

@app.route('/send' ,methods=["GET","POST"])
def rsend1():
    email=request.form
    print(email)
   
    massage="ok"
    result1=firebase.get('/phonebook','')
    emailid=data(result1.keys(),result1)
    
    password=generate_password(emailid)
    error=create_account_in_firebase(password,emailid)
    
    send_password(emailid,password,email,massage)
    return jsonify({"data":error})





if __name__ == '__main__':
   app.run(debug = True)
