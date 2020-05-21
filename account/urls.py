from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('sign/', views.sign, name='sign'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('user/', views.user, name='user'),
    path('delete/', views.delete, name='delete'),
    path('change_password/', views.change_password, name='change_password'),

    url(r'^nop/$', views.Nop.as_view(), name='nop'),
]