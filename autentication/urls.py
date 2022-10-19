from django.urls import path
from . import views
urlpatterns=[
path('login_users',views.login_users,name='login'),
path('',views.register_user,name='register'),
path('logout',views.logout_user,name='logout'),
]