from django.urls import path
#from .views import fileUpload
from .views import image_get

urlpatterns = [
    #path('fileupload/', fileUpload, name="fileupload"),
    path('image_get/', image_get.as_view(), name="fileupload"),
]
