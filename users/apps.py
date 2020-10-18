from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # import signals inside ready()
    def ready(self):
    	import users.signals