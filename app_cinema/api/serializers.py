# import io
#
# from rest_framework import serializers
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
#
# from myapp.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
#
# from myapp.models import Women
#
#
# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance
#
#
# # class WomenSerialiser(serializers.ModelSerializer):
# #     class Meta:
# #         model = Women
# #         fields = ('title', 'cat_id')
#
# # class WomenModel:
# #     def __init__(self, title, content):
# #         self.title = title
# #         self.content = content
#
#
# class WomenSerialiser(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField()
#     time_update = serializers.DateTimeField()
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
# # def decode():
# #     stream = io.BytesIO(b'{"title":"angela","content":"Conten: Angela"}')
# #     data = JSONParser().parse(stream)
# #     serializer = WomenSerialiser(data=data)
# #     serializer.is_valid()
# #     print(serializer.validated_data)
# #
# #
# # def encode():
# #     model = WomenModel('angela', 'Conten: Angela')
# #     model_sr = WomenSerialiser(model)
# #     print(model_sr.data, type(model_sr.data), sep='\n')
# #     json = JSONRenderer().render(model_sr.data)
# #     print(json)
