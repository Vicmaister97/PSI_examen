from django.contrib import admin
from aplicacion.models import pizza, ingrediente, contiene

# Register your models here.
admin.site.register(pizza)
admin.site.register(ingrediente)
admin.site.register(contiene)
