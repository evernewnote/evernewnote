from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('main/', views.main_view, name='main'),
    path('edit_note/', views.edit_note, name='edit'),
    path('test_edit_note/', views.test_edit_note, name='test_edit'),
]
