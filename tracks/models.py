from django.db.models import Model
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField


class Author(Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Genre(Model):
    name = models.CharField('Genre', max_length=50, null=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Track(Model):
    title = models.CharField('Title', max_length=100, null=False)
    description = models.TextField('Description', default='', max_length=1000, null=False)
    audio = models.FileField('Audio', upload_to='media/', blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    slug = AutoSlugField(populate_from='title', unique=True, db_index=True, editable=False, blank=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('tracks:track-detail', args=[self.slug])

    class Meta:
        verbose_name = 'Track'
        verbose_name_plural = 'Tracks'
