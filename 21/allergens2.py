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

converged = False
while not converged:
    converged = True
    for a1 in all_allergens:
        if len(allergen_ingredients[a1]) == 1:
            i = list(allergen_ingredients[a1])[0]
            for a2 in all_allergens:
                if a1 != a2:
                    if i in allergen_ingredients[a2]:
                        allergen_ingredients[a2].remove(i)
                        converged = False

ingredient_allergens = [(list(p[1])[0],p[0]) for p in allergen_ingredients.items()]
ingredient_allergens = sorted(ingredient_allergens, key=lambda p: p[1])

print(",".join(i for (i,a) in ingredient_allergens))