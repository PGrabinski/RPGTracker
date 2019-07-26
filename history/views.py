from django.shortcuts import render

from django.views import generic

from .models import Session, Character, Player

from .forms import AddCharacterForm

from django.urls import reverse_lazy

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
        print(self.request.user)
        print(Player.objects.get(user=self.request.user))
        return Character.objects.filter(player=Player.objects.get(user=self.request.user))
    
class AddCharacterView(generic.edit.CreateView):
    template_name = 'history/add_character.html'
    form_class = AddCharacterForm
    success_url = reverse_lazy('characters')
