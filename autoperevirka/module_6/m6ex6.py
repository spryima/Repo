# У вас є файл, який містить рецепти у вигляді:

# 60b90c1c13067a15887e1ae1,Herbed Baked Salmon,4 lemons,1 large red onion,2 tablespoons chopped fresh basil
# 60b90c2413067a15887e1ae2,Lemon Pancakes,2 tablespoons baking powder,1 cup vanilla-flavored almond milk,1 lemon
# 60b90c2e13067a15887e1ae3,Chicken and Cold Noodles,6 ounces dry Chinese noodles,1 tablespoon sesame oil,3 tablespoons soy sauce
# 60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese
# 60b90c4613067a15887e1ae5,State Fair Lemonade,6 lemons,1 cups white sugar,5 cups cold water
# Кожен рецепт записаний з нового рядка (не забуваємо під час вирішення завдання про кінець рядка). Кожен запис починається з первинного ключа бази даних MongoDB. Далі через кому, йде назва рецепта, а потім через кому, йде перелік інгредієнтів рецепта.

# Вам необхідно реалізувати функцію, котра буде отримувати інформацію 
# про рецепт у вигляді словника для кожної страви що шукається. Створіть 
# функцію get_recipe(path, search_id), яка повертатиме словник для 
# рецепта із зазначеним ідентифікатором MongoDB.

# Де параметри функції:

# path — шлях до файлу.
# search_id — первинний ключ MongoDB для пошуку рецепта
# Вимоги:

# Використовуйте менеджер контексту with для читання з файлу
# Якщо рецепта із зазначеним search_id у файлі немає, функція повинна повернути None
# Приклад: для файлу, вказаного вище, виклик функції у вигляді

# get_recipe("./data/ingredients.csv", "60b90c3b13067a15887e1ae4")
# Повинен знайти у файлі рядок 60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,
# 1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese 
# і повернути результат у вигляді словника такої структури:

# {
#     "id": "60b90c3b13067a15887e1ae4",
#     "name": "Watermelon Cucumber Salad",
#     "ingredients": [
#         "1 large seedless watermelon",
#         "12 leaves fresh mint",
#         "1 cup crumbled feta cheese",
#     ],
# }


def get_recipe(path, search_id):
    with open(path, 'r') as file:
        recipe_list = file.readlines()
    for line in range(len(recipe_list)):
        if search_id in recipe_list[line]:
            if recipe_list[line][-1:] == '\n':  # прибираєм '\n' в кінці рядка
                recipe_list[line] = recipe_list[line][:-1]
                print(recipe_list[line])
            recipe = recipe_list[line].split(',')   # ділимо рядок на список 
            ingredients = recipe[2:] # виділяємо інгрідієнти в окремий список

            return {
                    "id": recipe[0],
                    "name": recipe[1],
                    "ingredients": ingredients,
                    }


search_id = '60b90c3b13067a15887e1ae4'
path = '/Users/sp/Docs/Projects/autoperevirka/Module 6/test.txt'
print(get_recipe(path,search_id))
    
