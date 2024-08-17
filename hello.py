from flask import Flask, render_template

#create a flask instance 
app = Flask(__name__)

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