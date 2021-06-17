##Third party imports
from rest_framework import serializers
##Local application imports
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('code', 'name', 'size', 'price', 'colour')