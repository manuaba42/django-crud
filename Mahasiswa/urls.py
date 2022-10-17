from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_mahasiswa, name='create-mahasiswa'),
    path('', views.retrieve_mahasiswa, name='retrieve-mahasiswa'),
    path('update/<int:pk>', views.update_mahasiswa, name='update-mahasiswa'),
    path('delete/<int:pk>', views.delete_mahasiswa, name='delete-mahasiswa'),
]
