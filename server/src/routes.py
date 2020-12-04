from flask import Blueprint, request, jsonify
from controllers import translate_text_to_morse

api = Blueprint('api', __name__)

@api.route('/', defaults={'path': ''})
@api.route('/<path:path>')
def homepage(path):
    return jsonify(
        error = "Cannot get /{}".format(path)
    ), 404

@api.route("/health")
def health():
    return jsonify(
        status = True,
        message = "Server is up"
    ), 200

@api.route("/morse-code")
def translate():
    text = request.args.get('text')

    if not text:
        return jsonify(
            status = False,
            error = "Please provide a text parameter to your request"
        ), 400

    morse_response =  translate_text_to_morse(text)

    if morse_response:
        return jsonify(
            status = True,
            result = morse_response
        ), 200
    else:
        return jsonify(
            status = False,
            error = "We can't translate your text to morse code now"
        ), 500

