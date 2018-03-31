from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.comments_list),
    path('comment/<id>/', views.comment_id)
]
