from django.shortcuts import render, redirect
from .models import Player
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from catalog.forms import PlayerEntryForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'index.html')


@login_required
def story(request):
    return render(request, 'story.html')


def dontshoot(request):
    return render(request, 'dontshoot.yaml')


def register_request(request):
    if request.method == 'POST':
        form = PlayerEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('story')
    form = PlayerEntryForm()
    return render(request, 'register.html', {'form': form})


def save_choices(request):
    if request.method == "POST":
        player = Player()
        player.player_s_choices = request.POST['choices']
        player.save()


class ChoicesSelectedByPlayer(LoginRequiredMixin,generic.ListView):

    model = Player
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
