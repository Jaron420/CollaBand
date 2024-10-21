from django.urls import path
from . import views  # Import views from the app

urlpatterns = [
    path('home/', views.homepage, name='homepage'),  # Example view
    path('dashboard/', views.dashboard, name='dashboard'),  # Another view
]