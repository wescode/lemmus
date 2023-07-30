import lemmus


class User:
    
    def __init__(self, lemmus: 'lemmus.Lemmus'):
        self._lemmus = lemmus
        self.id: str = None
        self.name: str = None
        self.isbanned: bool = None
        self.actor_id: str = None
        self.admin: bool = None
        self.isbot: bool = None
        self.deleted: bool = None
        self.instance_id: int = None

    def ban(self, person_id: int, ban: bool, remove_data: bool, reason: str,
            expires: int = None) -> None:
        """Ban a user"""
        payload = {
            'person_id': person_id,
            'ban': ban,
            'remove_data': remove_data,
            'expires': expires,
            'reason': reason,
            'auth': self._lemmus._auth.token
        }

        try:
            r = self._lemmus._requestor._req("user/ban", 'POST', json=payload)
            if r.status_code == 200:
                return r
        except Exception:
            raise

    def banned(self):
        """Get list of banned users"""
        payload = {
            'auth': self._lemmus._auth.token
        }

        try:
            r = self._lemmus._requestor._req("user/banned", params=payload)
            if r.status_code == 200:
                print(f"{r.json()}")
        except Exception:
            raise
    
    def get(self, person_id: int = None, username: str = None,
            sort: str = None, page: int = 1, limit: int = 50,
            community_id: int = None, saved_only: bool = None) -> dict:
        """Get a users details"""

        payload = {
            'person_id': person_id,
            'username': username,
            'sort': sort,
            'page': page,
            'limit': limit,
            'community_id': community_id,
            'saved_only': saved_only
        }
        
        try:
            r = self._lemmus._requestor._req("user", 'GET', params=payload)
            if r.status_code == 200:
                self.id = r.json()['person_viewd']['person']['id']
                self.name = r.json()['person_view']['person']['name']
                self.isbanned = r.json()['person_view']['person']['banned']
                self.actor_id = r.json()['person_view']['person']['actor_id']
                self.admin = r.json()['person_view']['person']['admin']
                self.isbot = r.json()['person_view']['person']['bot_account']
                self.deleted = r.json()['person_view']['person']['deleted']
                self.instance_id = r.json()['person_view']['person']\
                    ['instance_id']
                return r.json()
        except KeyError as e:
            raise
        except Exception as e:
            print(f"Failed to get user details {e}")
