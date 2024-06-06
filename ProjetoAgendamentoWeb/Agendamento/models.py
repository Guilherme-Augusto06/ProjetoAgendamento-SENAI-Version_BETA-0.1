from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Importa o modelo de usuário do Django
# Create your models here.
class Senai(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=1500)
    logo = models.ImageField(upload_to='logo/')

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    idade = models.IntegerField()
    data = models.DateField(default=timezone.now)
    quartos = models.CharField(max_length=50)



class Sala(models.Model):
    sala = models.CharField(max_length=50)
    descricao = models.TextField(max_length=50)
    equipamentos = models.CharField(max_length=50)


    def __str__(self):
        return self.sala
    

class DiasDaSemana(models.Model):
    dias = models.CharField(max_length=50)

    def __str__(self):
        return self.dias
    
class Horarios(models.Model):
    horarios = models.TimeField()

    def __str__(self):
        return self.horarios

class Agendamentos(models.Model):
    data = models.DateField()
    def __str__(self):
        return self.data
    


