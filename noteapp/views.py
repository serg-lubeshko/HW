from django.shortcuts import render, get_object_or_404, redirect
from .forms import NoteForm, CategoryForm
from .encryption.encryption import hello

# Create your views here.
from django.http import HttpResponse
from .models import *


def index(request):
    notes = Note.objects.all()
    maincategories = MainCategory.objects.all()
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


def view_note(request, note_id):
    notes_item = get_object_or_404(Note, id=note_id)
    # notes_item = Note.objects.get(id=note_id)
    maincategories = MainCategory.objects.all()
    return render(request, "noteapp/view_one.html", {'notesitem': notes_item,
                                                     'maincategories': maincategories,
                                                     })


def add_note(request):
    maincategories = MainCategory.objects.all()
    if request.method == "POST":

        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            a_text = form.cleaned_data.get('content')  # Получил данные из запроса
            print()
            print("A равно", a_text)
            b_key = form.cleaned_data.get('password')
            print("B равно", b_key)
            c_upd = form.cleaned_data
            c_upd["content_en"] = hello()
            print(c_upd)
            Note.objects.create(**c_upd)
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
