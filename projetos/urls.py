from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.ProjetoListView.as_view(), name='lista_projetos'),
    path('projeto/<int:pk>/', views.ProjetoDetailView.as_view(), name='detalhe_projeto'),

    
    path('projeto/novo/', views.ProjetoCreateView.as_view(), name='criar_projeto'),

    path('projeto/<int:pk>/editar/', views.ProjetoUpdateView.as_view(), name='editar_projeto'),

    path('projeto/<int:pk>/deletar/', views.ProjetoDeleteView.as_view(), name='deletar_projeto'),
]