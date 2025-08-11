from typing import List, TypedDict

TypeRecipe = TypedDict('TypeRecipe', {
    'title': str,
    'ingredients': List[str],
    'instructions': str,
})

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