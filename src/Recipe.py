"""
A Recipe that contains the its relevant data.
    id: unique identifier
    name: name of recipe
    ingredients: list of ingredients need to make recipe
    url: url to a detail website of the recipe
    time: time to make recipe
    rating: recipe rating
"""


class Recipe:
    def __init__(self, identification, name, ingredients, url, time, rating, imagine_url):
        self.identification = identification
        self.name = name
        self.ingredients = ingredients
        self.url = url
        self.time = time
        self.rating = rating
        self.imagine_url = imagine_url


"""
encodes the recipe so it can be stored in JSON format.
"""


def encode_recipe(recipe):
    if isinstance(recipe, Recipe):
        return {'id': recipe.identification,
                'name': recipe.name,
                'ingredients': recipe.ingredients,
                'url': recipe.url,
                'time': recipe.time,
                'rating': recipe.rating,
                'imagine_url': recipe.imagine_url}
    raise TypeError(f'Object {recipe} is not of type recipe')
