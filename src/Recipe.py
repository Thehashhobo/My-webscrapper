


class Recipe:
    """
    A Recipe that contains the its relevant data.
    id: unique identifier
    name: name of recipe
    ingredients: list of ingredients need to make recipe
    url: url to a detail website of the recipe
    time: time to make recipe
    rating: recipe rating
    """
    def __init__(self, identification: int, name: str, ingredients: list[list[str]],
                 url: str, time: str, rating: int, imagine_url: str, instructions: list[str],
                 overview: str):
        self.identification = identification
        self.name = name
        self.ingredients = ingredients
        self.url = url
        self.time = time
        self.rating = rating
        self.imagine_url = imagine_url
        self.instructions = instructions
        self.overview = overview





def encode_recipe(recipe: Recipe):
    """encodes the recipe so it can be stored in JSON format."""
    if isinstance(recipe, Recipe):
        return {'id': recipe.identification,
                'name': recipe.name,
                'ingredients': recipe.ingredients,
                'url': recipe.url,
                'time': recipe.time,
                'rating': recipe.rating,
                'imagine_url': recipe.imagine_url,
                'instructions': recipe.instructions,
                'overview': recipe.overview
                }
    raise TypeError(f'Object {recipe} is not of type recipe')
