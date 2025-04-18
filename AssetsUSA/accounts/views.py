from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm

# Create your views here.

@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'accounts/note_list.html', {'notes': notes})

@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('accounts:note_list')
    else:
        form = NoteForm()
    return render(request, 'accounts/note_form.html', {'form': form})
