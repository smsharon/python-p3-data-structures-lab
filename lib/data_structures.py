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
    foods = [f["name"]for f in spicy_foods]
    return foods

def get_spiciest_foods(spicy_foods):
    foods_dict = [f for f in spicy_foods if f["heat_level"] > 5]
    return foods_dict

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        emojis = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food ["heat_level"] > 5:
            emojis = "🌶" * food["heat_level"]
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {emojis}")

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    average = total_heat_level / len(spicy_foods)
    return int(average)

def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_foods = [food for food in spicy_foods] + [spicy_food]
    return new_spicy_foods
