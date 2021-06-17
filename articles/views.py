#Third party imports
from django.core.exceptions import ValidationError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

#Local application imports
from .models import Article
from .serializers import ArticleSerializer
##Module imports
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class ArticleList(APIView):
    
    @swagger_auto_schema(
        operation_summary="Gets all the articles stored in the database",
        operation_description="Gets all the articles stored in the database \n Permissions: all",
        responses={
            200: ArticleSerializer(many=True), 
            204: openapi.Response("No content"), 
            400: openapi.Response("Bad Request")
        },
        tags=["articles"]
    )
    def get(self, request):
        try:
            article_list = Article.objects.all()
            if len(article_list > 0):
                serializer_data = ArticleSerializer(article_list, many=True)
                return Response(data=serializer_data.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(f"There has been an error getting the articles {repr(e)}")
            return Response(status=status.HTTP_400_BAD_REQUEST)
       
    @swagger_auto_schema(
        operation_summary="Creates a new article in the database",
        operation_description="Creates a new article in the database \n Permissions: all",
        request_body=openapi.Schema(
            "body",
            "Article parameters",
            openapi.TYPE_OBJECT,
            properties={
                "code": openapi.Schema(type=openapi.TYPE_STRING),
                "name": openapi.Schema(type=openapi.TYPE_STRING),
                "price": openapi.Schema(type=openapi.TYPE_NUMBER),
                "size": openapi.Schema(type=openapi.TYPE_NUMBER),
                "colour": openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            201: ArticleSerializer(many=False),  
            400: openapi.Response("Bad Request")
        },
        tags=["articles"]
    ) 
    def post(self, request):
        data = request.data.copy()
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            try:
                serializer.save()
            except ValidationError as e:
                print(f"There has been an error saving the article instance. Reason {repr(e)}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)