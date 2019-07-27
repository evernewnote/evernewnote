from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.accounts.models import User

from apps.core.forms import EditRichTextNote, NewNotebook
from apps.core.models import Note, Notebook


def home(request):
    if request.user.is_authenticated:
        return render(request, 'pages/home.html', {})
    else:
        return render(request, 'pages/exterior.html', {})


def note_change(form, user):
    if form.is_valid():
        note = form.save(commit=False)
        note.user = user
        note.save()
        # print_user_notes(user)
        return form, note.id
    else:
        return None


@login_required
def new_note(request):
    user = User.objects.get(username=request.user)

    if request.method == 'POST':
        form = EditRichTextNote(user, request.POST)

        form, note_id = note_change(form, user)
        return redirect('/view_note/' + str(note_id))
        pass
    else:
        form = EditRichTextNote(user=user, initial={"title": "Title"})
        context = {
            'form': form,
        }
        return render(request, "pages/new_note.html", context)


@login_required
def edit_note(request, note_id):
    note = Note.objects.get(id=note_id)
    user = User.objects.get(username=request.user)

    if request.method == 'POST':
        # form = EditRichTextNote(user, request.POST, instance=note)
        # form = note_change(form, user)
        #
        # # print("test edit note: method is post" + request.META.get('HTTP_REFERER', '/'))
        # return HttpResponseRedirect('/edit_note/' + str(note_id))
        pass
    else:
        print("test edit note: " + request.method + " " + request.META.get('HTTP_REFERER', '/'))
        form = EditRichTextNote(user=user, instance=note)

        context = {
            'form': form,
            'note_id': note_id,
        }
        return render(request, "pages/edit_note.html", context)


@login_required
def save_note(request, note_id):
    note = Note.objects.get(id=note_id)
    user = User.objects.get(username=request.user)
    form = EditRichTextNote(user, request.POST, instance=note)
    form = note_change(form, user)

    return HttpResponseRedirect('/view_note/' + str(note_id))


def view_note(request, note_id):
    note = Note.objects.get(id=note_id)

    context = {
        'note': note,
    }
    return render(request, 'pages/view_note.html', context)


@login_required
def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return HttpResponseRedirect('/exterior/')


@login_required
def new_notebook(request):
    # TODO: hitting enter works but the button doesn't - why?
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        form = NewNotebook(request.POST)
        if form.is_valid():
            notebook = form.save(commit=False)
            notebook.user = user
            notebook.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def edit_notebook(request, notebook_id):
    user = User.objects.get(username=request.user)
    notebook = Notebook.objects.get(id=notebook_id)
    if request.method == 'POST':
        form = NewNotebook(request.POST)
        if form.is_valid():
            notebook = form.save(commit=False)
            notebook.id = notebook_id
            notebook.user = user
            notebook.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def delete_notebook(request, notebook_id):
    notebook = Notebook.objects.get(id=notebook_id)
    notebook.delete()
    # print(notebook.title)
    return redirect(request.META.get('HTTP_REFERER', '/'))


def page_not_found(request):
    return render(request, "404.html")

