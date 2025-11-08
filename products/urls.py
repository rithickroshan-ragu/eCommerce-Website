from django.urls import path
from products import views

urlpatterns = [
    path("hello/", views.HelloViews),
    path("hello/<slug:username>", views.HelloWorld),
    path("createProduct/", views.createProduct)
]