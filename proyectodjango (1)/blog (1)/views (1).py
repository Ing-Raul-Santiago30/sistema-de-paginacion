from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Category, Article
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def list(request):
    # sacar todos los articulos 
    articles= Article.objects.all()
    # paginar todos los articulos 
    paginator = Paginator(articles, 2)
    #recoger numero de las paginas 
    page = request.GET.get('page')
    # crear la variable para guardar todos los articulos de esa pagina
    page_articles = paginator.get_page(page)

    return render(request, 'articles/list.html',{
        'title': 'Articulos',
        'articles': page_articles

    })

    # sacar una pagina para cada categoria
@login_required(login_url="login")
def category(request, category_id):
# sacar nuestra categorias 
        # mostrar el rror 404 asi de esa forma se muestra cuando una pagina no existe
        category = get_object_or_404(Category,id= category_id)
        # sacar los articulos por categoria en una description y me muestra la informacion que yo quiera dentro de la pagina 
        #a parte del category_id tambien se le puede pasr un obkjetocompleto y tambien lo va a filtrar 
       # articles = Article.objects.filter(categories=category)
       

        return render(request, 'categories/category.html',{
            'category': category,
          #  'articles':articles
        })
@login_required(login_url="login")
def article(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    return render(request, 'articles/detail.html',{
        'article':article
    })
