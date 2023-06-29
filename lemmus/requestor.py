import requests
from time import sleep
from .defaults import _API_BASE_URL
from .lemmus import Lemmus

class Requestor():
    
    def __init__(self, lemmus: Lemmus) -> None:
        self._lemmus = lemmus
    
    def _req(self, endpoint: str,
                    method: str = 'GET',
                    params: str = None,
                    json: dict = None) -> requests.Response:
            
        self._rate_limit()

        # create full url
        endpoint = f"{self._lemmus.site_url}/{_API_BASE_URL}/{endpoint}" 

        try:
            r = requests.request(method, url=endpoint, params=params, json=json)
            r.raise_for_status()
            return r
        except requests.exceptions.HTTPError as e:
            raise
        except requests.exceptions.RequestException as e:
            raise

    def _rate_limit(self):
        sleep(1)
        