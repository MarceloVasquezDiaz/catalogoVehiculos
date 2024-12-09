from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

@receiver(post_save, sender = User)
def assign_view_catalog_permission(sender, instance, created, **kwargs):
    """
    Asigna automáticamente el permiso 'visualizar_catalogo' al registrar un nuevo usuario.
    """
    if created:  # Solo se ejecuta al crear un nuevo usuario
        # Buscar el permiso 'visualizar_catalogo'
        content_type = ContentType.objects.get(app_label='vehiculo', model='Vehiculo')
        permission = Permission.objects.get(codename='visualizar_catalogo', content_type=content_type)
        
        # Asignar el permiso al usuario
        instance.user_permissions.add(permission)