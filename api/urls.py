from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.comments_list, name='comments_list'),
    path('comment/<id>/', views.comment_id, name='comment_id'),
    path('comment/add/', views.comment_add, name='comment_add'),
]
