from django.test import TestCase
from notes.models import Note

class NoteModelTests(TestCase):
    def test_create_note(self):
        note = Note.objects.create(title="Test", content="Hello")
        self.assertEqual(note.title, "Test")
        self.assertEqual(note.content, "Hello")
        self.assertIsNotNone(note.id)
