from django.contrib import admin
from .models import Service

# Utilisation du décorateur pour enregistrer le modèle dans l'admin
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  # Assure-toi d'utiliser 'title' au lieu de 'name'

# Ou, si tu préfères utiliser la méthode classique (sans décorateur)
# admin.site.register(Service, ServiceAdmin)
