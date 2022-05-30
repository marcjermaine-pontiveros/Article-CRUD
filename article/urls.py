from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_article, name="list_article"),
    path('article/', views.create_article, name="create_article"),
    path('article/<int:pk>/', views.view_article, name="view_article"),
    path('article/<int:pk>/edit', views.edit_article, name="edit_article"),
    path('article/<int:pk>/delete', views.delete_article, name="delete_article"),
]
