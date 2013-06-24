from clusterEngine.models import Recipe
from django.contrib import admin

class RecipeAdmin(admin.ModelAdmin):
    fields = ['title', 'url', 'img_url', 'ingredient', 'method']
    list_display = ['title', 'url']
admin.site.register(Recipe, RecipeAdmin)
