from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model  = Note
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'Write your note here...',
                'rows': 8,
                'cols': 40,
            }),
        }