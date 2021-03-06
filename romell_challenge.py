#############################################
#                                           #
#   WindRiver Coding Challenge              #
#   Author: Romell Aguirre Gomez            #
#                                           #
#############################################


# Importing modules
import flask, base64
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# Exception catching - Error handling for bad endpoint requests or json invalid format
@app.errorhandler(Exception) 
def handle_error(error):
    return jsonify({"Input": "", "Output": "", "Status": "error", "Message": "Wrong Endpoint or invalid JSON format, try again", "Response Code": 400})


# Web Service Home Page - Provide a simple Welcome Message
@app.route('/', methods=['GET'])
def home():
    # return simple welcome message to the application
    return "<h1>Romell's WindRiver Application</h1><h2>Please use the following endpoints: /api/encrypt, /api/decrypt, /api/health</h2>"


# Encryption method - Take json value as input and encrypt it using the encode64 method
@app.route("/api/encrypt", methods=["POST"])
def encrypt():
    # validate is the POST input is a json document, otherwise launch the exception
    if request.is_json:
        data = request.json
        for key, value in data.items():
            if not value:
                return jsonify({"Input": value, "Output": "", "Status": "error", "Message": "Value is empty, cannot encrypt it", "Response Code": 400})
            else:
                # encode64 based strategy
                message_bytes = value.encode('utf-8')
                base64_bytes = base64.b64encode(message_bytes)
                encoded_data = base64_bytes.decode('utf-8')
                return jsonify({"Input": value, "Output": encoded_data, "Status": "success", "Message": "Encryption Successful", "Response Code": 200})
    else:
        return jsonify({"Input": "", "Output": "", "Status": "error", "Message": "Json format invalid, try again", "Response Code": 400})
    

# Decryption method - Take json value encrypted generated by encrypt method as input and decrypt it using the encode64 method
@app.route("/api/decrypt", methods=["POST"])
def decrypt():
    # validate is the POST input is a json document, otherwise launch the exception
    if request.is_json:
        data = request.json
        for key, value in data.items():
            if not value:
                return jsonify({"Input": value, "Output": "", "Status": "error", "Message": "Value is empty, cannot decrypt it", "Response Code": 400})
            else:
                # decode64 based strategy 
                base64_bytes = value.encode('utf-8')
                message_bytes = base64.b64decode(base64_bytes)
                decoded_data = message_bytes.decode('utf-8')
                return jsonify({"Input": value, "Output": decoded_data, "Status": "success", "Message": "Decryption Successful", "Response Code": 200})
    else:
        return jsonify({"Input": "", "Output": "", "Status": "error", "Message": "Json format invalid, try again", "Response Code": 400})


# Health method: check the application health
@app.route('/api/health', methods=['GET'])
def health():
    # return simple message to indicate the application is up and running
    return "<h1>Application is Up and Running!</h1><h2>Please use the following endpoints: /encrypt, /decrypt, /health</h2>"


# Launch the application method, default IP was change to launch in localhost(127.0.0.1) or remote docker  by accesing the host IP and the port 5000
app.run(host="0.0.0.0", port=5000)
