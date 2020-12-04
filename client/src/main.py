import os
import json
from requests import Request, Session
import socket
import logging
import morse_talk as morse
from time import sleep

def get_request(url, params):
    session = Session()

    req = Request('GET', url, params=params).prepare()

    try:
        server_result = session.send(req, timeout=1)
    except:
        logging.error("Could not reach the website {}".format(url))
        
        return None

    return server_result

def check_morse_result(url, text):
    server_result = get_request(url=url, params={"text": text})

    if not server_result:
        return False
    elif (not server_result.json()['status'] or  server_result.status_code != 200):
        logging.error("Cannot get morse code from server")

        return False
    else:
        morse_result = server_result.json()['result']

        if text != morse.decode(morse_result):
            logging.error("Morse response does not match the excepted result")
            return False

    logging.info("Morse response matches the excepted result !!!")
    return True

def main(server_url):
    morse_endpoint = "morse-code"

    morse_full_path = (server_url + "/" + morse_endpoint)
    ip_addr = socket.gethostbyname(socket.gethostname())
    
    if not check_morse_result(morse_full_path, ip_addr):
        exit(1)

    exit(0)
 
if __name__ == "__main__":
    server_url = os.getenv("SERVER_URL", "http://localhost:5000")
    logging.getLogger().setLevel(logging.INFO)

    main(server_url)