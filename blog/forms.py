from django import forms
from django.forms import ModelForm, fields
from .models import Post
from ckeditor.widgets import CKEditorWidget


class BlogPostForm(ModelForm):
    body = forms.CharField(label="توضیحات", widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = ['title', 'body', 'category', 'tags', 'image', 'publish'] 

    def __init__(self, *args, **kwargs):
        super(BlogPostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "یک عنوان انتخاب کنید"