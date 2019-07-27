from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('exterior/', views.home, name='home'),
    path('new_note/', views.new_note, name='new'),
    path('edit_note/<note_id>', views.edit_note, name='edit'),
    path('edit_note/', views.page_not_found, name='no_note'),
    path('view_note/<note_id>', views.view_note, name='view_note'),
    path('save_note/<note_id>', views.save_note, name='save_note'),
    path('delete_note/<note_id>', views.delete_note, name='delete_note'),
    path('new_notebook/', views.new_notebook, name='new_notebook'),
    path('edit_notebook/<notebook_id>', views.edit_notebook, name='edit_notebook'),
    path('delete_notebook/<notebook_id>', views.delete_notebook, name='delete_notebook')
]