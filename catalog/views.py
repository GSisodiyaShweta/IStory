from django.shortcuts import render, redirect
from .models import Player
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from catalog.forms import PlayerEntryForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def index(request):
    return render(request, 'index.html')


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

