from django.test import SimpleTestCase
from notes.forms import NoteForm

class NoteFormTests(SimpleTestCase):
    def test_title_is_required(self):
        form = NoteForm(data={"title": "", "content": "x"})
        self.assertFalse(form.is_valid())
