from flask import Flask, render_template, request
from twilio.rest import Client
app = Flask(__name__)

client = Client(
    "AC9947a5728fd4dfc0eeb2065dd2d200bf", 
    "enter auth token"
)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      first_name = request.form.get("Name")
      result = request.form
      print(first_name)
      client.messages.create(
          to ="+919050585522",
          from_ = "+16692018325",
          body= first_name,
      )
      return render_template("index.html",result = result)