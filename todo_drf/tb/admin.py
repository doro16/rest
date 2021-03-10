from django.contrib import admin

# Register your models here.

from .models import Gltf_json, Gltf_buffer

admin.site.register(Gltf_json)
admin.site.register(Gltf_buffer)