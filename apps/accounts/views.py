from django import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.accounts.forms import UserEditForm, SignupForm
from apps.accounts.models import User

from apps.core.models import Note, Notebook


class NewNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "text", "notebook"]

    def __init__(self, user, *args, **kwargs):
        super(NewNoteForm, self).__init__(*args, **kwargs)
        self.fields['notebook'].queryset = Notebook.objects.filter(user=user).values_list('title', flat=True)


class NewNotebookForm(forms.ModelForm):
    class Meta:
        model = Notebook
        fields = ["title"]


def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Log-in the user right away
            messages.success(request, 'Account created successfully. Welcome!')
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out.')
    return redirect('home')


def view_all_users(request):
    all_users = User.objects.all()
    context = {
        'users': all_users,
    }
    return render(request, 'accounts/view_all_users.html', context)


def view_profile(request, username):
    user = User.objects.get(username=username)

    if request.user == user:
        is_viewing_self = True

        if request.method == "POST":
            form = NewNoteForm(request.user, request.POST)

            if form.is_valid():
                note = form.save(commit=False)
                note.user = request.user
                note.save()
                return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            form = NewNoteForm(user)
    else:
        is_viewing_self = False
        form = None

    user = User.objects.get(username=username)
    notebooks = Notebook.objects.filter(user=user)

    context = {
        'user': user,
        'is_viewing_self': is_viewing_self,
        'form': form,
        'notebooks': notebooks,
    }
    return render(request, 'accounts/profile_page.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserEditForm(instance=request.user)

    context = {
        'form': form,
    }
    return render(request, 'accounts/edit_profile.html', context)


