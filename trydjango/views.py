from django.http import HttpResponse
from article.models import Article
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

@login_required
def home(request, *args, **kwargs):

    get_obj = Article.objects.get(id=2)

    queryset = Article.objects.all()

    context = {
        'objects': get_obj,
        'queryset': queryset, 
    }

    Html_Response = render_to_string("home.html", context = context)

    return HttpResponse(Html_Response)
    