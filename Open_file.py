
class Cookbook:
    def __init__(self):
        self.cook_book = {}
        self.list_dishes = {}

    def entry_dict(self):
        while_stop = True
        with open('Book.txt', encoding='utf-8') as f:
            while while_stop:
                ing_list = []
                ing_name = f.readline().strip()
                if not ing_name:
                    break
                self.cook_book[ing_name] = ing_name
                count = f.readline()

                for _ in range(int(count)):
                    ing_dick = {}
                    ingredient = f.readline().strip()
                    ing_dick['ingredient_name'] = ingredient.split(' | ')[0]
                    ing_dick['quantity'] = ingredient.split(' | ')[1]
                    ing_dick['measure'] = ingredient.split(' | ')[2]
                    ing_list.append(ing_dick)
                self.cook_book[ing_name] = ing_list

                f.readline()
        return self.cook_book

    def get_shop_list_by_dishes(self, dishes, person_count):
        self.entry_dict()
        for dish_get in dishes:
            for dish, ingredients in self.cook_book.items():
                if dish_get == dish:
                    for ing in ingredients:
                        self.list_dishes[ing['ingredient_name']] = {'measure': ing['measure'],
                                                                    'quantity': int(ing['quantity']) * person_count}

        return self.list_dishes


# Сортировка файлов и запись
class Merging:
    def merging_files(self, *args):
        count_line_file = {}
        for file in args:
            line_count = 0
            with open(file, encoding='utf-8') as f:
                for _ in f:
                    line_count += 1
                    count_line_file[file] = line_count

        list_d = list(count_line_file.items())
        list_d.sort(key=lambda i: i[1])

        for sort_file in list_d:
            with open(sort_file[0], encoding='utf-8') as num_f:
                data = num_f.read()
            with open('sort/menge.txt', 'a', encoding='utf-8') as merge_f:
                merge_f.write(sort_file[0])
                merge_f.write('\n')
                merge_f.write(str(sort_file[1]))
                merge_f.write('\n')
                merge_f.write(data)
                merge_f.write('\n')


print(Cookbook().entry_dict())
print(Cookbook().get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
Merging().merging_files('sort/1.txt', 'sort/2.txt', 'sort/3.txt')
