import unittest.mock as mock    
import pytest

from cocktails import *

@pytest.fixture
def fake_input():
	with mock.patch('cocktails.input') as m:
		yield m

def test_possible_cocktails_from_ingredients(fake_input):
	"""
	GIVEN a list of ingredients
	WHEN the ingredients are '7-up' and 'Salt'
	THEN check if the possible cocktails are '69 Special', 'Apple Slammer', 'Radler', 'Tequila Slammer', 'Egg-Nog - Classic Cooked', 'Lassi Khara', 'Microwave Hot Cocoa' and 'Salty Dog'

	"""

	fake_input.return_value = ['7-up','Salt']
	assert gatherPossibleDrinksForEachIngredient(fake_input.return_value) == ['69 Special', 'Apple Slammer', 'Radler', 'Tequila Slammer', 'Egg-Nog - Classic Cooked', 'Lassi Khara', 'Microwave Hot Cocoa', 'Salty Dog']

def test_common_cocktails(fake_input):
	"""
	GIVEN a list of cocktails
	WHEN the cocktails are 'Gin Toddy','Gin Fizz' and 'Gin Toddy'
	THEN check if the common cocktail is returned as 'Gin Toddy'
	
	"""

	fake_input.return_value = ['Gin Toddy','Gin Fizz', 'Gin Toddy']
	assert findCommonCocktails(fake_input.return_value) == {'Gin Toddy'}

def test_suggested_cocktail_with_multiple_ingredients(fake_input):
	"""
	GIVEN a list of ingredients 
	WHEN the ingredients are Gin,Water,Powdered sugar,Lemon peel
	THEN check if the suggested cocktail is 'Gin Toddy'
	
	"""

	fake_input.return_value = 'Gin,Water,Powdered sugar,Lemon peel'
	assert suggestCocktails(fake_input.return_value) == ['Gin Toddy']

def test_suggested_cocktail_with_multiple_ingredients_different_order(fake_input):
	"""
	GIVEN a list of ingredients 
	WHEN the ingredients are Lemon peel,Powdered sugar,Gin,Water in a different order
	THEN check if the suggested cocktail is 'Gin Toddy'
	
	"""

	fake_input.return_value = 'Lemon peel,Powdered sugar,Gin,Water'
	assert suggestCocktails(fake_input.return_value) == ['Gin Toddy']

def test_suggested_cocktail_with_ingredients_negative(fake_input):
	"""
	GIVEN a list of ingredients 
	WHEN the ingredients are Gin,Water,Powdered sugar which misses an ingredient Lemon Peel
	THEN check if no suggested cocktail is returned
	
	"""

	fake_input.return_value = 'Gin,Water,Powdered sugar'
	assert suggestCocktails(fake_input.return_value) == None

def test_suggested_cocktail_with_single_ingredient(fake_input):
	"""
	GIVEN an ingredient 
	WHEN the ingredient is 'Lemon peel'
	THEN check if no suggested cocktail is returned
	
	"""

	fake_input.return_value = 'Lemon peel'
	assert suggestCocktails(fake_input.return_value) == None

def test_suggested_cocktails_with_multiple_ingredients(fake_input):
	"""
	GIVEN a set of ingredients 
	WHEN the ingredients are 'Gin,Water,Carbonated water,Lemon,Lemon peel,Powdered sugar'
	THEN check if multiple possible cocktails are retuned
	
	"""

	fake_input.return_value = 'Gin,Water,Carbonated water,Lemon,Lemon peel,Powdered sugar'
	actual = set(suggestCocktails(fake_input.return_value))
	expected = set(['Gin Toddy','Gin Fizz'])
	assert actual == expected





