from django.http import HttpResponse
from django.shortcuts import render, reverse

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
    'invisibility_potion': {
        'Призрачная поганка': 1,
        'Солнечник': 1,
        'Хрустальная колба': 1,
    }
    # можете добавить свои рецепты ;) - ОК
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def home_view(request):
    pages = {}
    for key, value in DATA.items():
        pages[key.replace('_', ' ')] = reverse('recipes', args=[key])
    return render(request, 'home.html', {'pages': pages})


def recipes(request, recipe):
    servings = request.GET.get('servings')
    recipe = DATA.get(recipe)
    if servings:
        try:
            recipe = {k: v*int(servings) for k, v in recipe.items()}
        except ValueError:
            pass
    return render(request, 'index.html', {'recipe': recipe})
