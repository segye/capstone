from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ImageSerializer
from .forms import FileUploadForm
from .models import Image


# def fileUpload(request):
#     if request.method == 'POST':
#         img = request.FILES["image"]
#         fileupload = Image(
#             image=img,
#         )
#         fileupload.save()
#         return redirect('fileupload')
#     else:
#         fileuploadForm = FileUploadForm
#         context = {
#             'fileuploadForm': fileuploadForm,
#         }
#         return render(request, 'machine/fileupload.html', context)


class image_get(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ImageSerializer

    def post(self, request):
        data = request.data['image']
        Image.objects.create(image=data)

        return Response('Image was uploaded')
