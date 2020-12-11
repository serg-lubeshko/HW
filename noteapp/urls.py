from django.urls import path

from noteapp.views import *

urlpatterns = [
    path('', index, name="home"),
    path('regisry/', registry, name='registry'),
    path('login/', user_login, name='login'),
    path('logaut/', user_logaut, name='logaut'),
    path('category/add_category/', add_category, name='addcategory'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('one_note/<int:note_id>/', get_one_note, name='onenote'),
    path('view_note/<int:note_id>/', view_note, name='viewnote'),
    path('note/add_note/', add_note, name='addnote'),

]
