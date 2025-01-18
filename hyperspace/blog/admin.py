from django.contrib import admin
from .models import Blog

# Register your models here.
@admin.register(Blog)
class ServiceAdmin(admin.ModelAdmin):
    list_display=('title','slug','created_by')
    search_fields = ('title','description','created_by')
    list_filter = ('created_by',)
    row_id_fields=['created_by']