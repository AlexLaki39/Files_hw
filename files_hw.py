with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        num_ingredients = int(file.readline())
        ingredients = []
        for _ in range(num_ingredients):
            ingr = file. readline().strip().split(' | ')
            ingredient_name, quantity, measure = ingr
            ingredients.append({'ingredient_name': ingredient_name,
                                'quantity': quantity,
                                'measure': measure
                                })
        file.readline()
        cook_book[dish_name] = ingredients

print(cook_book)

