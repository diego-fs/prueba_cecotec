##Third party imports
from django.contrib import admin
##Local application imports
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    search_fields=("code",)
    ordering = ["name"]
    list_display = ('code', 'name', 'price', 'size', 'colour')
    
    class Meta:
        model = Article
        
admin.site.register(Article, ArticleAdmin)


