from django import forms
from django.forms import ModelForm, widgets
from .models import *

class FormArticle(forms.ModelForm):
    """docstring for SetVoiture"""

    class Meta(object):
        model = Articles
        fields = '__all__'
        exclude = ('slug',)
        widgets = {
            'art_content': forms.Textarea(attrs={'class': 'col-12 mb-3'}),
            'art_title': forms.TextInput(attrs={'class': 'col-12 mb-3'}),
                }



class FormComment(forms.ModelForm):
    """docstring for SetVoiture"""

    class Meta(object):
        model = Commentaires
        fields = '__all__'
        widgets = {
            'comment_article': forms.HiddenInput(),
            'comment_content': forms.Textarea(attrs={'class': 'col-12'}),
            'comment_author': forms.TextInput(attrs={'class': 'col-7'}),
            'comment_rating': forms.NumberInput(attrs={'class': 'col-7', 'placeholder':'/10','min':'0', 'max':'10'}),
                }




class FormMedia(forms.Form):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'class':'invisible'}))
