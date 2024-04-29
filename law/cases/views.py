from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,TemplateView
from .models import Client,Lawyer,Case
from .forms import ClientForm,LawyerForm,CaseForm
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name='home.html'

class ClientListView(ListView):
    model=Client
    template_name='clients/client_list.html'

class ClientCreateView(CreateView):
    model=Client
    form_class=ClientForm
    template_name='clients/client_form.html'
    success_url='/clients/'

class ClientUpdateView(UpdateView):
    model=Client
    form_class=ClientForm
    template_name='clients/client_form.html'
    success_url='/clients/'

class ClientDeleteView(DeleteView):
    model=Client
    template_name='clients/client_confirm_delete.html'
    success_url=reverse_lazy('cases:client_list')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Delete Client'
        return context