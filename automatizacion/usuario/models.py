from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
	email = models.EmailField('email address', unique=True)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']
	tipos_usuario = (
		('pg','profesor guía'),
		('d','docente'),
		('a','alumno'),
	)

	tipo_usuario = models.CharField(max_length=2, choices=tipos_usuario, blank=True, help_text='Tipo de usuario')