from django.shortcuts import render

from django.views import generic

from .models import Session

class IndexView(generic.ListView):
    template_name = 'history/index.html'
    context_object_name = 'session_list'

    def get_queryset(self):
        return Session.objects.all()
    
