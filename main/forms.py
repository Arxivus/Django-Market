from django import forms
from .models import Review

class OrderForm(forms.Form):
    contact = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ваш email'}),
        required=True
    )
    model = forms.ChoiceField(
        label='Модель',
        choices=[
            ('', 'Выберите модель'),
            ('zhuk', 'Жук'),
            ('dragon', 'Дракон'),
            ('strekoza', 'Стрекоза'),
            ('keglya', 'Кегля'),
            ('cherv', 'Червь'),
            ('plastinka', 'Пластинка'),
            ('shar', 'Шар'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    color = forms.ChoiceField(
        label='Цвет',
        choices=[
            ('', 'Выберите цвет'),
            ('machine_oil', 'Машинное масло'),
            ('emerald', 'Изумруд'),
            ('violet', 'Фиалка'),
            ('indigo', 'Индиго'),
            ('red', 'Красный'),
            ('amber', 'Янтарь'),
            ('lox', 'Lox'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    count = forms.IntegerField(
        label='Количество упаковок',
        min_value=1,
        max_value=12,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Количество упаковок'}),
        required=True
    )
    comment = forms.CharField(
        label='Комментарий',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментарий к заказу', 'rows': 4}),
        required=False,
        min_length=10,
        max_length=150
    )
    

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'image']
        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'Напишите ваш отзыв тут',
                'rows': 5,
                'minlength': 10,
                'maxlength': 100,
            }),
            'image': forms.FileInput(attrs={
                'accept': 'image/*', 
                'style': 'display: none;'
            }),
        }
        labels = {
            'text': '',
            'image': '',
        }
    
    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 10:
            raise forms.ValidationError('Отзыв должен быть не короче 10 символов')
        return text