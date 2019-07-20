from django.db import models
from django.contrib.auth.models import User
from evernewnote import config

# TODO: use django-taggit to manage tags for Notes

# Remember to run python manage.py makemigrations and then migrate when making changes!


# First pass at Notebook model
# One notebook to many notes
class Notebook(models.Model):
    user = models.ForeignKey(
        config.base.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=25)
    # notes = models.ForeignKey(Note, on_delete=models.CASCADE, blank=True, null=True)  # ok to have no notes

    def __str__(self):
        return self.user.username + "'s notebook: " + self.title


# First pass at Note model
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


# NOTE: User is a built-in model in Django, which means it's not included in
# models.py since it automatically comes with Django "for free". It has the
# following fields:


# class User:
#    username
#    first_name
#    last_name
#    password
#    email
