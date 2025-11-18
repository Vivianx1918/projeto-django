from django.contrib.auth import logout
from django.shortcuts import redirect

from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)
from django.urls import reverse_lazy
from .models import ProjetoPesquisa

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class ProjetoListView(ListView):
    model = ProjetoPesquisa
    template_name = 'projetos/lista_projetos.html'
    context_object_name = 'projetos'

class ProjetoDetailView(DetailView):
    model = ProjetoPesquisa
    template_name = 'projetos/detalhe_projeto.html'
    context_object_name = 'projeto'

class ProjetoCreateView(LoginRequiredMixin, CreateView):
    model = ProjetoPesquisa

    fields = ['titulo', 'descricao', 'alunos', 'data_inicio', 'data_fim', 'status']

    template_name = 'projetos/form_projeto.html'
    success_url = reverse_lazy('lista_projetos')

    def form_valid(self, form):
        form.instance.orientador = self.request.user
        return super().form_valid(form)

class ProjetoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ProjetoPesquisa
    fields = ['titulo', 'descricao', 'alunos', 'data_inicio', 'data_fim', 'status']
    template_name = 'projetos/form_projeto.html'
    success_url = reverse_lazy('lista_projetos')

    def test_func(self):
        projeto = self.get_object()
        return self.request.user == projeto.orientador

class ProjetoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ProjetoPesquisa
    template_name = 'projetos/projeto_confirm_delete.html'
    success_url = reverse_lazy('lista_projetos')

    def test_func(self):
        projeto = self.get_object()
        return self.request.user == projeto.orientador

class SignUpView(CreateView):
    
    form_class = UserCreationForm

    success_url = reverse_lazy('login')

    template_name = 'registration/signup.html'  



def logout_view(request):
    
    logout(request)
   
    return redirect('lista_projetos')          