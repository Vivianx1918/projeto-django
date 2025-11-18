from django.contrib import admin
from django.urls import path, include

from projetos.views import SignUpView, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),

   
    path('contas/cadastro/', SignUpView.as_view(), name='signup'),

   
    path('contas/sair/', logout_view, name='logout_manual'), 

   
    path('contas/', include('django.contrib.auth.urls')),

    
    path('', include('projetos.urls')),
]