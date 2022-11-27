from django.shortcuts import render
from article.models import Article
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def article_details(request, id=None):

    if id is not None:
        get_article = Article.objects.get(id = id)

    context = {
        'article_object': get_article,
    }
    return render(request, "article/details.html", context=context)


@login_required
def article_search_view(request):

    get_obj = None

    try:
        search_key = int(request.GET.get('q'))
    except:
        search_key = None

    if search_key is not None:
        get_obj = Article.objects.get(id = search_key)
        print(get_obj.title)

    context = {
        'article_object': get_obj
    }
    return render(request, "article/search.html", context = context)


@login_required
def article_create_view(request):

    context = {}
    if request.method == "POST":
        print(request.POST)
        title = request.POST.get('title')
        content = request.POST.get('content')
        article_object = Article.objects.create(title=title, content = content)
        context['article_obj'] = article_object
        context['created'] = True

    return render(request, "article/create.html", context=context)