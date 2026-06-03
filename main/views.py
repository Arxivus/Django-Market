from django.shortcuts import render, redirect
from .models import WorksImages, Post, Review
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import OrderForm, ReviewForm

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'index.html')


def worksPage(request):
    models = WorksImages.objects.all().order_by('-uploaded_at')
    return render(request, 'works.html', {'models': models})

def feedbackPage(request):
    reviews = Review.objects.filter(status=True).order_by('-created_at')
    return render(request, 'feedback.html', {'reviews': reviews})

def blogPage(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'blog.html', {'posts': posts})


""" def orderPage(request):
    return render(request, 'order.html') """


def orderPage(request):
    order_success = False
    review_success = False
    order_form = OrderForm()
    review_form = ReviewForm()
    
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        
        if form_type == 'order_form':
            order_form = OrderForm(request.POST)
            contact = request.POST.get('contact')
            model = request.POST.get('model')
            color = request.POST.get('color')
            count = request.POST.get('count')
            comment = request.POST.get('comment', '')
            
            if contact and model and color and count:
                message = f"""
                    Новый заказ!
                    Email: {contact}
                    Модель: {model}
                    Цвет: {color}
                    Количество: {count}
                    Комментарий: {comment}
                                    """
                send_mail(
                    subject=f'Новый заказ от {contact}',
                    message=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
                order_success = True
                messages.success(request, 'Заказ отправлен! Мы скоро свяжемся с вами.', extra_tags='order_success')
                return redirect('order') 
            else:
                messages.error(request, 'Заполните все поля формы заказа')
        
        elif form_type == 'review_form':
            review_form = ReviewForm(request.POST, request.FILES)
            text = request.POST.get('text')
            image = request.FILES.get('image')
            
            if text and len(text) >= 10:
                review = Review.objects.create(
                    text=text,
                    image=image,
                    status=False 
                )

                review_success = True
                messages.success(request, 'Спасибо за отзыв! Он будет опубликован после модерации.', extra_tags='review_success')
                return redirect('order')
            else:
                messages.error(request, 'Отзыв должен быть не короче 10 символов')
  
    return render(request, 'order.html', {
        'order_form': order_form,
        'review_form': review_form,
        'order_success': order_success,
        'review_success': review_success,
    })



class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        
        return response