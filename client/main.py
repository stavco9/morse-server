import os
import json
from requests import Request, Session
import socket
import logging
import morse_talk as morse

def get_request(url, params):
    session = Session()

    req = Request('GET', url, params=params).prepare()

    try:
        server_result = session.send(req, timeout=1)
    except:
        logging.error("Could not reach the website {}".format(url))
        
        return None

    return server_result


def main():
    server_url = "http://localhost:9000" #os.getenv("SERVER_URL")
    server_uri = "morse-code"

    ip_addr = socket.gethostbyname(socket.gethostname())
    
    server_result = get_request(url="{}/{}".format(server_url, server_uri), params={"text": ip_addr})

    if not server_result:
        exit(1)
    elif (not server_result.json()['status'] or  server_result.status_code != 200):
        logging.error("Cannot get morse code from server")

        exit(1)
    else:
        morse_result = server_result.json()['result']

        if ip_addr != morse.decode(morse_result):
            logging.error("Morse response not match the excepted result")

            exit(1)

        exit(0)
 
if __name__ == "__main__":
    main()