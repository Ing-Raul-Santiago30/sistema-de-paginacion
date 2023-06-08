from pages.models import Page


def get_pages(request):
# para solo mostrar paginas visibles con el filter si
    pages =Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug')

    return{
        'pages': pages
    }