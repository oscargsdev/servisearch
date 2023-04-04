from django.urls import path
from . import views

app_name = 'classified'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('register/', views.register, name='register'),
    path("success/", views.success, name="success")
]
