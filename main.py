"""
Testral SMS SDK

Austrlian Telstra SMS send utlity. To apply such a service, go https://dev.telstra.com/

2016
License: MIT
"""

__version__ = "0.0.1"

import requests
from requests import RequestException
import json

REQUEST_TOKEN_URL = "https://api.telstra.com/v1/oauth/token"
REQUEST_MSG_URL = "https://api.telstra.com/v1/sms/messages"

MSG_TEMPLATE = "Hello, this is a SMS from UniversApp, thanks for using our service! https://universapp.com.au"


class TelstraSMS(object):
    """This class helps setting up the client ID, client secret key

    """

    client_id = None
    client_secret = None
    token = None

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_token(self):
        """ get the token from client id and client secret
        :return: string type of token
        """
        if self.client_id is None or self.client_secret is None:
            return "Invalid client ID or client secret key"

        # get token
        token_params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials',
            'scope': 'SMS',
        }

        try:
            r = requests.post(REQUEST_TOKEN_URL, data=token_params)
            try:
                self.token = json.loads(r.content)['access_token']
                return json.loads(r.content)['access_token']
            except TypeError as e:
                print str(e)
                pass
        except RequestException as e:
            print str(e)
            pass
        else:
            return None

    def send_sms(self, num, sms_text="Sample Text"):
        """send sms message"""

        if self.token is None:
            return "Invalid token ", self.token

        if len(num) != 10:
            return "Invalid Australian Phone number"

        headers_msg = {
            'Authorization': 'Bearer {0}'.format(self.token)
        }

        params_msg = {
            'to': num,
            'body': sms_text,
        }

        try:
            r = requests.post(REQUEST_MSG_URL, data=json.dumps(params_msg), headers=headers_msg)
            return r
        except RequestException as e:
            print str(e)










