from django.test import TestCase
from django.urls import reverse
from notes.models import Note

class NoteViewsTests(TestCase):
    def setUp(self):
        self.note = Note.objects.create(title="First", content="alpha")

    def test_list_page_loads(self):
        url = reverse("notes:list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "First")

    def test_create_note_post(self):
        url = reverse("notes:create")
        resp = self.client.post(url, {"title": "New", "content": "Text"}, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Note.objects.filter(title="New").exists())

    def test_detail_404_for_missing(self):
        url = reverse("notes:detail", args=[123456])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)
