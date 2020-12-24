from dataclasses import dataclass

from constraint import *

with open("data.txt") as f:
    lines: list[str] = [line.strip() for line in f.readlines()]


@dataclass(frozen=True)
class Food:
    ingredients: set[str]
    allergens: set[str]


foods: list[Food] = []
for line in lines:
    ingredients, allergens = line.split(" (contains")
    foods.append(
        Food(
            ingredients=(set(ingredients.split(" "))),
            allergens=set(allrg.strip() for allrg in allergens.replace(")", "").split(", ")),
        )
    )


"""
* Each allergen is found in exactly one ingredient.
* Each ingredient contains zero or one allergen.
* Allergens aren't always marked. Even if an allergen isn't listed, the ingredient that contains 
    that allergen could still be present
"""
all_allergens = set().union(*[food.allergens for food in foods])
all_ingredients = set().union(*[food.ingredients for food in foods])

# Each variable represents the concept of "ingredient X has allergen Y"
all_variables = [
    f"{allergen}_{ingredient}"
    for allergen in all_allergens
    for ingredient in all_ingredients
    if any(allergen in food.allergens and ingredient in food.ingredients for food in foods)
]

problem = Problem()

# Add all variables to the problem.
# Each variable be either 0 (ingredient X doesn't have allergen Y)
# or 1 (ingredient X has allergen Y)
problem.addVariables(all_variables, [0, 1])

# If each allergen is found in exactly one ingredient, then the sum of all variables
# related to a certain allergen must be 1 (only one variable is 1, all other variables are 0).
for allergen in all_allergens:
    variables_with_allergen = [v for v in all_variables if v.startswith(allergen)]
    problem.addConstraint(ExactSumConstraint(1), variables_with_allergen)

# If each ingredient contains zero or one allergen, then the sum of all variables
# related to a certain ingredient must be at most 1 (either it has one allergen, or it has no allergens).
for ingredient in all_ingredients:
    variables_with_ingredient = [v for v in all_variables if v.endswith(ingredient)]
    problem.addConstraint(MaxSumConstraint(1), variables_with_ingredient)

solutions = problem.getSolutions()
print(solutions)
