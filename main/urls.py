from django.urls import path
from .views import RegisterView
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('works/', views.worksPage, name='works'),
    path('feedback/', views.feedbackPage, name='feedback'),
    path('order/', views.orderPage, name='order'),
    path('blog/', views.blogPage, name='blog'),
    
]