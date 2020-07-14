from django import forms

from .models import add_blog

class add_post(forms.ModelForm):
    class Meta:
        model = add_blog
        fields = ('name','title','catogery','email','post_body','date_pub')