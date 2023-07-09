from collections import defaultdict
import lemmus
from .types import ListingType


class Community():
    
    def __init__(self, lemmus: 'lemmus.Lemmus'):
        self._lemmus = lemmus
        self._user_communities = defaultdict(dict)

    def list(
            self,
            type: ListingType = None,
            sort: str = None,
            show_nsfw: bool = None,
            page: int = 1,
            limit: int = 50) -> dict:
        """Get list of communites"""
        payload = {
            'type_': type,
            'sort': sort,
            'auth': self._lemmus._auth.token,
            'limit': limit,
            'show_nfsw': show_nsfw,
            'page': page
        }
            
        # iterate over each page if needed
        fetched = 50
        while fetched == 50:
            try:
                r = self._lemmus._requestor._req("community/list",
                                                 params=payload)

                fetched = len(r.json()['communities'])
                payload['page'] += 1

                for comm in r.json()['communities']:
                    id = comm['community']['id']
                    url = comm['community']['actor_id']
                    self._user_communities[url]['id'] = id
            except Exception as err:
                print(f"{err}")
        
        return self._user_communities
    
    def follow(self, communities: dict) -> list:
        """Subscribe to a community. It will first attempt to
        resolve community.

        Return `list` of communities successfully subscribed to
        """
        payload = {
            'community_id': None,
            'follow': True,
            'auth': self._lemmus._auth.token
        }

        subscribed = []
        for url, cid in self._user_communities.items():
            try:
                # resolve community first
                comm_id = self.resolve(url)
                
                if comm_id:
                    payload['community_id'] = comm_id
                    self._println(2, f"> Subscribing to {url} ({comm_id})")
                    r = self._lemmus._requestor._req("community/follow",
                                                     json=payload,
                                                     method='POST')
                    
                    if r.status_code == 200:
                        subscribed.append(url)
            except Exception as e:
                print(f"Failed to subscribe to {url}: {e}")

        return subscribed

    def resolve(self, community: str) -> int | None:
        """resolve a community"""
        payload = {
            'q': community,
            'auth': self._auth.token
        }

        community_id = None
        try:
            r = self._lemmus._requestor._req("resolve_object", params=payload)
            community_id = r.json()['community']['community']['id']
        except Exception as e:
            print(f"Failed to resolve community {e}")
            raise

        return community_id
