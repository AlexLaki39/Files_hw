with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        num_ingredients = int(file.readline())
        ingredients = []
        for _ in range(num_ingredients):
            ingr = file.readline().strip().split(' | ')
            ingredient_name, quantity, measure = ingr
            ingredients.append({'ingredient_name': ingredient_name,
                                'quantity': int(quantity),
                                'measure': measure
                                })
        file.readline()
        cook_book[dish_name] = ingredients

print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    dict_1 = {}
    for dish, ingred in cook_book.items():
        if dish in dishes:
            for i in ingred:
                a = i.get('ingredient_name')
                i.pop('ingredient_name')
                if a not in dict_1.keys():
                    dict_1[a] = i
                    i['quantity'] *= person_count
                else:
                    dict_1[a]['quantity'] += i['quantity']
    print(dict_1)
    return


get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)
