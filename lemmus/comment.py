import lemmus


class Comment:
    def __init__(self, lemmus: "lemmus.Lemmus") -> None:
        self._lemmus = lemmus

    def get(self, post_id: str, max_depth: int = 1, limit: int = 1000) -> dict:
        """Get all comments for a Post"""
        payload = {
            "post_id": post_id,
            "max_depth": max_depth,
            "limit": limit,
        }

        try:
            r = self._lemmus._requestor._req("comment/list", params=payload)
        except Exception as e:
            self._println(2, f"> Failed to get comment list")

        return r.json()["comments"]
