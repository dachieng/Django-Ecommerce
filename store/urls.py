from django import views
from django.urls import path
from store import views

app_name = "store"
urlpatterns = [
    path("",views.products, name="products"),
    path("book/<slug:slug>/",views.product_detail, name="detail"),
    path("book-category/<slug:slug>/",views.category_list, name="categories-list")
]

