from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#create a flask instance 
app = Flask(__name__)
app.config['SECRET_KEY']="debjitt.k"


#create our form class 
class NamerForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Common WTForms Fields
# StringField
# PasswordField
# TextAreaField
# BooleanField
# RadioField
# SelectField
# SelectMultipleField
# FileField
# SubmitField
# DateField
# IntegerField
# DecimalField
# Common WTForms Validators
# DataRequired
# Email
# Length
# EqualTo
# NumberRange
# Optional
# URL
# AnyOf
# NoneOf











#create a route n decorator

@app.route('/')

#def index():
#   return "<h1>Hello, World!</h1>"
#filter 
#safe
#bold
#capitalize
#upper
#used in index.html

def index():
    favourite_pizza=['chesse', 'veg']
    return render_template("index.html",fp=favourite_pizza)

# return users 
@app.route('/user/<name>')

#def user(name):
#    return "<h1>hello {} </h1>".format(name)

def user(name ):
    return render_template("user.html", user_name=name)

# create custom error pages 

#page not found 
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


#internal server error 
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


#crete name page
@app.route('/name', methods=['GET','POST'])
def name():
    name=None
    form=NamerForm()

    #validate form
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=''
        
    return render_template("name.html",name=name,form=form)