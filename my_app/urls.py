from django.urls import path

from my_app import views


urlpatterns = [
    path("", views.home_page_view, name="home_page"),
    path("articles/", views.article_list_view, name="article_list"),
]


