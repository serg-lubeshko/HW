from django.contrib.auth import login, logout
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NoteForm, CategoryForm, UserRegisterForm, UserLoginForm
from .encryption.encryption import encrypt
from .encryption.decryption import decrypt

from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import *


def registry(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()  # Сохранил в объект "пользователь", для того что б сразу не логинится
            login(request, user)  # И сразу вызвал метод Login, где приняли нашего "пользователь" и рекв.
            messages.success(request, "Вы зарегистрированы")
            return redirect("home")
        else:
            messages.error(request, "Произошла ошибка")
    else:
        form = UserRegisterForm()

    return render(request, "noteapp/registry.html", {'form': form})


def user_login(request):
    if request.method == 'POST':
        print(request.method)
        form = UserLoginForm(data=request.POST)  # Без ДАТЫ НЕ РАБОТАЕТ ПОЧЕМУ-ТО
        print(form)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Из from django.contrib.auth import login"
            print(login(request, user))
            return redirect("home")
    else:
        form = UserLoginForm()
    return render(request, "noteapp/login.html", {'form': form})


def user_logaut(request):
    logout(request)
    return redirect("home")


def index(request):
    notes = Note.objects.all()
    maincategories = MainCategory.objects.all()
    # print(notes)


    return render(request, template_name="noteapp/index.html", context={'notes': notes,
                                                                        'title': "Список заметок",
                                                                        'maincategories': maincategories,
                                                                        # 'categories': categories,
                                                                        })


# Create your views here.
def get_category(request, category_id):
    notes = Note.objects.filter(category_id=category_id)
    maincategories = MainCategory.objects.all()
    maincategory = MainCategory.objects.get(id=category_id)
    return render(request, "noteapp/category.html", {'notes': notes,
                                                     'maincategories': maincategories,
                                                     'maincategory': maincategory,
                                                     })


def get_one_note(request, note_id):
    notes = get_object_or_404(Note, id=note_id)
    # notes = Note.objects.get(id=note_id)
    maincategories = MainCategory.objects.all()
    # maincategory = MainCategory.objects.get(id=note_id)

    return render(request, "noteapp/note_one.html", {'notes': notes,
                                                     'maincategories': maincategories,
                                                     # 'maincategory': maincategory,
                                                     })


@login_required
def view_note(request, note_id):
    notes_item = get_object_or_404(Note, id=note_id)


    if request.method == "POST":
        maincategories = MainCategory.objects.all()
        a = request.POST["password_2"]
        pk = request.POST["pk"]

        cipher_text1 = notes_item.content_en
        salt1 = notes_item.salt1
        nonce1 = notes_item.nonce1
        tag1 = notes_item.tag1
        encrypted1 = {'cipher_text': cipher_text1, 'salt': salt1, 'nonce': nonce1, 'tag': tag1}
        cont = decrypt(encrypted1, notes_item.password)

        cipher_text2 = notes_item.title_en
        salt2 = notes_item.salt2
        nonce2 = notes_item.nonce2
        tag2 = notes_item.tag2
        encrypted2 = {'cipher_text': cipher_text2, 'salt': salt2, 'nonce': nonce2, 'tag': tag2}
        title_ = decrypt(encrypted2, notes_item.password)

        note_pk = Note.objects.get(id=pk)

        if a == note_pk.password:

            return render(request, "noteapp/view_one.html", {'notesitem': notes_item,
                                                             'maincategories': maincategories,
                                                             'cont': cont,
                                                             'title': title_})

        else:
            return redirect("home")



@login_required  # Если не авторизован, то не добавишь новость
def add_note(request):
    maincategories = MainCategory.objects.all()
    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():


            a_text = form.cleaned_data.get('content')  # Получил данные из запроса content
            b_text = form.cleaned_data.get('title')  # Получил данные из запроса название
            b_key = form.cleaned_data.get('password')
            post_dict = form.cleaned_data  # Получил словарь из post
            encrypt_dict = encrypt(a_text, b_key, 1)  # Получил словарь_шифр из encryption.py
            encrypt_dict_b = encrypt(b_text, b_key, 2)

            p_e_dict = {**post_dict, **encrypt_dict, **encrypt_dict_b}
            Note.objects.create(**p_e_dict)  # Распакуем в модель

            return redirect("home")

    else:
        form = NoteForm()
    return render(request, "noteapp/add_note.html", {'maincategories': maincategories,
                                                     'form': form})


def add_category(request):
    maincategories = MainCategory.objects.all()
    if request.method == "POST":

        form_category = CategoryForm(request.POST)
        if form_category.is_valid():
            # print(form_category.cleaned_data)

            category = form_category.save()
            # print(category)
            return redirect("home")

    else:
        form_category = CategoryForm()
    return render(request, "noteapp/add_category.html", {'maincategories': maincategories,
                                                         'form_category': form_category})
