from django.contrib.auth import login, logout
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NoteForm, CategoryForm, UserRegisterForm, UserLoginForm
from .encryption.encryption import encrypt

from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse
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
    print(notes)
    # if request.method == "POST":
    #     a = request.POST["password_2"]
    #     pk = request.POST["pk"]
    #     print(request.POST)
    #     print(a)
    #     print('ЗДЕСЬ', pk)
    #     note_pk = Note.objects.get(id=pk)
    #     # note_pk_password = note_pk[1]
    #     print("Здесь", note_pk.password)
    #     if a == note_pk.password:
    #         print("Есть")
    #         flag =True
    #         return redirect("viewnote", pk)
    #     else:
    #         print("нЕТ")
    # print("Здесь2", note_pk_password )

    # categories = Category.objects.all()
    # res = ""
    # for i in notes:
    #     res = res+f'<div>\n<p>{i.title}</p>\n<p>{i.created_at}</p>\n<p>{i.is_published}</p>\n<hr></div>'
    # return HttpResponse(res)

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
    # notes_item = Note.objects.get(id=note_id)
    maincategories = MainCategory.objects.all()
    if request.method == "POST":
        a = request.POST["password_2"]
        pk = request.POST["pk"]
        # print(request.POST)
        # print(a)
        # print('id в пост', pk)
        note_pk = Note.objects.get(id=pk)
        # note_pk_password = note_pk[1]
        # print("Здесь", note_pk.password)
        if a == note_pk.password:
            print("Есть")
            return render(request, "noteapp/view_one.html", {'notesitem': notes_item,
                                                             'maincategories': maincategories,
                                                             })
            # return redirect("viewnote", pk)
        else:
            return redirect("home")
    # return render(request, "noteapp/view_one.html", {'notesitem': notes_item,
    #                                                  'maincategories': maincategories,
    #                                                  })


@login_required  # Если не авторизован, то не добавишь новость
def add_note(request):
    maincategories = MainCategory.objects.all()
    if request.method == "POST":

        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            print("form.cleaned_datat Словарь=====", form.cleaned_data)

            a_text = form.cleaned_data.get('content')  # Получил данные из запроса content
            b_text = form.cleaned_data.get('title')  # Получил данные из запроса название
            b_key = form.cleaned_data.get('password')
            post_dict = form.cleaned_data  # Получил словарь из post
            encrypt_dict = encrypt(a_text, b_key, 1)  # Получил словарь_шифр из encryption.py
            encrypt_dict_b = encrypt(b_text, b_key, 2)

            p_e_dict = {**post_dict, **encrypt_dict, **encrypt_dict_b}
            Note.objects.create(**p_e_dict)  # Распакуем в модель

            # print()
            # print("A равно===", a_text)
            #
            # print("B равно====", b_key)
            #
            #
            # print()
            # print("encrypt_dict Словарь=====", encrypt_dict)
            # print()
            # print("encrypt_dict Словарь=====", encrypt_dict_b)
            #
            #
            # # post_dict["content_en"] = encrypt_dict['cipher_text']
            # print()
            # print(p_e_dict)

            # s = Note.objects.update(content_en="1")
            # s.save()
            # print(Note.objects.get(**form.cleaned_data))
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
            print(form_category.cleaned_data)
            # MainCategory.objects.create(**form_category.cleaned_data)
            category = form_category.save()
            print(category)
            return redirect("home")

    else:
        form_category = CategoryForm()
    return render(request, "noteapp/add_category.html", {'maincategories': maincategories,
                                                         'form_category': form_category})
