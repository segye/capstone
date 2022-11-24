from django.forms import ModelForm
from .models import Image


class FileUploadForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image']
