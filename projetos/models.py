from django.db import models
from django.contrib.auth.models import User

class ProjetoPesquisa(models.Model):
    STATUS_CHOICES = (
        ('ativo', 'Ativo'),
        ('concluido', 'Concluído'),
        ('pausado', 'Pausado'),
    )

    titulo = models.CharField("Título do Projeto", max_length=200)
    
    descricao = models.TextField("Descrição Detalhada", blank=True, null=True)
    
    orientador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projetos_orientados')
    
    alunos = models.ManyToManyField(User, related_name='projetos_inscritos', blank=True, verbose_name="Alunos Participantes")
    
    data_inicio = models.DateField("Data de Início")
    
    data_fim = models.DateField("Previsão de Término", blank=True, null=True)
    
    status = models.CharField("Situação Atual", max_length=10, choices=STATUS_CHOICES, default='ativo')

    def __str__(self):
        return self.titulo