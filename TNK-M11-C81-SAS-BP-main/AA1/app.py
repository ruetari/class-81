from flask import Flask, render_template, request
# Import datetime from datetime

import os

STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True


@app.route("/", methods= ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template('index.html')
    else:
        sender = request.form.get("sender")
        receiver = request.form.get("receiver")
        amount = request.form.get("amount")
       
        # datetime object containing current date and time
        

        # Add date key in the blockData
        blockData = { 
                "sender": sender, 
                "receiver": receiver, 
                "amount": amount
                
            }

        return render_template('index.html', blockData = blockData)



if __name__ == '__main__':
    app.run(debug = True, port=4000)