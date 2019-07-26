from django.contrib import admin
from .models import Note
from .models import Notebook, TestNotebook, TestNote


# Register your models here.
admin.site.register(Note)
admin.site.register(Notebook)
admin.site.register(TestNotebook)
admin.site.register(TestNote)