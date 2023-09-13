spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # names = []
    # for spicy_food in spicy_foods:
    #     names.append(spicy_food['name']) 
    # return names
    return [spicy_food['name'] for spicy_food in spicy_foods]
    

def get_spiciest_foods(spicy_foods):
    # spiciest_food = []
    # for spicy_food in spicy_foods:
    #     if spicy_food['heat_level'] > 5:
    #         spiciest_food.append(spicy_food)
    # return spiciest_food
    return [spicy_food for spicy_food in spicy_foods if spicy_food['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        print(f'{spicy_food["name"]} ({spicy_food["cuisine"]}) | Heat Level: {"🌶" * spicy_food["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if cuisine == spicy_food['cuisine']:
            return spicy_food

def print_spiciest_foods(spicy_foods):
    # for spicy_food in spicy_foods:
    #     if spicy_food['heat_level'] > 5:
    #         print(f'{spicy_food["name"]} ({spicy_food["cuisine"]}) | Heat Level: {"🌶" * spicy_food["heat_level"]}')
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)


def get_average_heat_level(spicy_foods):
    heat_levels = [spicy_food['heat_level'] for spicy_food in spicy_foods]
    return (sum(heat_levels) / len(heat_levels))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

# print_spicy_foods(spicy_foods)
# print(get_spicy_food_by_cuisine(spicy_foods, 'Thai'))
# print(print_spiciest_foods(spicy_foods))
print(get_average_heat_level(spicy_foods))