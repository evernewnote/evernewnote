from django.db import models
from evernewnote import config
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

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
    title = models.CharField(max_length=100)        # deleted default field "No title"
    text = models.TextField(blank=True, null=True)  # changed type from CharField to TextField
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def get_gravatar(self):
        # Don't spend too much time worrying about this: This is the example
        # code found online for Gravatar, which is an API to generate avatars
        # based on email (we'll use username in this case).
        email = self.username
        encoded = hashlib.md5(email.encode('utf8')).hexdigest()
        gravatar_url = "http://www.gravatar.com/avatar/" + encoded + "?d=identicon"
        return gravatar_url

    def __str__(self):
        return self.user.username + "'s note: " + self.title

#class TaggedItem(TaggedItemBase):
#    content_object = models.ForeignKey('Note', on_delete=models.CASCADE)
#
#class Tabs(models.Model):
#    tags = TaggableManager(through=TaggedItem)
    


# NOTE: User is a built-in model in Django, which means it's not included in
# models.py since it automatically comes with Django "for free". It has the
# following fields:


# class User:
#    username
#    first_name
#    last_name
#    password
#    email
