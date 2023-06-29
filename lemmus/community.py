from collections import defaultdict
from .defaults import _API_BASE_URL, _API_VERSION
from .lemmus import Lemmus

class Community():
    
    def __init__(self, lemmus: Lemmus):
        self._leemus = lemmus
        self._user_communities = defaultdict(dict)

    def getall(self, type: str = "Subscribed") -> dict:
        """Get list of currently subscribed communites"""
        payload = { 
            'type_': type,
            'auth': self._leemus._auth.token,
            'limit': 50,
            'page': 1
        }
            
        # iterate over each page if needed
        fetched = 50 #max limit
        while fetched == 50:
            try:
                resp = self._leemus._requestor._req("community/list", params=payload)
                fetched = len(resp.json()['communities'])
                payload['page'] += 1

                for comm in resp.json()['communities']:
                    id = comm['community']['id']
                    url = comm['community']['actor_id']
                    self._user_communities[url]['id'] = id
            except Exception as err:
                print(f"error: {err}")
        
        return self._user_communities
    
    def subscribe(self, communities: dict = None) -> None:
        """Subscribe to a community. It will first attempt to resolve community."""
        if communities:
            self._user_communities = communities
        else:
            self.getall()

        payload = {
            'community_id': None,
            'follow': True,
            'auth': self._leemus._auth._token
        }

        for url,cid in self._user_communities.items():
            try: 
                # resolve community first
                comm_id = self.resolve(url)
                
                if comm_id:
                    payload['community_id'] = comm_id
                    self._println(2, f"> Subscribing to {url} ({comm_id})")
                    resp = self._leemus._requestor._req(
                        "community/follow",
                        json=payload, method='POST')
                    
                    if resp.status_code == 200:
                        self._println(3, f"> Succesfully subscribed to {url} ({comm_id})")
            except Exception as e:
                print(f"Failed to subscribe {e}")
                raise

    def resolve(self, community: str) -> int | None:
        """resolve a community"""
        payload = {
            'q': community,
            'auth':self._auth_token
        }

        community_id = None
        try:
            resp = self._leemus._requestor._req("resolve_object",params=payload)
            community_id = resp.json()['community']['community']['id']
        except Exception as e:
            print(f"Failed to resolve community {e}")
            raise

        return community_id