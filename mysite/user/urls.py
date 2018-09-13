from django.urls import path
from . import views
from .url import views as url_views

urlpatterns = [
    path('sign_in/', views.sign_in.as_view(), name='sign_in'),
    path('sign_up/', views.sign_up.as_view(), name = 'sign_up'),
    path('url/register/', url_views.registerView.as_view(), name = 'url_register'),
    path('url/list/', views.url_list, name = 'url_list'),
]
