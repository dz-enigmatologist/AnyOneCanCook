"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import find_the_match
##
##

def test_find_the_match():
    recipeRepo = {
        "Mango Lassi": ["Mango", "Curd"],
        "Pasta": ["Pasta", "Pasta Sauce", "Butter"],
        "BBJ": ["Butter", "Jam", "Bread"],
        "Garlic Bread": ["Garlic", "Bread"]
    }
    recipeDetails = {
        "Mango Lassi": "1. Chop mangoes and blend with sugar \n2. Serve Chilled.\n",
        "Pasta": "1. Boil pasta in pasta sauce with butter \n2. Serve Hot.\n",
        "BBJ": "1. Spread butter and jam on bread \n2. Serve Anyhow.\n",
        "Garlic Bread": "1. Spread garlic on bread and toast \n2. Serve Hot.\n"
    }

    assert "Mango Lassi" in find_the_match(recipeRepo, ["Mango", "Curd", "Pasta"], recipeDetails)
    assert "update" in find_the_match(recipeRepo, ["Mango", "Pasta"], recipeDetails)
    assert "update" in find_the_match(recipeRepo, ["salt", "sugar"], recipeDetails)