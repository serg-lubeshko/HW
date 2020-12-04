from django.shortcuts import render, get_object_or_404

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
