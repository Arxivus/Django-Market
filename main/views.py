from django.shortcuts import render
from .models import WorksImages, Post, Review

def home(request):
    return render(request, 'index.html')


def worksPage(request):
    models = WorksImages.objects.all().order_by('-uploaded_at')
    return render(request, 'works.html', {'models': models})

def feedbackPage(request):
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'feedback.html', {'reviews': reviews})

def blogPage(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'blog.html', {'posts': posts})