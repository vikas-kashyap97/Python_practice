'''
first you need to install flask module by pip install flask

and then
'''




from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()


''' 
when you run this on the terminal it will start the server and you can see the webpage on your browser by typing http://127.0.0.1:5000.
'''