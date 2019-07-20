from django.db import models


# TODO: use django-taggit to manage tags for Notes

# Remember to run python manage.py makemigrations and then migrate when making changes!


# First pass at Note model
class Note(models.Model):
    username = models.CharField(max_length=30)
    text = models.CharField(max_length=300)  # TODO: use more appropriate type
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username + ' said ' + self.text


# First pass at Notebook model
# One notebook to many notes
class Notebook(models.Model):
    username = models.CharField(max_length=30)
    title = models.CharField(max_length=25)
    notes = models.ForeignKey(Note, on_delete=models.CASCADE, blank=True, null=True)  # ok to have no notes

    def __str__(self):
        return self.username + "'s notebook: " + self.title

# NOTE: User is a built-in model in Django, which means it's not included in
# models.py since it automatically comes with Django "for free". It has the
# following fields:


# class User:
#    username
#    first_name
#    last_name
#    password
#    email
