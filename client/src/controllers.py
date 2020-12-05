from models import HTTPGetRequest
import logging
import morse_talk as morse

# Check the morse result from server by text parameter
def check_morse_result(server_url, text):

    # Build the morse code full uri
    morse_endpoint = "morse-code"
    morse_full_path = (server_url + "/" + morse_endpoint)

    # Invoke the HTTP Request
    server_result = HTTPGetRequest(url=morse_full_path, headers=None, params={"text": text}).send()

    if not server_result:
        return False
    elif (not server_result.json()['status'] or  server_result.status_code != 200):
        logging.error("Cannot get morse code from server")

        return False
    else:
        morse_result = server_result.json()['result']

        # If the text does not match the Morse Code given as a response
        if text != morse.decode(morse_result):
            logging.error("Morse response does not match the excepted result")
            return False
        else:
            logging.info("The morse code of {} is {}".format(text, morse_result))

    logging.info("Morse response matches the excepted result !!!")
    return True