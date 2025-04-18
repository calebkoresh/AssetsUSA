from django.urls import path
from .views import note_list, note_create, signup, note_edit, note_delete

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('',    note_list,   name='note_list'),
    path('new/', note_create, name='note_create'),
    path('edit/<int:pk>/', note_edit, name='note_edit'),
    path('delete/<int:pk>/', note_delete, name='note_delete'),
] 