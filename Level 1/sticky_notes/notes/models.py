from django.db import models

class Note(models.Model):
    """Represents a single sticky note with a title and freeform content."""
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[:50]
