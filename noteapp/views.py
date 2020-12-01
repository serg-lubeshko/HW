from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *


def index(request):
    notes = Note.objects.all()
    maincategories = MainCategory.objects.all()
    categories = Category.objects.all()
    # res = ""
    # for i in notes:
    #     res = res+f'<div>\n<p>{i.title}</p>\n<p>{i.created_at}</p>\n<p>{i.is_published}</p>\n<hr></div>'
    # return HttpResponse(res)

    return render(request, template_name="noteapp/index.html", context={'notes': notes,
                                                                        'title': "Список заметок",
                                                                        'maincategories': maincategories,
                                                                        'categories': categories,

                                                                        })

# Create your views here.
