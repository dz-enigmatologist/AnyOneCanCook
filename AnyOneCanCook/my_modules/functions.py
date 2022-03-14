"""The function for my project."""

def find_the_match(repository_dict, ingredients, recipe_detail_dict):
    """
    On recieving a specific list of elements, this function maps a repository disctionary's keys with values among the input elements to a dictionary with those key's and other values. With an example, it gives the recipe for the associated dish that could be made from the input ingredients.

    Parameters
    ----------
    repository_dict : dict
        Dictionary containing keys and associated values that can be input. (keys : values :: dish names : ingredients)
    ingredients : list
        List of input values to be associated. (ingredients)
    recipe_detail_dict : dict
        List of key values from the repository with other values. (keys : values :: dish names : recipe)

    Returns
    -------
    str
        A string of what dish can be made using the ingredients along with a recipe for it.
    
    See Also
    --------
    find_the difference : Finds the missing elements for possible association with certain key values.

    Examples
    --------
    >>> find_the_match(recipeRepo, ["Mango", "Curd", "Pasta"], recipeDetails)
    
    You could make:
    
    Mango Lassi
    *****************
    1.Chop mangoes and blend with sugar
    
    2.Serve Chilled.
    """
    output_string = "\nYou could make :\n"
    match = False
    for key, value in repository_dict.items():
        ingredientSet = []
        for item in value:
            if item in ingredients:
                ingredientSet.append(item)
                if ingredientSet == value:
                    match = True
                    output_string += "\n" + key + "\n*********************\n" + recipe_detail_dict[key]
                continue
    if match == False:
        output_string = "Time to update your recipe list or get more ingredients"

    return output_string