from .models import Post
from crispy_forms.helper import FormHelper
from django import forms
from crispy_forms.layout import Layout,Column,Row,Submit

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','category','description','relevant_pic']

    def __init__(self,*args,**kwargs):
            super().__init__(*args, **kwargs)
            self.helper=FormHelper()
            self.helper.form_method='POST'
            self.helper.layout=Layout(
                'title',
                'category',
                'description',
                'relevant_pic',
                Submit('submit','Post' ,css_class='btn btn-primary mt-3')
            )   
        