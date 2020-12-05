from requests import Request, Session
import logging

class HTTPGetRequest():
    def __init__(self, url, headers, params):
        self.url = url
        self.headers = headers
        self.params = params

    def send(self):
        session = Session()

        req = Request('GET', self.url, params=self.params, headers=self.headers).prepare()

        try:
            server_result = session.send(req, timeout=1)
        except:
            logging.error("Could not reach the website {}".format(self.url))
            
            return None

        return server_result