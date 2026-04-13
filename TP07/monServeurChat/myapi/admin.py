from django.contrib import admin

# Register your models here.
from .models import Message

# Rend le modèle Message visible et gérable depuis /admin
admin.site.register(Message)