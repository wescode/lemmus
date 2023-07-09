from enum import Enum
import lemmus


class ListingType(Enum):
    all = 'All'
    local = 'Local'
    subscribed = 'Subscribed'
    
class SortType(Enum):
    active = 'Active'
    hot = 'Hot'
    new = 'New'
    old = 'Old'