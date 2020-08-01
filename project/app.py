from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/pcbuilder'
db=SQLAlchemy(app)


app.config['SECRET_KEY']='pcbuilder'

class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(50), unique=False, nullable=False)
    message = db.Column(db.String(100), unique=False, nullable=False)
class Links(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    search = db.Column(db.String(100), unique=False, nullable=False)

@app.route('/',  methods=['GET', 'POST'])
def index():
    if(request.method=='POST'):
        y=0
        search=request.form.get('search')
        if(len(search) == 0):
            return render_template("index.html")
        else:
             se=Links.query.all()
             for x in se:
                if(search==x.name):
                  y=1
                  return redirect(x.search)
       
        if (y==0):
             flash("Sorry match not found")
             return render_template("index.html") 

        
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        name=request.form.get('firstname')
        email=request.form.get('email')
        message=request.form.get('subject')
        entry=Contact(name=name,email=email,message=message)
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex,email)):
            db.session.add(entry)
            db.session.commit()
            flash("MESSAGE SENT SUCCESSFULLY")
        else:
             flash("PLEASE PROVIDE A CORRECT MAIL ID")
             return render_template("contact.html")   
       
    return render_template("contact.html")



if __name__=="__main__":
 app.run(debug=True)