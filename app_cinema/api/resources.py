# from django.forms import model_to_dict
# from rest_framework.response import Response
#
# from myapp.api.serializers import WomenSerialiser
# from myapp.models import Women
# from rest_framework import generics
# from rest_framework.views import APIView
#
# # class WomenAPIView(generics.ListAPIView):
# #     queryset = Women.objects.all()
# #     serializer_class = WomenSerialiser
# class WomenAPIView(APIView):
#     def get(self,request):
#         lst = Women.objects.all().values()
#         return Response({'sss': list(lst)})
#     def post(self,request):
#         post_new = Women.objects.create(
#             title=request.data['title'],
#             content=request.data['content'],
#             cat_id=request.data['cat_id'],
#         )
#         return Response({'post':model_to_dict(post_new)})
#