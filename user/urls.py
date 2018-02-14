from rest_framework.authtoken import views
from django.urls import path
from .views import user_create

urlpatterns = [
    # path('api-token-auth/', views.obtain_auth_token),
    path('api/user_create/', user_create)
]
