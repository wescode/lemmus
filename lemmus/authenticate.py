import lemmus


class Authenticate:
    def __init__(self, lemmus: "lemmus.Lemmus") -> None:
        self._lemmus = lemmus
        self.token = None

        # authenticate
        self._login()

    def _login(self) -> None:
        """authenticate to instance"""
        payload = {
            "username_or_email": self._lemmus.username,
            "password": self._lemmus.password,
        }

        try:
            resp = self._lemmus._requestor._req(
                "user/login", method="POST", json=payload
            )
            self.token = resp.json()["jwt"]
        except Exception as e:
            print(f"Authentication error: {e}")
