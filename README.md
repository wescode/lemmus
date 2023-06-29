# <center> Lemmus
## <center>A python API wrapper for Lemmy
### Very much still a WIP
<br>

### Example usage

```python
from lemmus import Lemmus

lemming = Lemmus("https://sh.itjust.works", 'Username', 'password')
comments = lemming.comment.get_comments('1234')
communities = lemming.community.get_communities()
```