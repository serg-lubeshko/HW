from django.urls import path

from noteapp.views import *

urlpatterns = [
    path('', index),
    path('category/<int:category_id>/', get_category),
    path('one_note/<int:note_id>/', get_one_note),
]
