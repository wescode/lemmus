import requests
from time import sleep

import lemmus
from .defaults import _API_BASE_URL


class Requestor:
    def __init__(self, lemmus: "lemmus.Lemmus") -> None:
        self._lemmus = lemmus

    def _req(self, endpoint: str, method: str = "GET", **kwargs) -> requests.Response:
        self._rate_limit()

        # create full url
        endpoint = f"{self._lemmus.site_url}/{_API_BASE_URL}/{endpoint}"

        self._prepare(kwargs)
        try:
            r = requests.request(method, url=endpoint, **kwargs)
            r.raise_for_status()
            return r
        except requests.exceptions.HTTPError as e:
            raise
        except requests.exceptions.RequestException as e:
            raise

    def _rate_limit(self):
        sleep(1)

    def _prepare(self, params: dict) -> None:
        """Remove params/json/data that have no value"""
        if params is None:
            return

        for k in list(params.keys()):
            if "params" in k or "json" in k or "data" in k:
                for sk in list(params[k]):
                    if params[k][sk] is None:
                        del params[k][sk]
