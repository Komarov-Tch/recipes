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
    'meat': {
        'свинина, кг': 0.5,
        'горчица, банка': 1,
        'яблоки, шт': 3,
        'приправы, ч.л.': 5,
    }
}


def calculate_recipes(request, dish):
    person = int(request.GET.get('servings', 1))
    context = {'recipe': {}}
    for ingridient, quanty in DATA[dish].items():
        context['recipe'][ingridient] = quanty * person
    return render(request, 'calculator/index.html', context=context)
