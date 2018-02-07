from django import forms
from .models import account
from .models import Post
from .models import Mail

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','category')

class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ('mail', 'title', 'nachricht')

class AutoForm(forms.Form):
    schl1 = forms.CharField(label='Mail', max_length=40)
    schl2 = forms.CharField(label='Schlüssel', max_length=20)

class accountForm(forms.ModelForm):
    class Meta:
        model = account
        fields = ('adresse', 'passwort')






