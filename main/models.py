from django.db import models

class WorksImages(models.Model):
    name = models.CharField(max_length=100, blank=True, verbose_name="Название")
    image = models.ImageField(upload_to='images/', verbose_name="Изображение") 
    uploaded_at = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Модель приманки"
        verbose_name_plural = "Модели приманок"


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст поста")
    date_posted = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-date_posted']
        
    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(verbose_name="Текст отзыва")
    image = models.ImageField(upload_to='reviews/', blank=True, null=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    status = models.BooleanField(default=False, verbose_name="Опубликован")
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']
        
    def __str__(self):
        return self.text[:50] + "..." if len(self.text) > 50 else self.text