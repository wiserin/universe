from django import forms
from tinymce.widgets import TinyMCE
from .models import Articles

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Articles
        fields = ['heading', 'content']