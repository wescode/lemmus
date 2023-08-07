import lemmus


class Admin:
    def __init__(self, lemmus: "lemmus.Lemmus"):
        self._lemmus = lemmus

    def purge_person(self, person_id: int, reason: str) -> None:
        """Purge a person"""

        payload = {
            "person_id": person_id,
            "reason": reason,
            "auth": self._lemmus._auth.token,
        }

        try:
            r = self._lemmus._requestor._req("admin/purge/person", "POST", json=payload)
            if r.status_code == 200:
                return r
        except Exception:
            raise

    def purge_community(self):
        pass

    def purge_post(self):
        pass

    def purge_comment(self):
        pass
