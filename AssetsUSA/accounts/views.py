from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import JsonResponse

# Create your views here.

@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'accounts/note_list.html', {'notes': notes, 'form': NoteForm()})

@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'id': note.id,
                    'text': note.text,
                    'created_at': note.created_at.strftime('%Y-%m-%d %H:%M')
                })
            return redirect('accounts:note_list')
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = NoteForm()
    return render(request, 'accounts/note_form.html', {'form': form})

@login_required
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('accounts:note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'accounts/note_form.html', {'form': form})

@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('accounts:note_list')
    return render(request, 'accounts/note_confirm_delete.html', {'note': note})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home:home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
