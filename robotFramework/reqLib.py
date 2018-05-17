import requests  
from robot.api import logger  
  
  
class reqLib(object):  
	# ROBOT_LIBRARY_SCOPE = 'TEST CASE'
	# ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    # ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):  
        self.session = requests.Session()  
        self.response = None  
  
    def _send(self, method, url, params=None, data=None, headers=None, files=None):  
        """ 
        send request. 
        """  
        req = requests.Request(method, url, params=params, data=data, headers=headers, files=files)  
        prepped = self.session.prepare_request(req)  
        logger.info('= <request params> = \n'+str(params))  
        logger.info('= <request data> = \n'+str(data))  
        self.response = self.session.send(prepped)  
        logger.info('= <response code> = \n'+str(self.response.status_code))  
        logger.info('= <response content> = \n'+str(self.response.content))  
        return self.response  
  
    def get(self, url, **params):  
        """ 
        send get request 
 
        Params: 
        | url | request url| 
        | params | query args dict | 
 
        Return: response object 
        """  
        # params = self._add_public_para(**params)  
        # url = self._handle_url(url)  
        self.response = self._send('GET', url, params=params)  
        return self.response  
  
    def post(self, **params):  
        """ 
        send post request 
 
        Params: 
        | url | request url| 
        | params | body args dict | 
 
        Return: response object 
        """  
        # params = self._add_public_para(**params)

        self.response = self._send('POST', url, data=params) 
        return self.response 
    def check_status_code(self, code): 
        """ 
        check response http code 
        Params: 
        | code | expected http code | 
        Examples: 
        | check_status_code | 400 | """ 
        assert int(code) == self.response.status_code, 'The expected code is {}, actually {}'.format(code, self.response.status_code)