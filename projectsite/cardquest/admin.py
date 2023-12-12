from django.contrib import admin
from . import models


@admin.register(models.Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("created_at","updated_at","name", "birthdate", "location", "email")
    search_fields = ("name", "location",)

@admin.register(models.PokemonCard)
class PokemonCardAdmin(admin.ModelAdmin):
    list_display = ("created_at","updated_at","name", "rarity")
    search_fields = ("name",)

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("created_at","updated_at","card", "trainer", "collection_date")
    search_fields = ("card","trainer",)
    