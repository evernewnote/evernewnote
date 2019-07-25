from django.db import models
from evernewnote import config

from ckeditor.fields import RichTextField

# TODO: use django-taggit to manage tags for Notes

# Remember to run python manage.py makemigrations and then migrate when making changes!


# First pass at Notebook model
class Notebook(models.Model):
    user = models.ForeignKey(
        config.base.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.user.username + "'s notebook: " + self.title


# First pass at Note model
# Many notes to one notebook
class Note(models.Model):
    user = models.ForeignKey(
        config.base.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100, default="<No title>")
    text = models.CharField(max_length=400, blank=True, null=True)  # TODO: use more appropriate type
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + "'s note: " + self.title


class TestNote(models.Model):
    user = models.ForeignKey(
        config.base.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=80, default="")
    content = RichTextField()

    def __str__(self):
        return str(self.id) + ":  " + self.title + " || " + self.content

# NOTE: User is a built-in model in Django, which means it's not included in
# models.py since it automatically comes with Django "for free". It has the
# following fields:


# class User:
#    username
#    first_name
#    last_name
#    password
#    email
