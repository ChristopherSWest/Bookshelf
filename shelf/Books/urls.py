from django.urls import path
from . import views


app_name = "books"
urlpatterns = [
    path("", views.index, name="index"),
    path("b/<str:title>", views.title, name="title"),
    path("add", views.add, name="add"),
    path("add/<str:isbn>", views.add_title, name="add_title"),
    path("add/<str:isbn>/<str:user>/success", views.add_success, name="add_success"),
    path("<str:user>/my_books", views.my_books, name="my_books"),
    
]