from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register'),  # User registration
    path('bro/delete/<int:pk>/', views.BroDelete.as_view(), name='bro-delete'),  # Delete a Bro instance
    path('bro/', views.BroListCreate.as_view(), name='bro-list-create'),  # List/Create Bro instances
]
