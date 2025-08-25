from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    """Simple form to create and edit notes."""
    class Meta:
        model = Note
        fields = ["title", "content"]
