from apps.core.models import Note, Notebook
from apps.accounts.models import User


def menu_items(request):
    if request.user.id:
        user = User.objects.get(username=request.user)
        notebooks = Notebook.objects.filter(user=user)

        notes_by_notebook = {}
        for notebook in notebooks:
            lst = []
            for n in Note.objects.filter(notebook=notebook.id):
                lst.append(n)
            notes_by_notebook[notebook.title] = lst

        return {'notes_by_notebook': notes_by_notebook,
                'notebooks': notebooks,
                }
    else:
        return {}


