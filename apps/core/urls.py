from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('exterior/', views.home, name='home'),
    path('edit_note/', views.edit_note, name='edit'),
    path('new_note/', views.new_note, name='new'),
    path('edit_note/<note_id>', views.edit_note, name='edit'),
    path('edit_note/', views.page_not_found, name='no_note'),
    path('new_notebook/', views.new_notebook, name='new_note'),
]