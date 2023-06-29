import sys
from collections import defaultdict
from urllib.parse import urlparse
from .authenticate import Authenticate
from .requestor import Requestor
from .defaults import _API_BASE_URL, _API_VERSION
from .comment import Comment
from .community import Community

class Lemmus:
    
    def __init__(self, url, user, passwd) -> None:
        self._site_url = url
        self._username = user
        self._password = passwd

        # requestor
        self._requestor = Requestor(self)

        # auth and store token
        self._auth = Authenticate(self)
        
        # comment
        self.comment = Comment(self)

        # community
        self.community = Community(self)

    def _println(self, indent, line):
        print(f"{' ' * indent}{line}")