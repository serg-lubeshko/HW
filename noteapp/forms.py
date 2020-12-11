from django import forms
from .models import MainCategory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(max_length=10, label="Ваш пароль",
                                help_text="не боллее 10 символов",
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))





class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(max_length=10, label="Ваш пароль",
                                help_text="не боллее 10 символов (можешь скопировать для пароля: bootstrap123)",
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(max_length=10, label="Подтверждение пароля",
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NoteForm(forms.Form):
    title = forms.CharField(max_length=150, label='Название', required=False,
                            widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label='Текст', required=False,
                              widget=forms.Textarea(attrs={"class": "form-control", "rows": "5"}))
    is_published = forms.BooleanField(label='Публиковать?', initial=True)  # initial отмечает по умолчанию
    category = forms.ModelChoiceField(queryset=MainCategory.objects.all(), label='Категория',
                                      empty_label="Выберите категорию",
                                      widget=forms.Select(attrs={"class": "form-control"}))

    password = forms.CharField(max_length=8, label='Пароль для расшифровки',
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))
    photo = forms.ImageField(label='Фото', required=False)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = MainCategory
        fields = ['name', ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"})
        }
