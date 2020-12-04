from django.urls import path

from noteapp.views import *

urlpatterns = [
    path('', index, name="home"),
    path('category/<int:category_id>/', get_category, name='category'),
    path('one_note/<int:note_id>/', get_one_note, name='onenote'),
    path('view_note/<int:note_id>/', view_note, name='viewnote'),
]
