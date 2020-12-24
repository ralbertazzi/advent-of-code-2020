from dataclasses import dataclass
from typing import Optional


###################################
#            UTILITIES            #
###################################


@dataclass(frozen=True)
class Food:
    """
    Holds information about one entry of the problem:
    a food is a set of ingredients and a set of allergens
    """

    ingredients: set[str]
    allergens: set[str]


def can_have(ingredient: str, allergen: str) -> bool:
    """
    Returns weather an ingredient can contain a certain allergen.

    In order for an ingredient to contain a certain allergen, it must appear
    in all the foods in which the allergen appears as well. Note that the opposite
    is not always true, since sometimes allergens are omitted.
    """
    return all(
        ingredient in food.ingredients for food in foods if allergen in food.allergens
    )


###################################
#            PARSING              #
###################################

with open("data.txt") as f:
    lines: list[str] = [line.strip() for line in f.readlines()]

foods: list[Food] = []

# Parsing
for line in lines:
    ingredients, allergens = line.split(" (contains")
    foods.append(
        Food(
            ingredients=(set(ingredients.split(" "))),
            allergens=set(
                allrg.strip() for allrg in allergens.replace(")", "").split(", ")
            ),
        )
    )


###################################
#             PART 1              #
###################################

# Get a set of all ingredients in the problem
all_ingredients = set().union(*[food.ingredients for food in foods])

# Get the possible allergens for each ingredient by taking all allergens
# in which the ingredient appears
possible_allergens_for_ingredient = {
    ingredient: set().union(
        *[food.allergens for food in foods if ingredient in food.ingredients]
    )
    for ingredient in all_ingredients
}


# Here we compute the ingredients that cannot contain any allergen
ingredients_without_allergens = [
    ingredient
    for ingredient, possible_allergens in possible_allergens_for_ingredient.items()
    if not any(can_have(ingredient, allergen) for allergen in possible_allergens)
]

# Finally we compute how many times they appear in each food
part1 = sum(
    1 if ingredient in food.ingredients else 0
    for ingredient in ingredients_without_allergens
    for food in foods
)
print(part1)


###################################
#             PART 2              #
###################################

ingredients_with_allergens = list(
    all_ingredients.difference(set(ingredients_without_allergens))
)

all_allergens = set().union(*[food.allergens for food in foods])

# The remaining ingredients have the same count of the total number of allergens.
# We just need to match them.
assert len(ingredients_with_allergens) == len(all_allergens)


def solve_assignment(idx: int = 0, solution: Optional[dict[str, str]] = None):
    """
    Solves the ingredient -> allergen assignment.

    The algorithm acts as such:
    1. Take the next unassigned ingredient
    2. For each unassigned allergen that the ingredient can have
        * Add the (ingredient -> allergen) assignment to the solution
        * Go to 1 (recursively).
    3. When a solution is complete (the only solution), return it.

    The returned solution consists of a mapping ingredient -> allergen.
    """
    solution = solution or {}
    if len(solution) == len(ingredients_with_allergens):
        yield solution

    ingredient = ingredients_with_allergens[idx]
    for allergen in all_allergens - set(solution.values()):
        if can_have(ingredient, allergen):
            forward_solution = solution.copy()
            forward_solution[ingredient] = allergen
            yield from solve_assignment(idx + 1, forward_solution)


assignment = next(solve_assignment())

# Once we have the solution, apply the usually clean one-liner to get the answer
part2 = ",".join(s[0] for s in sorted(assignment.items(), key=lambda kv: kv[1]))
print(part2)
