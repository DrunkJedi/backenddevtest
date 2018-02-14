from django.urls import path
from . import views

urlpatterns = [
    path('api/answer/', views.answer_list),
    path('api/answer/<int:pk>/', views.answer_detail),
]
