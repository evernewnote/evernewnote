from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('exterior/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('main/', views.main_view, name='main'),
    path('edit_note/', views.edit_note, name='edit'),
    path('new_note/', views.new_note, name='new'),
    path('edit_note/<note_id>', views.edit_note, name='edit'),
    path('edit_note/', views.page_not_found, name='no_note'),
]
