from typing import Generic, List, TypeVar, TypedDict
from bson import ObjectId

TypeUser = TypedDict('TypeUser', {
    '_id': ObjectId,
    'collections': List[str],
    'email': str,
    'name': str,
    'picture': str,
})

T = TypeVar("T")
class PaginatedResponse(TypedDict, Generic[T]):
    items: List[T]
    total_items: int
    page_pages: int