import io

from .models import Woman
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Model serializer
class WomanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Woman
        fields = '__all__'


# How work Model serializer
# class WomanSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     category_id = serializers.IntegerField()

#     def create(self, validated_data):
#         return Woman.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.time_update = validated_data.get('time_update', instance.time_update)
#         instance.is_published = validated_data.get('is_published', instance.is_published)
#         instance.category = validated_data.get('category', instance.category)
#         instance.save()
#         return instance
    

# # Принцип работы сериалайзера
# class WomanModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# class WomanSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()


# # Кодирование данных из в json
# def encode():
#     model = WomanModel('Woman name', 'Her content')
#     model_sr = WomanSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)


# # Декодирование данных из в json
# def decode():
#     stream = io.BytesIO(b'{"title":"Woman name","content":"Her content"}')
#     data = JSONParser().parse(stream)
#     serializer = WomanSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
