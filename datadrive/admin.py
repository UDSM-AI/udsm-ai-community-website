from django.contrib import admin
from .models import MovementCategory, Movement, MovementEntry

@admin.register(MovementCategory)
class MovementCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image_url')

@admin.register(Movement)
class MovementAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category')

@admin.register(MovementEntry)
class MovementEntryAdmin(admin.ModelAdmin):
    list_display = ('movement', 'audio_file', 'notes')
