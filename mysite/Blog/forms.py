from django import forms

from .models import Post
from .models import Mail

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','category')

class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ('schlüssel1', 'schlüssel2', 'title', 'nachricht')

class AutoForm(forms.Form):
    schl1 = forms.CharField(label='Schlüssel 1', max_length=20)
    schl2 = forms.CharField(label='Schlüssel 2', max_length=20)






