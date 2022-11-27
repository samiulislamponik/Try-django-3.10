from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_search_view, name='article_search_view'),
    path('create/', views.article_create_view, name='article_create_view'),
    path('<int:id>/', views.article_details, name='article_details'),
]