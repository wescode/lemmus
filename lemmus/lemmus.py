from .authenticate import Authenticate
from .requestor import Requestor
from .comment import Comment
from .community import Community


class Lemmus:
    
    def __init__(self, url: str, user: str, passwd: str) -> None:
        self.site_url = url
        self.username = user
        self.password = passwd

        # requestor
        self._requestor = Requestor(self)

        # auth and store token
        self._auth = Authenticate(self)
        
        # comment
        self.comment = Comment(self)

        # community
        self.community = Community(self)