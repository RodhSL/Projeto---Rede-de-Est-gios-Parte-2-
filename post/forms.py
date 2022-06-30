from dataclasses import field
from django import forms
from .models import Postagem

class PostForm(forms.ModelForm):

    class Meta:
        model = Postagem
        fields = ('curso', 'titulo', 'descricao', 'imagem', 'escolaridade', 'remuneracao')

#Outra forma de capturar o user logado     
#def form_valid(self, form):       
# form.instance.user = self.request.user
# return super().form_valid(form)