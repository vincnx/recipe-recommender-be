from typing import Generic, List, TypeVar, TypedDict

TypeRecipe = TypedDict('TypeRecipe', {
    'title': str,
    'ingredients': List[str],
    'instructions': str,
})

T = TypeVar("T")
class PaginatedResponse(TypedDict, Generic[T]):
    items: List[T]
    total_items: int
    page_pages: int

# class RecipeModel():
#     def __init__(self, title: str, ingredients: List[str], instructions: str):
#         self.title = title
#         self.ingredients = ingredients
#         self.instructions = instructions

#     def to_dict(self) -> TypeRecipe:
#         return {
#             'title': self.title,
#             'ingredients': self.ingredients,
#             'instructions': self.instructions,
#         }