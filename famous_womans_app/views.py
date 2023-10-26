from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import Woman, Category
from .serializers import WomanSerializer

# With generic. ListCreateAPIView (post, get)
class WomenListAPIView(generics.ListCreateAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer


# With base class
class WomenAPIView(APIView):
    def get(self, request):
        queryset = Woman.objects.all()
        return Response({"womans_list": WomanSerializer(queryset, many=True).data})
    
    def post(self, request):
        serializer = WomanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if pk is None:
            return Response({'error': "Ключ не определен"})
        
        try:
            instance = Woman.objects.get(pk=pk)
        except:
            return Response({'error': "Object not found"})

        serializer = WomanSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if pk is None:
            return Response({'error': "Ключ не определен"})

        try:
            instance = Woman.objects.get(pk=pk)
        except:
            return Response({'error': "Object not found"})
        
        instance.delete()

        return Response({'post': f"post {pk} deleted"})


# With generic ListAPIView (get)
# class WomanAPIView(generics.ListAPIView):
#     queryset = Woman.objects.all()
#     serializer_class = WomanSerializer
