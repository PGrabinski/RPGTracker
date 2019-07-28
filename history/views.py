from django.shortcuts import render

from django.views import generic

from .models import Session, Character

from register.models import Player

from .forms import AddCharacterForm

from django.urls import reverse_lazy, reverse

from django.http import HttpResponseRedirect

from pprint import pprint

class IndexView(generic.ListView):
    template_name = 'history/index.html'
    context_object_name = 'session_list'

    def get_queryset(self):
        return Session.objects.all()

class SessionView(generic.DetailView):
    template_name = 'history/session.html'
    model = Session

class CharacterView(generic.DetailView):
    template_name = 'history/character.html'
    model = Character
    def get_queryset(self):
        return Character.objects.filter(player=self.request.user)
    
class AddCharacterView(generic.edit.CreateView):
    template_name = 'history/add_character.html'
    form_class = AddCharacterForm
    success_url = reverse_lazy('history:index')

    def form_valid(self, form):
        character = form.save(commit=False)
        request = self.request
        # pprint(vars(self.request))
        user_request = request.user
        print(user_request)
        player = Player.objects.get(nickname=user_request)
        character.player = player
        character.save()
        return HttpResponseRedirect('character/1')#self.get_success_url)
