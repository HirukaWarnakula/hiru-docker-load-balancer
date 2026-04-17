import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    container_id = os.environ.get('HOSTNAME')
    return f'<h1>Load Balancing in Action,Hiruka! 🚀</h1><p>Served by Container ID: <b>{container_id}</b></p>'
    
if __name__== "__main__":
    app.run(host="0.0.0.0", port=5000)


    