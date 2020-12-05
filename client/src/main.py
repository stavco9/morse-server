import os
import socket
import logging
from time import sleep, time
from controllers import check_morse_result

def test_server(server_url, text):

    # A flag that indicates if the server is reachable
    server_reachable = False

    # The test result of the last test
    test_result = False

    # Timer
    t_end = time() + 30
    counter = 1

    while time() < t_end:

        # Get the test result
        test_result = check_morse_result(server_url=server_url, text=text)
        
        # When the test Passed at the first time, then we know the server is reachable
        if not server_reachable and test_result:
            server_reachable = True
        # If the test passed before and now it is not passing, immidiately exit with error
        elif server_reachable and not test_result:
            return False

        if test_result:
            logging.info("{} time: test has been passed".format(str(counter)))
        else:
            logging.error("{} time: test has been failed".format(str(counter)))

        counter+=1

        sleep(5)
    
    # If the last test has been failed or the server is not reachable
    if not test_result or not server_reachable:
        return False
    
    return True

def main(server_url):
    ip_addr = socket.gethostbyname(socket.gethostname())
    
    if not test_server(server_url, ip_addr):
        exit(1)

    exit(0)

 
if __name__ == "__main__":
    server_url = os.getenv("SERVER_URL", "http://localhost:5000")
    logging.getLogger().setLevel(logging.INFO)

    main(server_url)