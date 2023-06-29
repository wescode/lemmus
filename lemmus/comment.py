from .defaults import _API_BASE_URL
from .lemmus import Lemmus

class Comment:
    
    def __init__(self, lemmus: Lemmus):
        self._lemmus = lemmus

    def get_comments(
            self, post_id: str, max_depth: int = 1,
            limit: int = 1000) -> dict:

        payload = {
            'post_id': post_id,
            'max_depth': max_depth,
            'limit': limit,
        }

        try:
            r = self._lemmus._requestor._req("comment/list", params=payload)
        except Exception as e:
            self._println(2, f"> Failed to get comment list")

        return r.json()['comments']
