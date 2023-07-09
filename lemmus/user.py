import lemmus


class User:
    
    def __init__(self, lemmus: 'lemmus.Lemmus'):
        self._lemmus = lemmus

    def ban(
            self,
            person_id: int,
            ban: bool,
            remove_data: bool,
            reason: str,
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
            r = self._lemmus._requestor._req("user/ban",
                                             'POST', json=payload)
            if r.status_code == '200':
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
    
    def get(
            self,
            person_id: int,
            username: str,
            sort: str,
            page: int = 1,
            limit: int = 50,
            community_id: int,
            saved_only: bool) -> None:
        """Get a users details"""

