from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify
from django import forms
from .models import Image

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {
        "url": forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data["url"]
        vectors = ['jpg', 'jpeg']
        vector = url.rsplit(".", 1)[1].lower()
        if vector not in vectors:
            raise forms.ValidationError('The given URL does not match valid image extensions.')
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        url = self.cleaned_data["url"]
        image_name = "{}.{}".format(slugify(self.cleaned_data["title"]), url.rsplit(".", 1)[1].lower())
        #保存
        respond = request.urlopen(url)
        image.image.save(image_name, ContentFile(respond.read()), save=False)

        if commit:
            image.save()
        return image