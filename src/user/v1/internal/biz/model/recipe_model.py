from typing import Generic, List, TypeVar, TypedDict

TypeRecipe = TypedDict('TypeRecipe', {
    'title': str,
    'ingredients': List[str],
    'instructions': str,
})
