import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

#Ex https://Itz-zaid:ghp_147bkkabcdefgh@github.com/Itz-zaid/anything
os.system("git clone https://itz-zaid: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@github.com/itz-zaid/mogenius ok && cd ok && pip3 install -U -r requirements.txt && nohup python3 -m telegram &")
