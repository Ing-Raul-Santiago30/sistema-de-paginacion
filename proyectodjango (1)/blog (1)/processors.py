from blog. models import Category, Article

# hacer consultas y subconsultas en django como si fuera codigo sql
def get_categories(request):
    # hacer un consulta en la base de datos 
    categories_in_use = Article.objects.filter(public=True).values_list('categories', flat=True)

# para solo mostrar paginas visibles con el filter el guin bajo guion bajo para hacer mas interaciones en django
    categories =Category.objects.filter(id__in=categories_in_use).values_list('id', 'name')

    return{
        'categories': categories,
        'ids': categories_in_use
    }