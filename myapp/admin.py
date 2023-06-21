from django.contrib import admin
from .models import Pilihan, Pertanyaan

# Register your models here.
class PilihanAdmin(admin.StackedInline):
    model = Pilihan
    extra = 4
    
class PertanyaanAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["pertanyaan_text"]}),
        ("informasi tanggal", {"fields": ["tanggal_post"], "classes": ["collapse"]}),
    ]
    inlines = [PilihanAdmin]
    
admin.site.register(Pertanyaan, PertanyaanAdmin)
