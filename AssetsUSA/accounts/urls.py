from django.urls import path
from .views import note_list, note_create

app_name = 'accounts'

urlpatterns = [
    path('',    note_list,   name='note_list'),
    path('new/', note_create, name='note_create'),
] 