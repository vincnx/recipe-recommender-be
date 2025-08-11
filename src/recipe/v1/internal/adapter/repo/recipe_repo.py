import numpy as np
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
import os
import pickle
from ...biz.model.recipe_model import TypeRecipe

class RecipeRepo():
    def __init__(self):        
        self.w2v_model = None
        self.all_recipes_vector = None
        self.df_clean = None
        self._load_model()
    
    def get_recommendations(self, user_input, num_recommendations=5) -> list[TypeRecipe]:
        """Get recipe recommendations based on user input"""
        if not self.w2v_model or not self.all_recipes_vector.any():
            raise ValueError("Model not trained. Call train() first.")
            
        # Vectorize user input
        user_input_tokens = word_tokenize(user_input)
        user_input_vector = [0] * self.w2v_model.vector_size
        num_tokens = 0
        
        for token in user_input_tokens:
            if token in self.w2v_model.wv:
                user_input_vector = [a + b for a, b in zip(user_input_vector, self.w2v_model.wv[token])]
                num_tokens += 1
                
        if num_tokens > 0:
            user_input_vector = [x / num_tokens for x in user_input_vector]
            
        user_input_vector = np.array(user_input_vector).reshape(1, -1)
        similarities = cosine_similarity(user_input_vector, self.all_recipes_vector)
        
        # Get top recommendations
        top_indices = similarities.argsort()[0][-num_recommendations:][::-1]
        
        recommendations = []
        for idx in top_indices:
            recipe = {
                'title': self.df_clean['title'][idx],
                'ingredients': self.df_clean['ingredient_item'][idx],
                'instructions': self.df_clean['instructions'][idx]
            }
            recommendations.append(recipe)
            
        return recommendations
    
    def _load_model(self, model_dir='models'):
        """Load a trained model from files"""
        # TODO: add error handling if models not present

        self.w2v_model = Word2Vec.load(os.path.join(model_dir, 'word2vec.model'))
        
        # Load recipe vectors and cleaned dataframe
        with open(os.path.join(model_dir, 'recipe_vectors.pkl'), 'rb') as f:
            self.all_recipes_vector = pickle.load(f)
            
        with open(os.path.join(model_dir, 'recipes_df.pkl'), 'rb') as f:
            self.df_clean = pickle.load(f)
            
        return self