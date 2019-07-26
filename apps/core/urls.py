from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('main/', views.main_view, name='main'),
    path('edit_note/', views.edit_note, name='edit'),
    path('test_new_note/', views.test_new_note, name='test_new'),
    path('test_edit_note/<note_id>', views.test_edit_note, name='test_edit'),
    path('test_edit_note/', views.page_not_found, name='no_note'),
    path('<notebook>', views.choose_notebook, name='choose_notebook')
]
