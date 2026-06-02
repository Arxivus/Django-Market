from django.shortcuts import render, redirect
from .models import WorksImages, Post, Review
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
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


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        
        return response