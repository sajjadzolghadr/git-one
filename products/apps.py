from timeit import default_timer
from django.apps import AppConfig

from sajishop.settings import DEFAULT_AUTO_FIELD


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'



    