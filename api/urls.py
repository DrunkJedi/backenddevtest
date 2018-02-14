from django.urls import path
from . import views

app = 'api/'


urlpatterns = [
    path(app + 'login/', views.apilogin, name='api_login'),
    path(app + 'auth-token/', views.obtain_auth_token, name='api-token-auth'),
]
