from django.apps import AppConfig


class VehiculoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vehiculo'

class UsuarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'
    
    def ready(self):
        import usuarios.signals