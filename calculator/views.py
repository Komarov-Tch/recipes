from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'blue_lagoon': {
        'водка, мл': 50,
        'ликер блю кюрасао': 20,
        'спрайт': 150,
        'ананас': 30,
        'лёд': 200,
    },
}


def reciepts_view(request, reciept_name):
    dishes = int(request.GET.get('servings', '1'))
    recipe = {}

    for name, number in DATA[reciept_name].items():
        recipe[name] = number * dishes

    context = {
        'recipe': recipe
    }
    return render(request, './calculator/index.html', context=context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
