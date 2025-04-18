from django.urls import path
from .views import note_list, note_create, signup

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('',    note_list,   name='note_list'),
    path('new/', note_create, name='note_create'),
] 