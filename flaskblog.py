from flask import Flask
import os
import socket

app = Flask(__name__)
counter=0
app.debug = True
@app.route('/')
def hello():
    return str(counter) 

@app.route('/stat')
def stat():
    global counter
    counter += 1
    return str(counter)

@app.route('/about')
def about():
    html = "<h3>Hello!</h3>"\
           "<b>Hostname:</b> {hostname}<br/>"

   
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())


if(__name__ == '__main__'):
    app.run(debug=True,host='0.0.0.0',port=5000)
 # docker-compose up --build 
 #  links :http://localhost:5000/about
           # http://localhost:5000/
           #http://localhost:5000/stat

