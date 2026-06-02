from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('works/', views.worksPage, name='works'),
    path('feedback/', views.feedbackPage, name='feedback'),
    path('blog/', views.blogPage, name='blog'),
]