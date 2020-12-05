import os
from flask import Flask
from routes import api

# Run the server
def main(listen_port):
    app = Flask(__name__)

    app.register_blueprint(api)

    app.run(debug=True, host="0.0.0.0", port=listen_port)
 
if __name__ == "__main__":
    listen_port = os.getenv('LISTEN_PORT', 3000)

    main(listen_port)