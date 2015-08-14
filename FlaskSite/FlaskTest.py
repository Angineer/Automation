from flask import Flask, render_template, request
import relayCommands

# Create a flask app instance
app = Flask(__name__)

# Mapping for relay pin numbers
pinMap = {1:4, 2:17, 3:27, 4:22}

# Bind app URLs to python functions
# Homepage
@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method=='POST':
        reqValue=request.form['button1']

        if reqValue=='On':
            relayCommands.oneOn(pinMap[1])

        if reqValue=='Off':
            relayCommands.oneOff(pinMap[1])

    return render_template('index.html')

if __name__ == "__main__":
#    app.debug=True
    app.run(host='0.0.0.0')
