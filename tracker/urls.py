from django.urls import path
from . import views
from .views import AddPost,Updat_task,Delete_task
urlpatterns=[
path('add_task/',AddPost.as_view(),name='add_t'),
path('update_task/<int:pk>',Updat_task.as_view(),name='update_t'),
path('delete_task/<int:pk>',Delete_task.as_view(),name='delete_t'),
path('view',views.list_view,name='view'),

]