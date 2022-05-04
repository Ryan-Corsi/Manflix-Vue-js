from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# impede a criação de usuários com emails repetidos
User._meta.get_field('email')._unique = True
# impede com que o email seja null ou vazior durante cadastro
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False
# Create your models here.


class Materias(models.Model):
    nome = models.CharField(max_length=55)
    idMaterias = models.BigIntegerField()
    cargaHoraria = models.BigIntegerField()
    periodo = models.CharField(max_length=55)
    ativa = models.BooleanField(default=False)

    def __str__(self):
        return self.nome



def upload_image_user(instance, filename):
    return f"{instance.id}-{timezone.now()}-{filename}"

def upload_image_movie(instance, filename):
    return f"{instance.id}-{timezone.now()}-{filename}"



class Filmes(models.Model):
    nome = models.CharField(max_length=55)
    foto = models.ImageField(upload_to=upload_image_movie, blank=True, null=True)
    categoria_id = models.BigIntegerField()

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=55)

    def __str__(self):
        return self.nome

class Assinatura(models.Model):
    nome = models.CharField(max_length=55)
    valor = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.nome

class Usuarios(models.Model):
    nome = models.CharField(max_length=55)
    idUser = models.ForeignKey(User, related_name="usuario", on_delete=models.CASCADE)
    email = models.CharField(max_length=80)
    fone = models.CharField(max_length=15, null=True, blank=True, default=False)
    cpf  = models.CharField(max_length=14, null=False,blank=False, default=False)
    dtNascimento = models.DateField(null=True, blank=True)
    ativo = models.BooleanField(default=False)
    foto = models.ImageField(upload_to=upload_image_user, blank=True, null=True)

    

    def __str__(self):
        return self.nome

class Favoritos(models.Model):
    filme_id = models.BigIntegerField()
    usuarios_id = models.BigIntegerField()