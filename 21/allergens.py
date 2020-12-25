from collections import defaultdict

lines = open("input","r").readlines()
foods = []

all_allergens = set()
all_ingredients = set()
ingredient_counts = defaultdict(int)

for line in lines:
    ingredients, allergens = line.split(" (contains")
    ingredients = ingredients.strip().split(" ")
    allergens = [s.strip() for s in allergens.strip()[:-1].split(",")]
    ingredients, allergens = set(ingredients), set(allergens)
    foods.append((ingredients, allergens))
    all_allergens |= allergens
    all_ingredients |= ingredients
    for i in ingredients:
        ingredient_counts[i] += 1

allergen_ingredients = { a: set(all_ingredients) for a in all_allergens }

for (fi, fa) in foods:
    for a in fa:
        allergen_ingredients[a] &= fi

safe_ingredients = set(all_ingredients)
for a in allergen_ingredients:
    ai = allergen_ingredients[a]
    safe_ingredients.difference_update(set(ai))

print(sum(map(lambda i: ingredient_counts[i], safe_ingredients)))