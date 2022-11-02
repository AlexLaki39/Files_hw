# Задание 1
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


print('=' * 79)
# Задание 2


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


print('=' * 79)
# Задание 3

with open('sorted/1.txt', 'r', encoding='utf-8') as file1, \
     open('sorted/2.txt', 'r', encoding='utf-8') as file2,\
     open('sorted/3.txt', 'r', encoding='utf-8') as file3,\
     open('sorted/resul.txt', 'a+', encoding='utf-8') as file_result:
    def lines_file(file_):
        '''
        Считывает строки из файла и вставляет в начало название файла
         и количество строк в нём.
        '''
        line_file = file_.readlines()
        file_info = ['\n' + file_.name + '\n', str(len(line_file)) + '\n']
        return file_info + line_file

    list_files = [lines_file(file1), lines_file(file2), lines_file(file3)]
    r = sorted(list_files, key=len)
    result_text = r[0] + r[1] + r[2]
    for line in result_text:
        file_result.write(line)
