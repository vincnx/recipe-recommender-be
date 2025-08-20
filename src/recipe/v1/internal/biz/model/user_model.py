from typing import List, TypedDict

from bson import ObjectId


TypeUser = TypedDict('TypeUser', {
    '_id': ObjectId,
    'collections': List[str],
    'email': str,
    'name': str,
    'picture': str,
})
