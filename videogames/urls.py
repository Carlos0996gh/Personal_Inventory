from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('add/', views.add, name = 'add'),
    path('insert/', views.insert, name = 'insert'),

    path('edit/<int:id>', views.edit, name = 'edit'),
    path('update/<int:id>', views.update, name = 'update'),

    path('item/<int:id>', views.item, name = 'item')
    
]