input_data = filter(None, open('day_21/input.txt').read().split('\n'))

def parse_food(line):
    ingredients, allergens = line.split('(contains ')
    allergens = set(map(lambda a: a.strip(), allergens.strip(')').split(',')))
    ingredients = set(map(lambda i: i.strip(), ingredients.split()))
    return (ingredients, allergens)

def find_potential_allergenic_ingredients(foods):
    allergens_to_ingredients = {}
    for ingredients, allergens in foods:
        for a in allergens:
            if a in allergens_to_ingredients:
                allergens_to_ingredients[a].intersection_update(ingredients)
            else:
                allergens_to_ingredients[a] = set(ingredients)
    return allergens_to_ingredients

def find_all_ingredients(foods):
    all_ingredients = set()        
    for ingredients, allergens in foods:
        all_ingredients.update(ingredients)
    return all_ingredients

def find_non_allergens(all_ingredients, allergens_to_ingredients):
    non_allergens = set(all_ingredients)
    for allergen, ingredients in allergens_to_ingredients.items():
        non_allergens.difference_update(ingredients)
    return non_allergens

def count_in_foods(ingredients: set, foods):
    total_count = 0
    for f in foods:
        total_count += len(ingredients.intersection(f[0]))
    return total_count

foods = list(map(parse_food, input_data))
all_ingredients = find_all_ingredients(foods)
allergens_to_ingredients = find_potential_allergenic_ingredients(foods)
non_allergens = find_non_allergens(all_ingredients, allergens_to_ingredients)

print(str(count_in_foods(non_allergens, foods)))


def find_allergens(non_allergens, allergens_to_ingredients):
    done = set(non_allergens)
    todo = set(allergens_to_ingredients.keys())
    allergens = []
    while len(todo) > 0:
        for allergen, ingredients in allergens_to_ingredients.items():
            potentials = ingredients.difference(done)
            if len(potentials) == 1:
                ingredient = potentials.pop()
                allergens.append((allergen, ingredient))
                done.add(ingredient)
                todo.remove(allergen)
    return allergens

allergens = find_allergens(non_allergens, allergens_to_ingredients)
allergens.sort()

print(','.join([ai[1] for ai in allergens]))
