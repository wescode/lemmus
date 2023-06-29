from collections import defaultdict
from .defaults import _API_BASE_URL

class Authenticate():
    
    def __init__(self, lemmus) -> None:
        self._lemmus = lemmus
        self.token = None

        # authenticate
        self._login()
    
    def _login(self) -> None:
        """authenticate to instance"""
        payload = { 
            'username_or_email': self._lemmus.username,
            'password': self._lemmus.password
        }
        
        try:
            resp = self._lemmus._requestor._req("user/login", method='POST',
                                              json=payload)
            self.token = resp.json()['jwt']
        except Exception as e:
            print(f"Authentication error: {e}")
          #raise Exception(f"Failed to authenticate: {e}")
          #self._println(1, f"[ERROR]: login() failed for {self._username} on {self._site_url}")
          #self._println(2, f"-Details: {e}")
          #sys.exit(1)