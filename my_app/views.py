from django.shortcuts import render

from my_app.models import Article


def home_page_view(request):
    return render(request, 'my_app/homepage.html')


def article_list_view(request):
    articles = Article.objects.filter(status=Article.Status.PB)
    context = {
        'articles': articles,
    }

    return render(
        request,
        template_name='my_app/article_list.html',
        context=context
    )


def article_detail_view(request, pk):
    article = Article.objects.get(pk=pk)

    context = {"article": article}

    return render(
        request,
        template_name='my_app/article_detail.html',
        context=context
    )
