from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('view/',views.view,name='view'),
    path('delete/',views.delete,name='delete'),
    path('delete/<int:emp_id>',views.delete,name='delete'),
    path('filter/',views.filter,name='filter'),
]